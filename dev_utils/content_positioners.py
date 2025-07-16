import shutil
import math
import numpy as np
from pathlib import Path
from isaacsim import SimulationApp
import cv2
import matplotlib.pyplot as plt

simulation_app = SimulationApp({"headless": False})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.utils.prims import delete_prim, set_prim_visibility, get_prim_at_path
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation, XFormPrim
from isaacsim.core.utils.types import ArticulationAction
from isaacsim.sensors.camera import Camera
from scipy.spatial.transform import Rotation as R

from pxr import UsdLux, Sdf

world = World()

project_root = Path(__file__).parent.parent

scene_usd_path = project_root / "dev_utils" / "positioner_scene.usd"
assert scene_usd_path.exists()

positioner_1_prim_path = "/World/Irbpd_600_D1200_L2000_IRC5_rev02_CAD"
positioner_2_prim_path = "/World/Irbpk_600_D1200_L1600_IRC5_rev02_CAD"
positioner_3_prim_path = "/World/Irbpb_250_D1000_IRC5_rev02_CAD"

trolley_prim_path = "/World/ElevRailTrolley_v2"
railbot_prim_path = "/World/ElevRailTrolley_v2/IRB5500_27"

scene_prim_path = "/World"

add_reference_to_stage(str(scene_usd_path), scene_prim_path)

camera = Camera(
    "/World/Camera",
    name="cam",
    resolution=(1920, 1080),
)

railbot = SingleArticulation(railbot_prim_path)

positioner_1 = SingleArticulation(positioner_1_prim_path)
positioner_2 = SingleArticulation(positioner_2_prim_path)
positioner_3 = SingleArticulation(positioner_3_prim_path)

trolley_xform = XFormPrim(trolley_prim_path)
trolley_pos = trolley_xform.get_local_poses()[0][0]

trolley_waypoints = [
    np.array([[5.0, 3.85, 4.0]]),
    np.array([[5.0, -1.41, 4.0]]),
    np.array([[5.0, -4.82, 4.0]]),
]

one_to_two = np.linspace(trolley_waypoints[0], trolley_waypoints[1], 20)
two_to_three = np.linspace(trolley_waypoints[1], trolley_waypoints[2], 20)
three_to_one = np.linspace(trolley_waypoints[2], trolley_waypoints[0], 15)


def spin(art: SingleArticulation, start, stop, step=14, rev=False):
    if rev:
        start, stop = stop, start
    for i in np.linspace(start, stop, step):
        art.set_joint_positions(np.deg2rad(np.array([[i]])), joint_indices=[0])
        update()


i = 0


def update():
    global i
    world.step(render=True)
    if i > 180:
        rgba = camera.get_current_frame()["rgba"][..., :-1][..., ::-1]
        cv2.imwrite(f"ignore_render/{i}.png", rgba)

        camera_xyz = camera.get_local_pose()[0]  # type: ignore
        camera.set_local_pose(
            translation=camera_xyz + np.array([-0.002, -0.001, 0.002]) * 8
        )
    i += 1


def bot_action():
    traj = np.linspace(0, 1, 10) / 3
    for i in range(len(traj)):
        act = traj[i]
        joints = np.array([act * 2, act, act, np.abs(act), act, act, act])
        railbot.set_joint_positions(joints[None])
        update()
    traj = np.linspace(1, -1, 15) / 3
    for i in range(len(traj)):
        act = traj[i]
        joints = np.array([act * 2, act, act, np.abs(act), act, act, act])
        railbot.set_joint_positions(joints[None])
        update()
    traj = np.linspace(-1, 0, 10) / 3
    for i in range(len(traj)):
        act = traj[i]
        joints = np.array([act * 2, act, act, np.abs(act), act, act, act])
        railbot.set_joint_positions(joints[None])
        update()


world.reset()
positioner_1.initialize()
positioner_2.initialize()
positioner_3.initialize()
railbot.initialize()
camera.initialize()
side = -1

render_dir = project_root / "ignore_render"
if render_dir.exists():
    shutil.rmtree(render_dir)
render_dir.mkdir(exist_ok=False)

for i in range(180):
    update()

while True:
    rev = side == -1
    # station 1
    bot_action()
    for step in one_to_two:
        world.step(render=True)
        trolley_xform.set_local_poses(translations=np.array(step))
        update()

    spin(positioner_1, 0, 180, rev=rev)

    # station 2
    bot_action()
    for step in two_to_three:
        world.step(render=True)
        trolley_xform.set_local_poses(translations=np.array(step))
        update()

    spin(positioner_2, 0, 180, rev=rev)

    # station 3
    bot_action()
    for step in three_to_one:
        world.step(render=True)
        trolley_xform.set_local_poses(translations=np.array(step))
        update()

    spin(positioner_3, 0, 180, rev=rev)

    side = 1 if side == -1 else -1
