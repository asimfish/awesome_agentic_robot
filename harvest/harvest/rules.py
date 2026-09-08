# -*- coding: utf-8 -*-
"""L3 · Rule memory (global rules). Rules are objects with an observable condition, an action for the planner, a label
emitted when they fire, evidence counters and a lifecycle status (see notes/45). The starter set below encodes the ten
rules of the proposal; only those with executable conditions are evaluated by the engine, the rest are documented
constraints that the agent prompt / primitive layer enforce."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Rule:
    id: str
    scope: Dict[str, str]
    condition: str
    action: List[str]
    label: Dict[str, str]
    status: str = "candidate"          # candidate | validated | retired
    provenance: str = "starter set (Harness VLA appendix E + HARVEST proposal), 2026-09-08"
    evidence: Dict[str, int] = field(default_factory=lambda: {"applied": 0, "fixed": 0, "harmed": 0})
    enforced_by: str = "engine"        # engine | primitives | agent | recorder


STARTER_RULES: List[Rule] = [
    Rule("R01_division_of_labor", {"primitive": "*", "phase": "*"}, "phase is contact-rich (grasp/insert/place-in-container)",
         ["use contact_act or hand off to human/RL", "use analytic primitives for grounding/transport/release"], {"phase_boundary": "contact"}, enforced_by="agent"),
    Rule("R02_prestage", {"primitive": "contact_act", "phase": "pre-contact"}, "before any contact primitive the EEF is above the target within the pre-contact pose distribution",
         ["move_to(approach point) first"], {"entry_condition": "pre_contact_pose"}, enforced_by="primitives"),
    Rule("R03_empty_grasp", {"primitive": "contact_act", "phase": "grasp"}, "contact_act returned empty_grasp (fingers closed, nothing between them / object did not move with EEF)",
         ["mark_segment(negative, empty_grasp)", "relocalize(target)", "restage", "retry within budget"], {"outcome": "negative", "failure_type": "empty_grasp"}),
    Rule("R04_no_visual_termination", {"primitive": "*", "phase": "terminal"}, "episode may only be declared successful by the independent verifier (never by the agent, never by the oracle)",
         ["require verifier.placed_in_bowl.passed"], {"terminal": "verifier_gated"}),
    Rule("R05_relocalize", {"primitive": "move_to|contact_act", "phase": "*"}, "target localisation is stale after any robot/object/gripper state change; use median of multiple surface pixels",
         ["localize(target) immediately before the command"], {"grounding": "fresh"}, enforced_by="agent"),
    Rule("R06_output_discipline", {"primitive": "*", "phase": "*"}, "always write episode.json + commands.jsonl + trajectory + labels + verifier, for successes and failures alike",
         ["recorder.finalize() on every exit path"], {"record": "complete"}, enforced_by="recorder"),
    Rule("R07_retry_budget", {"primitive": "contact_act", "phase": "grasp"}, "the same contact segment has been attempted k times (k=2)",
         ["hand off to human takeover / residual RL", "mark segment as needs_completion"], {"handoff": "requested"}),
    Rule("R08_diversity", {"primitive": "*", "phase": "bootstrapping"}, "fewer than m distinct successful skeletons stored for this task (m=3)",
         ["vary staging order / pre-contact pose on the next seed"], {"skeleton": "novel"}, enforced_by="agent"),
    Rule("R09_retiming", {"primitive": "move_to", "phase": "*"}, "motion between waypoints executes with bounded per-step speed and the executed trajectory is what gets recorded",
         ["bounded-speed servo; record executed trajectory"], {"trajectory": "executed_not_planned"}, enforced_by="primitives"),
    Rule("R10_safety_projection", {"primitive": "move_to|contact_act", "phase": "*"}, "commanded target outside workspace or per-step motion above limit",
         ["project target into workspace", "clip step"], {"safety": "projected"}, enforced_by="primitives"),
]


class RuleEngine:
    """Evaluates the executable rules after each primitive result and records every firing."""

    def __init__(self, rules: Optional[List[Rule]] = None, retry_budget: int = 2):
        self.rules = {r.id: r for r in (rules or STARTER_RULES)}
        self.retry_budget = retry_budget
        self.firings: List[Dict[str, Any]] = []
        self.grasp_attempts = 0

    def _fire(self, rid: str, cmd_index: int, detail: Dict[str, Any]):
        self.rules[rid].evidence["applied"] += 1
        self.firings.append({"rule": rid, "cmd_index": cmd_index, "detail": detail, "label": self.rules[rid].label, "action": self.rules[rid].action})

    def after_primitive(self, cmd: Dict[str, Any], result, cmd_index: int) -> List[str]:
        """Returns planner directives derived from the fired rules (e.g. 'retry', 'handoff')."""
        directives: List[str] = []
        if result.action in ("move_to", "contact_act") and result.info.get("safety_projected"):
            self._fire("R10_safety_projection", cmd_index, {"target": result.info.get("target")})
        if result.action == "contact_act":
            self.grasp_attempts += 1
            if result.status == "empty_grasp":
                self._fire("R03_empty_grasp", cmd_index, {"aperture_after_lift": result.info.get("aperture_after_lift")})
                if self.grasp_attempts >= self.retry_budget:
                    self._fire("R07_retry_budget", cmd_index, {"attempts": self.grasp_attempts}); directives.append("handoff")
                else:
                    directives.append("retry")
        return directives

    def to_json(self):
        return {"rules": [asdict(r) for r in self.rules.values()], "firings": self.firings}
