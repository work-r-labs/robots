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
    # "generated/IRB5500-27_v1/IRB5500-27/IRB5500-27.usd",
    "generated/IRB5510-12_v1/IRB5510-12/IRB5510-12.usd",
    "generated/IRB6750S_185-390-LID_v1/IRB6750S_185-390-LID/IRB6750S_185-390-LID.usd",
    "generated/IRB8700_550-420-SW6_v1/IRB8700_550-420-SW6/IRB8700_550-420-SW6.usd",
    "generated/IRB8700_800_350_v1/IRB8700_800_350/IRB8700_800_350.usd",
    # "generated/IRB920_6kg_550_180_STD_v1/IRB920_6kg_550_180_STD/IRB920_6kg_550_180_STD.usd",
    "generated/Irbpa_250_D1000_IRC5_rev02_CAD_v1/Irbpa_250_D1000_IRC5_rev02_CAD/Irbpa_250_D1000_IRC5_rev02_CAD.usd",
    "generated/Irbpk_600_D1200_L1600_IRC5_rev02_CAD_v1/Irbpk_600_D1200_L1600_IRC5_rev02_CAD/Irbpk_600_D1200_L1600_IRC5_rev02_CAD.usd",
    "generated/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD_v1/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD.usd",
]
usd_paths = [project_root / p for p in usd_paths]


# world.scene.add_default_ground_plane()

camera_orientation_xyzw = R.from_euler("xyz", [0, 0, 270], degrees=True).as_quat()
camera_orientation_wxyz = [camera_orientation_xyzw[-1], *camera_orientation_xyzw[:-1]]
camera = Camera(
    "/World/cam",
    name="cam",
    resolution=(1920, 1080),
    position=[7, 0, 0.6],
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


spacing = 5  # m  – centre-to-centre distance between robots
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

    side = 1 if i % 2 == 0 else -1
    x = col * spacing + side + (side * i / 16)  # metres in X
    y = row * spacing + i  # metres in Y
    z = 0.0

    if side == -1:
        rot = None
    else:
        rot_xyzw = R.from_euler("xyz", [0, 0, 180], degrees=True).as_quat()
        rot_wxyz = list(map(float, [rot_xyzw[-1], *rot_xyzw[:-1]]))
        rot = [rot_wxyz]

    xform = XFormPrim(prim_path)
    xform.set_local_poses(
        translations=np.array([list(map(float, [x, y, z]))]), orientations=rot
    )

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
i = 60 * 15
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
    camera.set_world_pose(position=[0, i / 3, 0.6])
    rgba = camera.get_current_frame()["rgba"][..., :-1][..., ::-1]
    cv2.imwrite(f"ignore_render/{i}.png", rgba)
    i -= 1
    if i == -60:
        i = 60 * 14
        break
