# -*- coding: utf-8 -*-
"""L5 · Three-layer episode recorder (proposal §5).
  agent layer   -> episode.json (task, seed, agent, cost, verifier summary, oracle audit) + agent_log.jsonl (reasoning)
  intent layer  -> commands.jsonl (one JSON primitive call + result per line)
  action layer  -> trajectory.npz / trajectory.csv (every control step) + <cam>.mp4 (top / front / wrist at control rate)
  labels.json   -> phase boundaries (per command step range), rule firings, negative segments
  verifier.json -> every verdict with evidence; oracle comparison is appended by finalize() for auditing only"""
from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import imageio.v2 as imageio
import numpy as np

from .backends.base import Observation


class EpisodeRecorder:
    def __init__(self, out_dir: Path, cameras=("top", "front", "wrist"), fps: int = 20, video: bool = True):
        self.dir = Path(out_dir); self.dir.mkdir(parents=True, exist_ok=True)
        self.cameras, self.fps, self.video = cameras, fps, video
        self._writers = {c: imageio.get_writer(str(self.dir / f"{c}.mp4"), fps=fps, codec="libx264", quality=7, macro_block_size=1) for c in cameras} if video else {}
        self.rows: List[Dict[str, Any]] = []
        self.commands: List[Dict[str, Any]] = []
        self.agent_log: List[Dict[str, Any]] = []
        self.phases: List[Dict[str, Any]] = []
        self._phase_start: Optional[int] = None
        self.t_wall0 = time.time()
        self.meta: Dict[str, Any] = {}

    # ------------------------------------------------------------ action layer
    def log_step(self, obs: Observation, dpos, drot, gripper_cmd, primitive: str, cmd_index: int):
        self.rows.append({"step": obs.step, "t_sim": round(float(obs.t), 4), "cmd_index": cmd_index, "primitive": primitive,
                          **{f"eef_{a}": float(v) for a, v in zip("xyz", obs.eef_pos)},
                          **{f"eef_q{a}": float(v) for a, v in zip("xyzw", obs.eef_quat)},
                          "gripper_aperture": float(obs.gripper_aperture), "gripper_cmd": float(gripper_cmd),
                          **{f"dpos_{a}": float(v) for a, v in zip("xyz", dpos)}, **{f"drot_{a}": float(v) for a, v in zip("xyz", drot)},
                          **{f"q{i}": float(v) for i, v in enumerate(obs.joint_pos)}, **{f"dq{i}": float(v) for i, v in enumerate(obs.joint_vel)}})
        if self.video:
            for c in self.cameras:
                if c in obs.rgb: self._writers[c].append_data(obs.rgb[c])

    # ------------------------------------------------------------ intent layer
    def begin_command(self, cmd: Dict[str, Any], step: int):
        self._phase_start = step
        self._current_cmd = cmd

    def end_command(self, cmd: Dict[str, Any], result, step: int, reasoning: str = ""):
        self.commands.append({"index": len(self.commands) + 1, "command": cmd, "result": result.to_json(), "step_range": [self._phase_start, step], "reasoning": reasoning})
        self.phases.append({"index": len(self.commands), "primitive": cmd.get("action"), "step_range": [self._phase_start, step], "status": result.status})

    # ------------------------------------------------------------ agent layer
    def log_agent(self, entry: Dict[str, Any]):
        self.agent_log.append({"wall_s": round(time.time() - self.t_wall0, 3), **entry})

    # ------------------------------------------------------------------ finalize
    def finalize(self, meta: Dict[str, Any], verifier_json, rules_json, labels_extra: Dict[str, Any], oracle: Dict[str, Any]):
        for w in self._writers.values(): w.close()
        # trajectory
        if self.rows:
            keys = list(self.rows[0].keys())
            with open(self.dir / "trajectory.csv", "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(self.rows)
            arrays = {k: np.array([r[k] for r in self.rows]) for k in keys if k != "primitive"}
            arrays["primitive"] = np.array([r["primitive"] for r in self.rows])
            np.savez_compressed(self.dir / "trajectory.npz", **arrays)
        with open(self.dir / "commands.jsonl", "w", encoding="utf-8") as f:
            for c in self.commands: f.write(json.dumps(c, ensure_ascii=False) + "\n")
        with open(self.dir / "agent_log.jsonl", "w", encoding="utf-8") as f:
            for e in self.agent_log: f.write(json.dumps(e, ensure_ascii=False) + "\n")
        final_verdict = next((v for v in reversed(verifier_json) if v["stage"] == "placed_in_bowl"), None)
        verifier_success = bool(final_verdict and final_verdict["passed"])
        audit = {"verifier_success": verifier_success, "oracle_success": bool(oracle.get("success")),
                 "agreement": verifier_success == bool(oracle.get("success")),
                 "type": "TP" if verifier_success and oracle.get("success") else "TN" if not verifier_success and not oracle.get("success") else "FP" if verifier_success else "FN"}
        json.dump({"verdicts": verifier_json, "oracle_audit": audit, "oracle_state": oracle}, open(self.dir / "verifier.json", "w"), indent=1)
        json.dump({"phases": self.phases, "rule_firings": rules_json["firings"], **labels_extra}, open(self.dir / "labels.json", "w"), indent=1, ensure_ascii=False)
        json.dump(rules_json["rules"], open(self.dir / "rules_snapshot.json", "w"), indent=1, ensure_ascii=False)
        ep = {**meta, "n_control_steps": len(self.rows), "n_commands": len(self.commands), "sim_time_s": round(self.rows[-1]["t_sim"], 3) if self.rows else 0.0,
              "wall_time_s": round(time.time() - self.t_wall0, 2), "success": {"verifier": verifier_success, "oracle_audit": audit},
              "files": sorted(p.name for p in self.dir.iterdir())}
        json.dump(ep, open(self.dir / "episode.json", "w"), indent=1, ensure_ascii=False)
        return ep
