# -*- coding: utf-8 -*-
"""L1 · Primitive layer. A fixed, small vocabulary invoked through JSON; every primitive runs until its internal
post-condition (or a step budget) and returns control with a refreshed observation. Safety projection (rule R10)
clamps every commanded target into the workspace and bounds the per-step motion."""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

import numpy as np

from .backends.base import Observation, RobotBackend

VOCABULARY = {
    "move_to":     {"args": ["xyz", "tol?", "speed?", "max_steps?"], "role": "free-space transport to a world-frame target (composite)"},
    "set_gripper": {"args": ["gripper: open|close", "steps?"],          "role": "drive the gripper to a set-point (atomic)"},
    "release":     {"args": ["retreat_dz?"],                            "role": "open the gripper under a release post-condition (atomic)"},
    "contact_act": {"args": ["skill: grasp", "xyz", "descend_dz?", "lift_dz?"], "role": "closed-loop contact primitive (replaceable by a learned VLA/flow head)"},
    "rotate_wrist": {"args": ["dyaw"],                                  "role": "wrist yaw set-point while holding position (atomic)"},
}


@dataclass
class Safety:
    workspace_min: np.ndarray = field(default_factory=lambda: np.array([-0.40, -0.40, 0.815]))
    workspace_max: np.ndarray = field(default_factory=lambda: np.array([0.30, 0.40, 1.20]))
    max_step_m: float = 0.02
    max_step_rad: float = 0.15

    def project(self, xyz: np.ndarray):
        p = np.clip(np.asarray(xyz, dtype=float), self.workspace_min, self.workspace_max)
        return p, bool(np.any(p != np.asarray(xyz, dtype=float)))


@dataclass
class PrimitiveResult:
    action: str
    status: str                 # ok | timeout | empty_grasp | rejected | error
    steps: int
    wall_s: float
    info: Dict[str, Any] = field(default_factory=dict)

    def to_json(self):
        return {"action": self.action, "status": self.status, "steps": self.steps, "wall_s": round(self.wall_s, 3), "info": self.info}


class PrimitiveLibrary:
    def __init__(self, backend: RobotBackend, recorder=None, safety: Optional[Safety] = None):
        self.b, self.rec, self.safety = backend, recorder, safety or Safety()
        self.gripper_cmd = -1.0          # persists across primitives: -1 open, +1 close
        self.obs: Observation = backend.observe()
        self._cmd_index = 0

    # ---------------------------------------------------------------- core
    def _step(self, dpos, drot, primitive: str):
        dpos = np.clip(dpos, -self.safety.max_step_m, self.safety.max_step_m)
        drot = np.clip(drot, -self.safety.max_step_rad, self.safety.max_step_rad)
        self.obs = self.b.servo_step(dpos, drot, self.gripper_cmd)
        if self.rec is not None:
            self.rec.log_step(self.obs, dpos, drot, self.gripper_cmd, primitive, self._cmd_index)
        return self.obs

    def execute(self, cmd: Dict[str, Any]) -> PrimitiveResult:
        """Entry point for JSON commands: {"action": "move_to", "xyz": [...], ...}."""
        self._cmd_index += 1
        t0 = time.time()
        action = cmd.get("action")
        if action not in VOCABULARY:
            return PrimitiveResult(str(action), "rejected", 0, 0.0, {"error": f"unknown primitive; vocabulary={list(VOCABULARY)}"})
        try:
            res = getattr(self, f"_p_{action}")(**{k: v for k, v in cmd.items() if k != "action"})
        except TypeError as e:
            res = PrimitiveResult(action, "rejected", 0, 0.0, {"error": f"bad arguments: {e}"})
        res.wall_s = time.time() - t0
        res.info["eef_pos_after"] = self.obs.eef_pos.round(4).tolist()
        res.info["gripper_aperture_after"] = round(self.obs.gripper_aperture, 3)
        return res

    # ---------------------------------------------------------- primitives
    def _p_move_to(self, xyz, tol=0.008, speed=0.02, max_steps=150):
        target, projected = self.safety.project(np.asarray(xyz, dtype=float))
        speed = min(float(speed), self.safety.max_step_m)
        settled, steps = 0, 0
        for steps in range(1, max_steps + 1):
            err = target - self.obs.eef_pos
            d = float(np.linalg.norm(err))
            if d < tol:
                settled += 1
                if settled >= 2: break
            else:
                settled = 0
            dpos = err if d < speed else err / d * speed
            self._step(dpos, np.zeros(3), "move_to")
        final_err = float(np.linalg.norm(target - self.obs.eef_pos))
        return PrimitiveResult("move_to", "ok" if final_err < tol * 1.5 else "timeout", steps, 0.0,
                               {"target": target.round(4).tolist(), "final_err_m": round(final_err, 4), "safety_projected": projected})

    def _p_set_gripper(self, gripper: str, steps: int = 12):
        self.gripper_cmd = 1.0 if gripper == "close" else -1.0
        for _ in range(int(steps)): self._step(np.zeros(3), np.zeros(3), "set_gripper")
        return PrimitiveResult("set_gripper", "ok", int(steps), 0.0, {"gripper": gripper})

    def _p_release(self, retreat_dz: float = 0.0):
        self.gripper_cmd = -1.0
        steps = 0
        for steps in range(1, 25):
            self._step(np.zeros(3), np.zeros(3), "release")
            if self.obs.gripper_aperture > 0.6: break
        if retreat_dz:
            target = self.obs.eef_pos + np.array([0, 0, float(retreat_dz)])
            r = self._p_move_to(target.tolist(), tol=0.01, max_steps=60); steps += r.steps
        return PrimitiveResult("release", "ok" if self.obs.gripper_aperture > 0.6 else "timeout", steps, 0.0,
                               {"aperture": round(self.obs.gripper_aperture, 3)})

    def _p_rotate_wrist(self, dyaw: float, steps: int = 10):
        per = float(dyaw) / int(steps)
        for _ in range(int(steps)): self._step(np.zeros(3), np.array([0, 0, per]), "rotate_wrist")
        return PrimitiveResult("rotate_wrist", "ok", int(steps), 0.0, {"dyaw": dyaw})

    def _p_contact_act(self, skill: str, xyz, descend_dz: float = 0.0, lift_dz: float = 0.10, approach_dz: float = 0.10):
        """Analytic closed-loop grasp used as the stand-in contact primitive: approach from above, descend, close,
        lift, and report whether something is between the fingers. Post-condition = grasp aperture in (0.05, 0.9)."""
        if skill != "grasp":
            return PrimitiveResult("contact_act", "rejected", 0, 0.0, {"error": "only skill=grasp is implemented"})
        goal = np.asarray(xyz, dtype=float) + np.array([0, 0, float(descend_dz)])
        steps = 0
        self.gripper_cmd = -1.0
        r1 = self._p_move_to((goal + np.array([0, 0, approach_dz])).tolist(), tol=0.006, max_steps=120); steps += r1.steps
        r2 = self._p_move_to(goal.tolist(), tol=0.005, speed=0.012, max_steps=80); steps += r2.steps
        self.gripper_cmd = 1.0
        for _ in range(14): self._step(np.zeros(3), np.zeros(3), "contact_act"); steps += 1
        aperture_closed = self.obs.gripper_aperture
        r3 = self._p_move_to((goal + np.array([0, 0, lift_dz])).tolist(), tol=0.008, max_steps=80); steps += r3.steps
        holding = 0.05 < self.obs.gripper_aperture < 0.9
        return PrimitiveResult("contact_act", "ok" if holding else "empty_grasp", steps, 0.0,
                               {"skill": skill, "goal": goal.round(4).tolist(), "aperture_after_close": round(aperture_closed, 3),
                                "aperture_after_lift": round(self.obs.gripper_aperture, 3), "descend_err_m": r2.info["final_err_m"]})
