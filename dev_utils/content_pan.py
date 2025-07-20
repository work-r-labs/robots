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
from isaacsim.sensors.camera import Camera
from scipy.spatial.transform import Rotation as R

from pxr import UsdLux, Sdf

world = World()

project_root = Path(__file__).parent.parent

robot_paths = [
    "library/ABB/IRB920_6kg_650_180_STD_v1/IRB920_6kg_650_180_STD/IRB920_6kg_650_180_STD.usd",
    "library/ABB/IRB920T_6kg_450_180_STD_v1/IRB920T_6kg_450_180_STD/IRB920T_6kg_450_180_STD.usd",
    "library/ABB/IRB930_12kg_1050_300_STD_v1/IRB930_12kg_1050_300_STD/IRB930_12kg_1050_300_STD.usd",
    "library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152/CRB15000_10kg_152.usd",
    "library/ABB/CRB15000_12kg_127_v1/CRB15000_12kg_127/CRB15000_12kg_127.usd",
    "library/ABB/CRB15000_5kg_950_v1/CRB15000_5kg_950/CRB15000_5kg_950.usd",
    "library/ABB/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370/IRB1010_1_5kg_370.usd",
    "library/ABB/IRB1100_4kg_475_STD_v1/IRB1100_4kg_475_STD/IRB1100_4kg_475_STD.usd",
    "library/ABB/IRB1100_4kg_580_STD_v1/IRB1100_4kg_580_STD/IRB1100_4kg_580_STD.usd",
    "library/ABB/IRB1200_5_90_STD_v1/IRB1200_5_90_STD/IRB1200_5_90_STD.usd",
    "library/ABB/IRB1200H_5_90_STD_v1/IRB1200H_5_90_STD/IRB1200H_5_90_STD.usd",
    "library/ABB/IRB1200H_7_70_STD_v1/IRB1200H_7_70_STD/IRB1200H_7_70_STD.usd",
    "library/ABB/IRB14000_Yumi_v1/IRB14000_Yumi/IRB14000_Yumi.usd",
    "library/ABB/IRB14050_SAYuMi_v1/IRB14050_SAYuMi/IRB14050_SAYuMi.usd",
    "library/ABB/IRB1520ID_4_150_v1/IRB1520ID_4_150/IRB1520ID_4_150.usd",
    "library/ABB/IRB1600_X-120_v1/IRB1600_X-120/IRB1600_X-120.usd",
    "library/ABB/IRB52_7-1_2-Short_v1/IRB52_7-1_2-Short/IRB52_7-1_2-Short.usd",
    "library/ABB/IRB52_7-1_45-Long_v1/IRB52_7-1_45-Long/IRB52_7-1_45-Long.usd",
    "library/ABB/IRB5500-22_v1/IRB5500-22/IRB5500-22.usd",
    "library/ABB/IRB5510-12_v1/IRB5510-12/IRB5510-12.usd",
    "library/ABB/IRB6750S_185-390-LID_v1/IRB6750S_185-390-LID/IRB6750S_185-390-LID.usd",
    "library/ABB/IRB8700_550-420-SW6_v1/IRB8700_550-420-SW6/IRB8700_550-420-SW6.usd",
    "library/ABB/IRB8700_800_350_v1/IRB8700_800_350/IRB8700_800_350.usd",
]

positioner_paths = [
    "library/ABB/Irbpa_250_D1000_IRC5_rev02_CAD_v1/Irbpa_250_D1000_IRC5_rev02_CAD/Irbpa_250_D1000_IRC5_rev02_CAD.usd",
    "library/ABB/Irbpk_600_D1200_L1600_IRC5_rev02_CAD_v1/Irbpk_600_D1200_L1600_IRC5_rev02_CAD/Irbpk_600_D1200_L1600_IRC5_rev02_CAD.usd",
    "library/ABB/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD_v1/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD.usd",
    "library/ABB/Irbpa_500_D1000_H700_IRC5_rev02_CAD_v1/Irbpa_500_D1000_H700_IRC5_rev02_CAD/Irbpa_500_D1000_H700_IRC5_rev02_CAD.usd",
    "library/ABB/Irbpb_250_D1000_IRC5_rev02_CAD_v1/Irbpb_250_D1000_IRC5_rev02_CAD/Irbpb_250_D1000_IRC5_rev02_CAD.usd",
    "library/ABB/Irbpb_500_D1450_v1/Irbpb_500_D1450/Irbpb_500_D1450.usd",
    "library/ABB/Irbpc_1000_v1/Irbpc_1000/Irbpc_1000.usd",
    "library/ABB/Irbpc_500_IRC5_rev02_CAD_v1/Irbpc_500_IRC5_rev02_CAD/Irbpc_500_IRC5_rev02_CAD.usd",
    "library/ABB/Irbpd_600_D1000_L1600_IRC5_rev02_CAD_v1/Irbpd_600_D1000_L1600_IRC5_rev02_CAD/Irbpd_600_D1000_L1600_IRC5_rev02_CAD.usd",
    "library/ABB/Irbpl_1000_L1250_v1/Irbpl_1000_L1250/Irbpl_1000_L1250.usd",
    "library/ABB/Irbpl_5000_v1/Irbpl_5000/Irbpl_5000.usd",
    "library/ABB/Irbpr_300_D1000_L1250_v1/Irbpr_300_D1000_L1250/Irbpr_300_D1000_L1250.usd",
]

# Alternate between robots and positioners
usd_paths = []
max_len = max(len(robot_paths), len(positioner_paths))
for i in range(max_len):
    # if i < len(robot_paths):
    #     usd_paths.append(robot_paths[i])
    if i < len(positioner_paths):
        usd_paths.append(positioner_paths[i])
usd_paths = [project_root / p for p in usd_paths]


# world.scene.add_default_ground_plane()

camera_orientation_xyzw = R.from_euler("xyz", [0, 0, 270], degrees=True).as_quat()
camera_orientation_wxyz = [camera_orientation_xyzw[-1], *camera_orientation_xyzw[:-1]]
camera = Camera(
    "/World/cam",
    name="cam",
    resolution=(1920, 1080),
    position=[8, 0, 0.9],
    orientation=camera_orientation_wxyz,
)

# dome_light = UsdLux.DomeLight.Define(world.stage, "/World/Lights/DomeLight")
# dome_light.GetIntensityAttr().Set(1000)

# distantLight: UsdLux.CylinderLight = UsdLux.CylinderLight.Define(world.stage, Sdf.Path("/DistantLight"))

# distantLight.AddTranslateOp()
# distantLight.CreateLengthAttr(100)
# distantLight.CreateRadiusAttr(10)
# distantLight.CreateIntensityAttr(500)


def sanitize_name(name: str) -> str:
    return name.replace("-", "_")


def set_xform(prim_path, x, y, z, rot=None):
    xform = XFormPrim(prim_path)
    xform.set_world_poses(
        positions=np.array([list(map(float, [x, y, z]))]), orientations=rot
    )


spacing = 4  # m  – centre-to-centre distance between robots
robots: dict[str, SingleArticulation] = {}
for i, usd_path in enumerate(usd_paths):
    print(f"Loading {usd_path}")
    prim_path = sanitize_name(f"/World/robots/{usd_path.stem}")
    add_reference_to_stage(str(usd_path), prim_path)

    x = i * spacing
    y = 0
    z = 0

    xform = XFormPrim(prim_path)
    xform.set_local_poses(translations=np.array([list(map(float, [x, y, z]))]))

    robot = SingleArticulation(prim_path=prim_path)
    robots[prim_path] = robot

# init
n_tiles = 3
tile_halfsize = 50
for ix in range(-n_tiles, n_tiles + 1):
    for iy in range(-n_tiles, n_tiles + 1):
        prim_path = f"/World/groundplane/tile_{ix}_{iy}".replace("-", "neg")
        name = prim_path.split("/")[-1]
        print(f"{prim_path=} {name=}")
        world.scene.add_default_ground_plane(prim_path=prim_path, name=name)  # type: ignore
        light_prim_path = f"{prim_path}/SphereLight"
        # delete_prim(light_prim_path)
        light_prim = get_prim_at_path(light_prim_path)
        set_prim_visibility(light_prim, False)

world.reset()

step = 2 * tile_halfsize
for ix in range(-n_tiles, n_tiles + 1):
    for iy in range(-n_tiles, n_tiles + 1):
        prim_path = f"/World/groundplane/tile_{ix}_{iy}".replace("-", "neg")
        set_xform(prim_path, ix * step, iy * step, 0)
for robot in robots.values():
    robot.initialize()
camera.initialize()

render_dir = project_root / "ignore_render"
if render_dir.exists():
    shutil.rmtree(render_dir)
render_dir.mkdir(exist_ok=False)

# run
i = -400
while True:
    world.step(render=True)
    for name, robot in robots.items():
        ndof = len(robot.get_joint_positions())
        joints = [0] * ndof
        joints[0] = np.sin(i / 20)
        if len(joints) >= 2:
            joints[1] = np.sin(i / 20) * 0.5
        if len(joints) >= 3:
            joints[2] = np.sin(i / 20) * 0.5
        if len(joints) >= 4:
            joints[3] = np.sin(i / 20) * 0.7
        if len(joints) >= 5:
            joints[4] = np.sin(i / 20) * 0.7
        if len(joints) >= 6:
            joints[5] = np.sin(i / 20)

        robot.set_joint_positions(positions=np.array(joints))
    speed_div = 8
    camera.set_world_pose(
        position=[
            i / speed_div,
            12 + (i / speed_div / 140) * 4,
            0.8 + (i / speed_div / 140) * 1.5,
        ]
    )
    rgba = camera.get_current_frame()["rgba"][..., :-1][..., ::-1]
    cv2.imwrite(f"ignore_render/{i}.png", rgba)
    i += 1
    if i / speed_div > 140:
        i = -100
