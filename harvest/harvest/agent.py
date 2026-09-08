# -*- coding: utf-8 -*-
"""L2 · Agent interface. An agent sees a perception-isolated context (images, EEF pose, gripper aperture, localisation
results it asked for, memory) and returns ONE JSON primitive call per turn (Harness VLA's REPL contract).

ScriptedAgent  : deterministic recipe agent — the stand-in used when no LLM API is available. It exercises exactly
                 the same interface so that the rest of the stack (rules, verifier, recorder) is validated end to end.
LLMAgent       : drop-in planner backed by any OpenAI-compatible chat endpoint; prompt modules follow Harness VLA
                 appendix E (role, perception isolation, JSON REPL, primitive vocabulary, division of labour, memory)."""
from __future__ import annotations

import json
import os
from typing import Any, Dict, Optional

import numpy as np

from .perception import block_grasp_point, bowl_drop_point, localize
from .primitives import VOCABULARY


class Agent:
    name = "agent"
    def reset(self): ...
    def next_command(self, ctx: Dict[str, Any]) -> Optional[Dict[str, Any]]: raise NotImplementedError


class ScriptedAgent(Agent):
    """Recipe: localize block -> contact_act(grasp) -> [verify grasp; retry on empty grasp] -> move above bowl ->
    lower -> release -> retreat -> done. Every move re-localises its target right before the call (rule R05)."""
    name = "scripted-v0"

    def reset(self):
        self.stage = "grasp"
        self.reason = ""

    def next_command(self, ctx):
        obs, backend, directives = ctx["obs"], ctx["backend"], ctx.get("directives", [])
        if "handoff" in directives:
            self.reason = "retry budget exhausted -> hand off (human takeover / residual RL); ending episode as needs_completion"
            return None
        if self.stage == "grasp":
            loc = localize(obs, backend, "block"); ctx["localizations"].append(loc.to_json())
            if not loc.found:
                self.reason = "block not visible in top camera; aborting"; return None
            self.reason = f"block surface median at {loc.surface_xyz.round(3).tolist()} from {loc.n_px} px; grasp one half-size below the top face"
            self.stage = "to_bowl"
            return {"action": "contact_act", "skill": "grasp", "xyz": block_grasp_point(loc).round(4).tolist(), "lift_dz": 0.12}
        if self.stage == "to_bowl":
            if "retry" in directives:
                self.stage = "grasp"; self.reason = "empty grasp reported by primitive + rule R03 -> relocalize and retry"
                return self.next_command(ctx)
            if ctx.get("grasp_verdict") is not None and not ctx["grasp_verdict"].passed:
                self.stage = "grasp"; self.reason = "verifier did not confirm the grasp -> relocalize and retry"; return self.next_command(ctx)
            loc = localize(obs, backend, "bowl"); ctx["localizations"].append(loc.to_json())
            if not loc.found:
                self.reason = "bowl not visible; aborting"; return None
            self.drop = bowl_drop_point(loc, height_above_rim=0.10)
            self.reason = f"bowl surface median {loc.surface_xyz.round(3).tolist()}; transport 10 cm above it"
            self.stage = "lower"
            return {"action": "move_to", "xyz": self.drop.round(4).tolist(), "tol": 0.01}
        if self.stage == "lower":
            self.stage = "release"; self.reason = "lower to 4 cm above the bowl surface before releasing"
            return {"action": "move_to", "xyz": (self.drop - np.array([0, 0, 0.06])).round(4).tolist(), "tol": 0.008, "speed": 0.015}
        if self.stage == "release":
            self.stage = "done"; self.reason = "release and retreat 10 cm; final success is decided by the verifier (rule R04)"
            return {"action": "release", "retreat_dz": 0.10}
        return None


PROMPT_MODULES = {
 "role": "You are an LLM-in-the-loop hybrid manipulation agent. A driver is running and waiting for your commands. Complete the task by reading the state, localising objects from perception, choosing primitives, and writing one JSON command per turn.",
 "perception_isolation": "You never receive object poses. Localise entities by naming the pixels you want back-projected; the driver returns the median world point of the visible surface.",
 "repl": "Output exactly one JSON object per turn: {\"action\": <primitive>, ...args}. Wait for the result before the next command.",
 "vocabulary": json.dumps(VOCABULARY),
 "division_of_labour": "contact_act for contact-rich phases (grasp); move_to / release for grounding, transport and release; re-localise before every targeted command.",
 "memory": "Task-recipe memory (previous successful skeleton) and global rules are provided; follow the rules, never declare success yourself.",
}


class LLMAgent(Agent):
    name = "llm"
    def __init__(self, model: str = "gpt-6-astra", base_url: Optional[str] = None):
        self.model, self.base_url = model, base_url
        self.key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY")
        if not self.key:
            raise RuntimeError("LLMAgent needs OPENAI_API_KEY (or DEEPSEEK_API_KEY); use --agent scripted otherwise")

    def reset(self): self.history = []

    def next_command(self, ctx):
        from openai import OpenAI  # optional dependency
        client = OpenAI(api_key=self.key, base_url=self.base_url)
        obs = ctx["obs"]
        state = {"eef_pos": obs.eef_pos.round(4).tolist(), "gripper_aperture": round(obs.gripper_aperture, 3),
                 "localizations": ctx["localizations"][-4:], "last_results": [c["result"] for c in ctx["recorder"].commands[-3:]],
                 "directives": ctx.get("directives", []), "rules": [r["id"] + ": " + r["condition"] for r in ctx["rules"].to_json()["rules"]]}
        messages = [{"role": "system", "content": "\n\n".join(f"## {k}\n{v}" for k, v in PROMPT_MODULES.items())}] + self.history + \
                   [{"role": "user", "content": json.dumps(state)}]
        r = client.chat.completions.create(model=self.model, messages=messages, response_format={"type": "json_object"})
        text = r.choices[0].message.content
        self.history += [{"role": "user", "content": json.dumps(state)}, {"role": "assistant", "content": text}]
        ctx["tokens"] = ctx.get("tokens", 0) + (r.usage.total_tokens if r.usage else 0)
        cmd = json.loads(text)
        self.reason = cmd.pop("reasoning", "")
        return None if cmd.get("action") == "done" else cmd
