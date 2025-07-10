import argparse
from pathlib import Path
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("urdf_path", type=Path)

args = parser.parse_args()

urdf_path: Path = args.urdf_path.resolve()
assert urdf_path.exists()

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation

world = World()
world.scene.add_default_ground_plane()  # type: ignore

usd_path = urdf_path.parent / urdf_path.stem / f"{urdf_path.stem}.usd"
assert usd_path.exists()

robot_prim_path = "/World/robot"
add_reference_to_stage(str(usd_path), robot_prim_path)

articulation = SingleArticulation(prim_path=robot_prim_path)

world.reset()
articulation.initialize()
i = 0
slowdown_factor = 30
while True:
    world.step(render=True)

    ndof = len(articulation.get_joint_positions())
    joints = [0] * ndof
    joints[0] = np.sin(i / slowdown_factor)
    if len(joints) >= 2:
        joints[1] = np.sin(i / slowdown_factor) * 0.5
    if len(joints) >= 3:
        joints[2] = np.sin(i / slowdown_factor) * 0.5
    if len(joints) >= 4:
        joints[3] = np.sin(i / slowdown_factor) * 0.7
    if len(joints) >= 5:
        joints[4] = -np.sin(i / slowdown_factor) * 0.7
    if len(joints) >= 6:
        joints[5] = np.sin(i / slowdown_factor)

    articulation.set_joint_positions(positions=np.array(joints))
    i += 1
