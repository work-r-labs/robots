import argparse
from pathlib import Path
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--usd_path", type=Path, default=Path("/home/chris/robots/dev_utils/assembled_maybe.usd"), required=False)

args = parser.parse_args()

usd_path: Path = args.usd_path.resolve()
assert usd_path.exists()

from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": False,
    # "enable_extension": ["isaacsim.robot_setup.assembler"]
})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation

# I need to do this because enable_extension above didn't work and omni.kit.app extension manager doesn't work.
import sys
sys.path.append(str(Path.home() / "isaacsim/exts/isaacsim.robot_setup.assembler/isaacsim/robot_setup/assembler"))

from robot_assembler import RobotAssembler
# assert False

world = World()
world.scene.add_default_ground_plane()  # type: ignore

project_root = Path(__file__).parent.parent

robot_usd_path = project_root / "library/ABB/IRB1100_4kg_475_STD_v1/IRB1100_4kg_475_STD/IRB1100_4kg_475_STD.usd"
robot_prim_path = "/World/robot"
add_reference_to_stage(str(robot_usd_path), robot_prim_path)

eoat_usd_path = project_root / "dev_utils/eoat/eoat/eoat.usd"
eoat_prim_path = "/World/eoat"
add_reference_to_stage(str(eoat_usd_path), eoat_prim_path)

assembler = RobotAssembler()

r = assembler.assemble_articulations(
    base_robot_path=robot_prim_path,
    attach_robot_path=eoat_prim_path,
    base_robot_mount_frame="/World/robot/link_6",
    attach_robot_mount_frame= "/World/eoat/gripper_base_link",
    fixed_joint_offset= np.array([0., 0., 0.]),
    fixed_joint_orient= np.array([1, 0, 0, 0]),
    mask_all_collisions= True,
    single_robot=True
)

# articulation = SingleArticulation(prim_path=robot_prim_path)

world.reset()
# articulation.initialize()
i = 0
while True:
    # articulation.set_joint_velocities(np.array([np.sin(i/20)]))
    world.step(render=True)
    i += 1