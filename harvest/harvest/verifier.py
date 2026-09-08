# -*- coding: utf-8 -*-
"""L4 · Independent verifier. Reads only what a real robot would have: RGB-D from the top and front cameras, the
end-effector pose and the gripper aperture. It never reads simulator state; the oracle predicate is compared against
its verdicts only afterwards, by the recorder, to audit false positives / negatives (principle C of the proposal).

Stage checks (AGM-style physical evidence + cross-view comparison):
  grasped        gripper holds something AND the block's estimated height rose by >3 cm AND the block estimate is
                 within 4 cm (XY) of the end-effector after the lift
  above_bowl     EEF XY is inside the bowl footprint estimated from the top camera
  placed_in_bowl block estimate inside the bowl footprint (top cam), block resting at bowl-floor level, gripper open,
                 and cross-view agreement from the front camera"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import numpy as np

from .backends.base import Observation, RobotBackend
from .perception import BLOCK_HALF, BOWL_HEIGHT, Localization, localize, object_mask


@dataclass
class Verdict:
    stage: str
    passed: bool
    confidence: float
    evidence: Dict[str, Any] = field(default_factory=dict)

    def to_json(self):
        return {"stage": self.stage, "passed": self.passed, "confidence": round(self.confidence, 3), "evidence": self.evidence}


def _footprint(loc: Localization, shrink: float = 0.02):
    """Axis-aligned bowl footprint from the top-camera bbox back-projected via the median surface height."""
    return loc.surface_xyz[:2], np.array([0.14, 0.14]) / 2 - shrink   # bowl half-size prior (scene spec), shrunk margin


class Verifier:
    def __init__(self, backend: RobotBackend):
        self.b = backend
        self.verdicts: List[Verdict] = []

    def check_grasp(self, before: Observation, after: Observation) -> Verdict:
        b0, b1 = localize(before, self.b, "block"), localize(after, self.b, "block")
        holding = 0.05 < after.gripper_aperture < 0.9
        moved_px = float(np.linalg.norm(b1.centroid_px - b0.centroid_px)) if (b0.found and b1.found) else None
        dz = float(b1.surface_xyz[2] - b0.surface_xyz[2]) if (b0.found and b1.found) else None
        eef_dz = float(after.eef_pos[2] - before.eef_pos[2])
        checks = {"holding_aperture": holding,
                  "block_moved_in_image": moved_px is not None and moved_px > 8.0,
                  "block_rose": dz is not None and dz > 0.03,
                  "block_near_eef": b1.found and float(np.linalg.norm(b1.surface_xyz[:2] - after.eef_pos[:2])) < 0.04}
        conf = sum(checks.values()) / len(checks)
        v = Verdict("grasped", checks["holding_aperture"] and checks["block_rose"] and checks["block_near_eef"], conf,
                    {**checks, "moved_px": None if moved_px is None else round(moved_px, 1), "block_dz_m": None if dz is None else round(dz, 3),
                     "eef_dz_over_primitive_m": round(eef_dz, 3), "aperture": round(after.gripper_aperture, 3)})
        self.verdicts.append(v); return v

    def check_above_bowl(self, obs: Observation) -> Verdict:
        bowl = localize(obs, self.b, "bowl")
        if not bowl.found:
            v = Verdict("above_bowl", False, 0.0, {"bowl_found": False}); self.verdicts.append(v); return v
        c, half = _footprint(bowl)
        inside = bool(np.all(np.abs(obs.eef_pos[:2] - c) < half))
        v = Verdict("above_bowl", inside, 1.0 if inside else 0.0, {"eef_xy": obs.eef_pos[:2].round(3).tolist(), "bowl_xy": c.round(3).tolist(), "half": half.round(3).tolist()})
        self.verdicts.append(v); return v

    def check_placed(self, obs: Observation) -> Verdict:
        top_block, top_bowl = localize(obs, self.b, "block"), localize(obs, self.b, "bowl")
        checks: Dict[str, Any] = {"gripper_open": obs.gripper_aperture > 0.6, "block_visible_top": top_block.found, "bowl_visible_top": top_bowl.found}
        if top_block.found and top_bowl.found:
            c, half = _footprint(top_bowl)
            checks["block_inside_footprint"] = bool(np.all(np.abs(top_block.surface_xyz[:2] - c) < half))
            # the bowl's visible-surface median from the top camera is its floor (largest area); a block resting on that
            # floor shows its top face one block-height above it. Allow 3 cm for depth bias; reject anything higher (on the rim / held).
            rise = float(top_block.surface_xyz[2] - top_bowl.surface_xyz[2])
            checks["block_resting_on_floor"] = bool(rise < 2 * BLOCK_HALF + 0.03)
            checks["block_rise_over_bowl_floor_m"] = round(rise, 3)
        else:
            checks["block_inside_footprint"] = False; checks["block_resting_on_floor"] = False
        # cross-view: in the front camera the block centroid should fall inside the bowl's bbox (or be occluded by its wall)
        fb, fw = localize(obs, self.b, "block", cam="front"), localize(obs, self.b, "bowl", cam="front")
        if fw.found:
            r0, c0, r1, c1 = fw.bbox_px
            if fb.found:
                checks["front_view_agrees"] = bool(r0 - 6 <= fb.centroid_px[0] <= r1 + 6 and c0 - 6 <= fb.centroid_px[1] <= c1 + 6)
            else:
                checks["front_view_agrees"] = True   # occluded by the bowl wall from the front: consistent with being inside
        else:
            checks["front_view_agrees"] = False
        core = ["gripper_open", "block_inside_footprint", "block_resting_on_floor", "front_view_agrees"]
        passed = all(checks[k] for k in core)
        conf = sum(bool(checks[k]) for k in core) / len(core)
        v = Verdict("placed_in_bowl", passed, conf, {**checks, "block_est": None if not top_block.found else top_block.surface_xyz.round(3).tolist(),
                                                     "bowl_est": None if not top_bowl.found else top_bowl.surface_xyz.round(3).tolist()})
        self.verdicts.append(v); return v

    def to_json(self):
        return [v.to_json() for v in self.verdicts]
