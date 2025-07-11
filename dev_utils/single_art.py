import argparse
from pathlib import Path
import numpy as np

from isaacsim import SimulationApp

usd_path = Path("/home/chris/robots/dev_utils/new_assembly.usd")
assert usd_path.exists()

simulation_app = SimulationApp({
    "headless": False,
})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation

world = World()
world.scene.add_default_ground_plane()  # type: ignore

scene_prim_path = "/World"
add_reference_to_stage(str(usd_path), scene_prim_path)

robot_prim_path = f"{scene_prim_path}/IRB1100_4kg_475_STD"
articulation = SingleArticulation(prim_path=robot_prim_path)

world.reset()
articulation.initialize()
i = 0
while True:
    articulation.set_joint_velocities(np.array([np.sin(i/20)]))
    world.step(render=True)
    i += 1