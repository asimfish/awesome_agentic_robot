# -*- coding: utf-8 -*-
"""Perception isolation (Harness VLA appendix E.2): the agent never reads object poses. It localises entities by
picking pixels of the visible surface in RGB, indexing the depth/world map at those pixels and taking a robust
median (rule R05). Colour thresholds stand in for a detector; swap `object_mask` for a VLM/segmenter on real robots."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from .backends.base import Observation, RobotBackend

BLOCK_HALF = 0.021   # m, red block half-size (from the scene spec, not from the simulator state)
BOWL_HEIGHT = 0.045  # m


def object_mask(rgb: np.ndarray, target: str) -> np.ndarray:
    img = rgb.astype(int)
    if target == "block":
        return (img[..., 0] > 150) & (img[..., 1] < 80) & (img[..., 2] < 80)
    if target == "bowl":
        return (img[..., 2] > 150) & (img[..., 0] < 80) & (img[..., 1] < 120)
    raise ValueError(target)


@dataclass
class Localization:
    target: str
    cam: str
    n_px: int
    centroid_px: Optional[np.ndarray]     # (row, col) image-up
    bbox_px: Optional[tuple]              # (r0, c0, r1, c1)
    surface_xyz: Optional[np.ndarray]     # median of back-projected visible-surface points
    spread_m: float                       # robust spread of the sampled points (m)

    @property
    def found(self): return self.surface_xyz is not None

    def to_json(self):
        return {"target": self.target, "cam": self.cam, "n_px": self.n_px,
                "centroid_px": None if self.centroid_px is None else self.centroid_px.round(1).tolist(),
                "bbox_px": self.bbox_px, "surface_xyz": None if self.surface_xyz is None else self.surface_xyz.round(4).tolist(),
                "spread_m": round(self.spread_m, 4)}


def localize(obs: Observation, backend: RobotBackend, target: str, cam: str = "top", n_samples: int = 40, rng=None) -> Localization:
    mask = object_mask(obs.rgb[cam], target)
    ys, xs = np.nonzero(mask)
    if len(ys) < 4:
        return Localization(target, cam, int(len(ys)), None, None, None, 0.0)
    rng = rng or np.random.default_rng(0)
    pix = np.stack([ys, xs], 1)
    sel = pix[rng.choice(len(pix), min(n_samples, len(pix)), replace=False)]
    pts = backend.pixels_to_world(cam, sel, obs.depth[cam])
    med = np.median(pts, axis=0)
    spread = float(np.median(np.linalg.norm(pts - med, axis=1)))
    return Localization(target, cam, int(len(ys)), np.array([ys.mean(), xs.mean()]),
                        (int(ys.min()), int(xs.min()), int(ys.max()), int(xs.max())), med, spread)


def block_grasp_point(loc: Localization) -> np.ndarray:
    """Grasp centre = visible top-surface median lowered by one half-size (geometry prior, not simulator state)."""
    return loc.surface_xyz - np.array([0, 0, BLOCK_HALF])


def bowl_drop_point(loc: Localization, height_above_rim: float = 0.06) -> np.ndarray:
    """Point above the bowl interior: XY median of the visible bowl pixels, Z = visible rim/floor median + clearance."""
    return loc.surface_xyz + np.array([0, 0, height_above_rim])
