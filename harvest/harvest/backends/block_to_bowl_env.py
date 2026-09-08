# -*- coding: utf-8 -*-
"""BlockToBowl: a minimal robosuite task — pick the red block and put it into the bowl (a Bin container).

Built from robosuite 1.5 primitives (TableArena, BoxObject, Bin). The oracle success predicate below is used
ONLY to audit the independent verifier (see harvest/verifier.py); the agent never reads it."""
from __future__ import annotations

import numpy as np
from robosuite.environments.manipulation.manipulation_env import ManipulationEnv
from robosuite.models.arenas import TableArena
from robosuite.models.objects import Bin, BoxObject
from robosuite.models.tasks import ManipulationTask
from robosuite.utils.mjcf_utils import CustomMaterial
from robosuite.utils.observables import Observable, sensor
from robosuite.utils.placement_samplers import SequentialCompositeSampler, UniformRandomSampler

BOWL_SIZE = (0.14, 0.14, 0.045)  # x, y, height (m)


class BlockToBowl(ManipulationEnv):
    def __init__(self, robots="Panda", table_full_size=(0.8, 0.8, 0.05), table_offset=(0, 0, 0.8), seed=None, **kwargs):
        self.table_full_size = table_full_size
        self.table_friction = (1.0, 5e-3, 1e-4)
        self.table_offset = np.array(table_offset)
        self.placement_initializer = None
        super().__init__(robots=robots, seed=seed, **kwargs)

    # ---------------------------------------------------------------- model
    def _load_model(self):
        super()._load_model()
        xpos = self.robots[0].robot_model.base_xpos_offset["table"](self.table_full_size[0])
        self.robots[0].robot_model.set_base_xpos(xpos)
        arena = TableArena(table_full_size=self.table_full_size, table_friction=self.table_friction, table_offset=self.table_offset)
        arena.set_origin([0, 0, 0])
        redwood = CustomMaterial(texture="WoodRed", tex_name="redwood", mat_name="redwood_mat",
                                 tex_attrib={"type": "cube"}, mat_attrib={"texrepeat": "1 1", "specular": "0.4", "shininess": "0.1"})
        self.block = BoxObject(name="block", size_min=[0.02, 0.02, 0.02], size_max=[0.022, 0.022, 0.022],
                               rgba=[1, 0, 0, 1], material=redwood, rng=self.rng)
        self.bowl = Bin(name="bowl", bin_size=BOWL_SIZE, wall_thickness=0.008, transparent_walls=False,
                        use_texture=False, rgba=(0.15, 0.35, 0.85, 1.0))
        self.placement_initializer = SequentialCompositeSampler(name="ObjectSampler")
        self.placement_initializer.append_sampler(UniformRandomSampler(
            name="BlockSampler", mujoco_objects=self.block, x_range=[-0.12, -0.02], y_range=[-0.22, -0.08],
            rotation=None, ensure_object_boundary_in_range=False, ensure_valid_placement=True,
            reference_pos=self.table_offset, z_offset=0.01, rng=self.rng))
        self.placement_initializer.append_sampler(UniformRandomSampler(
            name="BowlSampler", mujoco_objects=self.bowl, x_range=[-0.10, 0.0], y_range=[0.10, 0.22],
            rotation=0.0, ensure_object_boundary_in_range=False, ensure_valid_placement=True,
            reference_pos=self.table_offset, z_offset=0.0, rng=self.rng))
        self.model = ManipulationTask(mujoco_arena=arena, mujoco_robots=[r.robot_model for r in self.robots],
                                      mujoco_objects=[self.block, self.bowl])

    def _setup_references(self):
        super()._setup_references()
        self.block_body_id = self.sim.model.body_name2id(self.block.root_body)
        self.bowl_body_id = self.sim.model.body_name2id(self.bowl.root_body)

    def _setup_observables(self):
        observables = super()._setup_observables()
        modality = "object"

        @sensor(modality=modality)
        def block_pos(obs_cache):
            return np.array(self.sim.data.body_xpos[self.block_body_id])

        @sensor(modality=modality)
        def bowl_pos(obs_cache):
            return np.array(self.sim.data.body_xpos[self.bowl_body_id])

        for s in (block_pos, bowl_pos):
            observables[s.__name__] = Observable(name=s.__name__, sensor=s, sampling_rate=self.control_freq)
        return observables

    def _reset_internal(self):
        super()._reset_internal()
        if not self.deterministic_reset:
            for obj_pos, obj_quat, obj in self.placement_initializer.sample().values():
                self.sim.data.set_joint_qpos(obj.joints[0], np.concatenate([np.array(obj_pos), np.array(obj_quat)]))

    def reward(self, action=None):
        return float(self._check_success())

    # ------------------------------------------------------------- oracle
    def _check_success(self):
        """Oracle predicate (privileged): block centre inside the bowl footprint and below the rim, gripper open."""
        b = self.sim.data.body_xpos[self.block_body_id]
        w = self.sim.data.body_xpos[self.bowl_body_id]
        inside_xy = abs(b[0] - w[0]) < BOWL_SIZE[0] / 2 - 0.015 and abs(b[1] - w[1]) < BOWL_SIZE[1] / 2 - 0.015
        low = b[2] < w[2] + BOWL_SIZE[2] + 0.01
        return bool(inside_xy and low)
