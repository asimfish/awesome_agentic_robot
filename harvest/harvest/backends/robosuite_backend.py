# -*- coding: utf-8 -*-
"""robosuite (MuJoCo) backend for the BlockToBowl task. Camera names are mapped to the generic
top / front / wrist roles used by the primitive layer, the verifier and the recorder."""
from __future__ import annotations

import os
import time
from typing import Dict, Optional

import numpy as np

os.environ.setdefault("MUJOCO_GL", "cgl")
import robosuite as suite  # noqa: E402
import robosuite.utils.camera_utils as cu  # noqa: E402
from robosuite.controllers import load_composite_controller_config  # noqa: E402

from . import block_to_bowl_env  # noqa: F401  (registers BlockToBowl)
from .base import Observation, RobotBackend

CAM_MAP = {"top": "agentview", "front": "frontview", "wrist": "robot0_eye_in_hand"}
GRIPPER_OPEN_QPOS = 0.04  # Panda gripper: |qpos| ~0.04 fully open, ~0 closed


class RobosuiteBackend(RobotBackend):
    control_freq = 20.0
    cameras = ("top", "front", "wrist")

    def __init__(self, image_hw=(240, 320), seed: Optional[int] = None):
        cfg = load_composite_controller_config(controller="BASIC", robot="Panda")
        self.env = suite.make("BlockToBowl", robots="Panda", controller_configs=cfg, has_renderer=False,
                              has_offscreen_renderer=True, use_camera_obs=True, camera_names=list(CAM_MAP.values()),
                              camera_heights=image_hw[0], camera_widths=image_hw[1], camera_depths=True,
                              control_freq=int(self.control_freq), horizon=100000, ignore_done=True, seed=seed)
        self.hw = image_hw
        self._step = 0
        self._last_raw = None

    # ------------------------------------------------------------- helpers
    def _to_obs(self, raw, with_images=True) -> Observation:
        rgb, depth = {}, {}
        if with_images:
            for role, cam in CAM_MAP.items():
                rgb[role] = raw[f"{cam}_image"][::-1].copy()                # flip to image-up
                depth[role] = cu.get_real_depth_map(self.env.sim, raw[f"{cam}_depth"])[::-1, :, 0].astype(np.float32)
        gq = raw["robot0_gripper_qpos"]
        aperture = float(np.clip(abs(gq[0] - gq[1]) / (2 * GRIPPER_OPEN_QPOS), 0, 1))
        return Observation(t=self.env.sim.data.time, step=self._step, eef_pos=np.array(raw["robot0_eef_pos"]),
                           eef_quat=np.array(raw["robot0_eef_quat"]), gripper_aperture=aperture,
                           joint_pos=np.array(raw["robot0_joint_pos"]), joint_vel=np.array(raw["robot0_joint_vel"]),
                           rgb=rgb, depth=depth, force=None)

    # ------------------------------------------------------------ interface
    def reset(self, seed: Optional[int] = None) -> Observation:
        if seed is not None:
            self.env.rng = np.random.default_rng(seed)
            self.env.placement_initializer.rng = self.env.rng
            for s in self.env.placement_initializer.samplers.values(): s.rng = self.env.rng
        self._last_raw = self.env.reset()
        self._step = 0
        return self._to_obs(self._last_raw)

    def observe(self, with_images: bool = True) -> Observation:
        return self._to_obs(self._last_raw, with_images)

    def servo_step(self, dpos, drot, gripper) -> Observation:
        a = np.zeros(self.env.action_dim, dtype=np.float32)
        a[:3] = np.clip(np.asarray(dpos) / 0.05, -1, 1)      # OSC_POSE output_max 0.05 m / step
        a[3:6] = np.clip(np.asarray(drot) / 0.5, -1, 1)      # 0.5 rad / step
        a[6] = float(np.clip(gripper, -1, 1))
        self._last_raw, _, _, _ = self.env.step(a)
        self._step += 1
        return self._to_obs(self._last_raw, with_images=True)

    def camera_model(self, cam: str):
        name = CAM_MAP[cam]
        return cu.get_camera_transform_matrix(self.env.sim, name, *self.hw), cu.get_camera_intrinsic_matrix(self.env.sim, name, *self.hw)

    def pixels_to_world(self, cam: str, pixels: np.ndarray, depth: np.ndarray) -> np.ndarray:
        """pixels: (N,2) (row, col) in image-up orientation; depth: HxW metres (image-up). Vectorised version of
        robosuite.utils.camera_utils.transform_from_pixels_to_world (which also uses image-up pixel rows)."""
        name = CAM_MAP[cam]
        h = self.hw[0]
        T_w2p = cu.get_camera_transform_matrix(self.env.sim, name, *self.hw)   # world -> pixel (4x4)
        T_p2w = np.linalg.inv(T_w2p)
        rows_up = np.clip(pixels[:, 0].astype(int), 0, h - 1)
        cols = np.clip(pixels[:, 1].astype(int), 0, self.hw[1] - 1)
        z = depth[rows_up, cols]                                   # depth is image-up like the pixels
        # robosuite's camera matrix is expressed in the image-up orientation (verified by forward projection)
        cam_pts = np.stack([cols * z, rows_up * z, z, np.ones_like(z)], axis=1)   # (N,4)
        return (T_p2w @ cam_pts.T).T[:, :3]

    def oracle(self):
        env = self.env
        return {"block_pos": env.sim.data.body_xpos[env.block_body_id].tolist(),
                "bowl_pos": env.sim.data.body_xpos[env.bowl_body_id].tolist(),
                "success": bool(env._check_success())}

    def close(self):
        self.env.close()
