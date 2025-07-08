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


import spatial_utils as su


world = World()

project_root = Path(__file__).parent.parent

camera_orientation_xyzw = R.from_euler("xyz", [0, 0, 270], degrees=True).as_quat()
camera_orientation_wxyz = [camera_orientation_xyzw[-1], *camera_orientation_xyzw[:-1]]
camera = Camera(
    "/World/cam",
    name="cam",
    # resolution=(1920, 1080),
    resolution=(256, 256),
    position=[0, 0, 2],
    orientation=camera_orientation_wxyz,
)


def set_camera_pose(pose: np.ndarray):
    assert pose.shape == (4, 4)
    t = pose[:3, 3]
    R.from_matr

    camera.set_world_pose(position)


world.reset()
camera.initialize()
while True:
    world.step(render=True)
