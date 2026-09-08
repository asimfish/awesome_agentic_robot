# -*- coding: utf-8 -*-
"""Robot backend interface. The primitive layer only talks to this interface, so a real arm (ROS 2 / vendor SDK)
replaces the simulator by implementing the same six methods. Units: metres, radians, seconds."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional

import numpy as np


@dataclass
class Observation:
    t: float                              # wall/sim time (s)
    step: int                             # control step index
    eef_pos: np.ndarray                   # (3,) world frame
    eef_quat: np.ndarray                  # (4,) xyzw
    gripper_aperture: float               # 0 = fully closed, 1 = fully open (normalised)
    joint_pos: np.ndarray
    joint_vel: np.ndarray
    rgb: Dict[str, np.ndarray] = field(default_factory=dict)     # cam -> HxWx3 uint8, image-up orientation
    depth: Dict[str, np.ndarray] = field(default_factory=dict)   # cam -> HxW float32 metres
    force: Optional[np.ndarray] = None     # (3,) end-effector force if available
    extra: Dict[str, Any] = field(default_factory=dict)


class RobotBackend:
    control_freq: float = 20.0
    cameras: tuple = ("top", "front", "wrist")

    def reset(self, seed: Optional[int] = None) -> Observation: raise NotImplementedError
    def observe(self, with_images: bool = True) -> Observation: raise NotImplementedError
    def servo_step(self, dpos: np.ndarray, drot: np.ndarray, gripper: float) -> Observation:
        """One control step: Cartesian delta (m, rad) in the base frame + gripper command in [-1 open, +1 close]."""
        raise NotImplementedError
    def camera_model(self, cam: str):
        """Return (camera_to_world 4x4 transform, intrinsics 3x3) for pixel -> world back-projection."""
        raise NotImplementedError
    def pixels_to_world(self, cam: str, pixels: np.ndarray, depth: np.ndarray) -> np.ndarray: raise NotImplementedError
    def oracle(self) -> Dict[str, Any]:
        """Privileged state (object poses, success predicate). Never shown to the agent; used only to audit the verifier."""
        return {}
    def close(self): pass
