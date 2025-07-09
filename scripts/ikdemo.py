import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("urdf_path", type=Path)

args = parser.parse_args()

urdf_path: Path = args.urdf_path.resolve()
assert urdf_path.exists()

# pyroki code

import yourdfpy
import pyroki as pk
from _ik_demo_utils import solve_ik
import numpy as np
import jax.numpy as jnp
from jaxlie import SE3, SO3

np.set_printoptions(suppress=True, precision=4)

project_root = Path(__file__).parent.parent

# urdf_path = project_root / "generated/CRB15000_12kg_127_v1/CRB15000_12kg_127.urdf"
# assert urdf_path.exists()

urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)
robot = pk.Robot.from_urdf(urdf)


def ik(goal: SE3):
    solution = solve_ik(
        robot=robot,
        target_link_name="tool0",
        target_position=np.array(goal.wxyz_xyz[-3:]),
        target_wxyz=np.array(goal.wxyz_xyz[:4]),
    )
    return solution


# isaacsim code

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation
from isaacsim.core.api.objects import VisualCuboid
from pxr import UsdGeom
import spatial_utils as su

world = World()
world.scene.add_default_ground_plane()  # type: ignore

lead_cube_prim_path = "/World/lead_cube"
lead_cube = VisualCuboid(
    prim_path=lead_cube_prim_path,
    name="lead_cube",
    position=[0.0, 0.0, 2.0],
    size=0.08,
    color=np.array([1.0, 0.0, 1.0]),
)
world.scene.add(lead_cube)
lead_cube_xform = UsdGeom.Xformable(lead_cube.prim)

usd_path = urdf_path.parent / urdf_path.stem / f"{urdf_path.stem}.usd"
# usd_path = project_root / "generated/CRB15000_5kg_950_v1/CRB15000_5kg_950/CRB15000_5kg_950.usd"
assert usd_path.exists()
print(usd_path)
# assert False


robot_prim_path = "/World/robot"
add_reference_to_stage(str(usd_path), robot_prim_path)

articulation = SingleArticulation(prim_path=robot_prim_path)

world.reset()
articulation.initialize()
while True:
    world.step(render=True)

    lead_pose = np.array(lead_cube_xform.GetLocalTransformation()).T
    print(lead_pose)

    goal = SE3.from_matrix(lead_pose @ su.tz(-0.08))

    solution = ik(goal)

    articulation.set_joint_positions(positions=np.array(solution))
