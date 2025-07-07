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

usd_paths = [
    "generated/abb_irb920_v1/abb_irb920/abb_irb920.usd",
    "generated/CRB15000_10kg_152_v1/CRB15000_10kg_152/CRB15000_10kg_152.usd",
    "generated/CRB15000_12kg_127_v1/CRB15000_12kg_127/CRB15000_12kg_127.usd",
    "generated/CRB15000_5kg_950_v1/CRB15000_5kg_950/CRB15000_5kg_950.usd",
    "generated/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370/IRB1010_1_5kg_370.usd",
    "generated/IRB1100_4kg_475_STD_v1/IRB1100_4kg_475_STD/IRB1100_4kg_475_STD.usd",
    "generated/IRB1100_4kg_580_STD_v1/IRB1100_4kg_580_STD/IRB1100_4kg_580_STD.usd",
    "generated/IRB1200_5_90_STD_v1/IRB1200_5_90_STD/IRB1200_5_90_STD.usd",
    "generated/IRB1200H_5_90_STD_v1/IRB1200H_5_90_STD/IRB1200H_5_90_STD.usd",
    "generated/IRB1200H_7_70_STD_v1/IRB1200H_7_70_STD/IRB1200H_7_70_STD.usd",
    "generated/IRB1520ID_4_150_v1/IRB1520ID_4_150/IRB1520ID_4_150.usd",
    "generated/IRB1600_X-120_v1/IRB1600_X-120/IRB1600_X-120.usd",
    # "generated/IRB460_110-240_v1/IRB460_110-240/IRB460_110-240.usd",
    "generated/IRB52_7-1_2-Short_v1/IRB52_7-1_2-Short/IRB52_7-1_2-Short.usd",
    "generated/IRB52_7-1_45-Long_v1/IRB52_7-1_45-Long/IRB52_7-1_45-Long.usd",
    "generated/IRB5500-22_v1/IRB5500-22/IRB5500-22.usd",
    "generated/IRB5500-27_v1/IRB5500-27/IRB5500-27.usd",
    "generated/IRB5510-12_v1/IRB5510-12/IRB5510-12.usd",
    "generated/IRB6750S_185-390-LID_v1/IRB6750S_185-390-LID/IRB6750S_185-390-LID.usd",
    "generated/IRB8700_550-420-SW6_v1/IRB8700_550-420-SW6/IRB8700_550-420-SW6.usd",
    "generated/IRB8700_800_350_v1/IRB8700_800_350/IRB8700_800_350.usd",
    # "generated/IRB920_6kg_550_180_STD_v1/IRB920_6kg_550_180_STD/IRB920_6kg_550_180_STD.usd",
]
usd_paths = [project_root / p for p in usd_paths]


world.scene.add_default_ground_plane()

camera_orientation_xyzw = R.from_euler('xyz', [0, 0, 270], degrees=True).as_quat()
camera_orientation_wxyz = [camera_orientation_xyzw[-1], *camera_orientation_xyzw[:-1]]
camera = Camera(
    "/World/cam", name="cam", resolution=(256, 256), position=[7, 0, 0.6], orientation=camera_orientation_wxyz)


def sanitize_name(name: str) -> str:
    return name.replace("-", "_")


spacing = 4  # m  – centre-to-centre distance between robots
n = len(usd_paths)
side = math.ceil(math.sqrt(n))
robots: dict[str, SingleArticulation] = {}
for i, usd_path in enumerate(usd_paths):
    print(f"Loading {usd_path}")
    prim_path = sanitize_name(f"/World/robots/{usd_path.stem}")
    add_reference_to_stage(str(usd_path), prim_path)

    # row, col = divmod(i, side)  # integer grid coordinates
    row = i
    col = 0
    x = col * spacing + (1 if i%2==0 else -1) * i/4  # metres in X
    y = row * spacing + i  # metres in Y
    z = 0.0

    xform = XFormPrim(prim_path)
    xform.set_local_poses(
        translations=np.array([list(map(float, [x, y, z]))]),
    )

    robot = SingleArticulation(prim_path=prim_path)
    robots[prim_path] = robot

world.reset()
for robot in robots.values():
    robot.initialize()
camera.initialize()
i = -60*5
while True:
    world.step(render=True)
    for name, robot in robots.items():
        ndof = len(robot.get_joint_positions())
        joints = [0]*ndof
        joints[0] = np.sin(i/20)
        joints[1] = -np.sin(i/20)
        if len(joints) >= 3:
            joints[2] = np.sin(i/20) * 0.5
        if len(joints) >= 4:
            joints[3] = np.sin(i/20) * 0.7
        if len(joints) >= 5:
            joints[4] = np.sin(i/20) * 0.7
        if len(joints) >= 6:
            joints[5] = np.sin(i/20)

        robot.set_joint_positions(positions=np.array(joints))
    camera.set_world_pose(position=[0, i/5, 0.6])
    i += 1
