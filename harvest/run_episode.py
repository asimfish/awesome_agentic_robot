# -*- coding: utf-8 -*-
"""Run one HARVEST episode: agent -> JSON primitive -> primitive layer -> backend, with rules, verifier and the
three-layer recorder. Usage:
  MUJOCO_GL=cgl <robocore>/.venv/bin/python run_episode.py --seed 0 --out data/episodes/ep_0000 [--agent scripted|llm]"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest.agent import LLMAgent, ScriptedAgent          # noqa: E402
from harvest.backends.robosuite_backend import RobosuiteBackend  # noqa: E402
from harvest.primitives import PrimitiveLibrary            # noqa: E402
from harvest.recorder import EpisodeRecorder               # noqa: E402
from harvest.rules import RuleEngine                       # noqa: E402
from harvest.verifier import Verifier                      # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default="data/episodes/ep_0000")
    ap.add_argument("--agent", default="scripted", choices=["scripted", "llm"])
    ap.add_argument("--max-commands", type=int, default=12)
    ap.add_argument("--no-video", action="store_true")
    a = ap.parse_args()

    t0 = time.time()
    backend = RobosuiteBackend(seed=a.seed)
    obs = backend.reset(seed=a.seed)
    rec = EpisodeRecorder(Path(a.out), video=not a.no_video)
    prims = PrimitiveLibrary(backend, recorder=rec)
    rules = RuleEngine()
    ver = Verifier(backend)
    agent = ScriptedAgent() if a.agent == "scripted" else LLMAgent()
    agent.reset()

    ctx = {"obs": obs, "backend": backend, "recorder": rec, "rules": rules, "localizations": [], "directives": [], "grasp_verdict": None, "tokens": 0}
    outcome = "running"
    for i in range(a.max_commands):
        cmd = agent.next_command(ctx)
        rec.log_agent({"turn": i + 1, "reasoning": getattr(agent, "reason", ""), "command": cmd})
        if cmd is None:
            outcome = "agent_stopped"; break
        before = prims.obs
        rec.begin_command(cmd, before.step)
        res = prims.execute(cmd)
        rec.end_command(cmd, res, prims.obs.step, reasoning=getattr(agent, "reason", ""))
        ctx["obs"] = prims.obs
        ctx["directives"] = rules.after_primitive(cmd, res, i + 1)
        ctx["grasp_verdict"] = None
        if cmd["action"] == "contact_act":
            ctx["grasp_verdict"] = ver.check_grasp(before, prims.obs)
        if cmd["action"] == "move_to" and agent.__dict__.get("stage") == "lower":
            ver.check_above_bowl(prims.obs)
        if cmd["action"] == "release":
            final = ver.check_placed(prims.obs)
            outcome = "verified_success" if final.passed else "verifier_rejected"
            break
        if "handoff" in ctx["directives"]:
            outcome = "needs_completion"; break
    else:
        outcome = "max_commands"

    oracle = backend.oracle()
    meta = {"task": "block_to_bowl", "backend": "robosuite/BlockToBowl (Panda, OSC_POSE, 20 Hz)", "seed": a.seed, "agent": agent.name,
            "outcome": outcome, "cost": {"llm_tokens": ctx["tokens"], "usd_estimate": 0.0 if a.agent == "scripted" else None,
                                          "robot_seconds_sim": None, "human_seconds": 0},
            "localizations": ctx["localizations"], "primitive_vocabulary": list(__import__("harvest.primitives", fromlist=["VOCABULARY"]).VOCABULARY)}
    ep = rec.finalize(meta, ver.to_json(), rules.to_json(), {"outcome": outcome}, oracle)
    ep["cost"]["robot_seconds_sim"] = ep["sim_time_s"]
    json.dump(ep, open(Path(a.out) / "episode.json", "w"), indent=1, ensure_ascii=False)
    backend.close()
    print(json.dumps({"outcome": outcome, "verifier_success": ep["success"]["verifier"], "oracle_success": oracle["success"],
                      "audit": ep["success"]["oracle_audit"]["type"], "commands": ep["n_commands"], "control_steps": ep["n_control_steps"],
                      "sim_s": ep["sim_time_s"], "wall_s": round(time.time() - t0, 1), "rule_firings": [f["rule"] for f in rules.firings], "out": a.out}, ensure_ascii=False))


if __name__ == "__main__":
    main()
