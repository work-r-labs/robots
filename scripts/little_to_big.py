import math
import numpy as np
from pathlib import Path
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation, XFormPrim
from isaacsim.sensors.camera import Camera
from scipy.spatial.transform import Rotation as R

world = World()

project_root = Path(__file__).parent.parent


small = (
    project_root
    / "generated/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370/IRB1010_1_5kg_370.usd"
)
big = project_root / "generated/IRB8700_800_350_v1/IRB8700_800_350/IRB8700_800_350.usd"


world.scene.add_default_ground_plane()

camera_orientation_xyzw = R.from_euler("xyz", [0, 0, 270], degrees=True).as_quat()
camera_orientation_wxyz = [camera_orientation_xyzw[-1], *camera_orientation_xyzw[:-1]]
camera = Camera(
    "/World/cam",
    name="cam",
    resolution=(256, 256),
    position=[7, 0, 0.6],
    orientation=camera_orientation_wxyz,
)


def sanitize_name(name: str) -> str:
    return name.replace("-", "_")


def set_xform(prim_path, x, y, z, rot):
    xform = XFormPrim(prim_path)
    xform.set_local_poses(
        translations=np.array([list(map(float, [x, y, z]))]), orientations=rot
    )


def euler_xyz_deg_to_rot_wxyz(x, y, z):
    rot_xyzw = R.from_euler("xyz", [x, y, z], degrees=True).as_quat()
    rot_wxyz = list(map(float, [rot_xyzw[-1], *rot_xyzw[:-1]]))
    return [rot_wxyz]


big_prim_path = "/World/bigbot"
small_prim_path = "/World/smallbot"

add_reference_to_stage(str(big), big_prim_path)
add_reference_to_stage(str(small), small_prim_path)

set_xform(big_prim_path, 0, 2, 0, None)
set_xform(small_prim_path, 0, 0, 0, euler_xyz_deg_to_rot_wxyz(0, 0, -90))

bigbot = SingleArticulation(prim_path=big_prim_path)
smallbot = SingleArticulation(prim_path=small_prim_path)

robots = {"big": bigbot, "small": smallbot}

world.reset()
for robot in robots.values():
    robot.initialize()
camera.initialize()
i = 60 * 20
while True:
    world.step(render=True)
    for name, robot in robots.items():
        ndof = len(robot.get_joint_positions())
        joints = [0] * ndof
        joints[0] = np.sin(i / 50)
        joints[1] = -np.sin(i / 50)
        if len(joints) >= 3:
            joints[2] = np.sin(i / 50) * 0.5
        if len(joints) >= 4:
            joints[3] = np.sin(i / 50) * 0.7
        if len(joints) >= 5:
            joints[4] = np.sin(i / 50) * 0.7
        if len(joints) >= 6:
            joints[5] = np.sin(i / 50)

        robot.set_joint_positions(positions=np.array(joints))
    camera.set_world_pose(position=[0, i / 3, 0.6])
    i -= 1
