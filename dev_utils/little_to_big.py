import shutil
import math
import numpy as np
from pathlib import Path
from isaacsim import SimulationApp
import cv2

simulation_app = SimulationApp({"headless": False})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation, XFormPrim
from isaacsim.sensors.camera import Camera
from scipy.spatial.transform import Rotation as R


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


def interp_homogeneous_translation(
    H: np.ndarray, xyz: np.ndarray, nsteps: int
) -> np.ndarray:
    """
    Linearly interpolate the translation of a 4×4 homogeneous transform.

    Parameters
    ----------
    H : (4,4) ndarray
        Source homogeneous matrix.  Its upper-left 3×3 block (rotation) is kept
        fixed.
    xyz : (3,) array-like
        Target translation (x, y, z) in the same units/coordinate frame as `H`.
    nsteps : int
        Number of interpolation steps (≥ 2).  The first matrix equals `H`,
        the last one has translation `xyz`.

    Returns
    -------
    out : (nsteps, 4, 4) ndarray
        Sequence of homogeneous matrices with linearly blended translations.
    """
    if nsteps < 2:
        raise ValueError("nsteps must be ≥ 2")

    H = np.asarray(H, dtype=float)
    # r = H[:3, :3]                # fixed rotation
    t0 = H[:3, 3]  # start translation
    t1 = np.asarray(xyz, dtype=float)

    alphas = np.linspace(0.0, 1.0, nsteps)[:, None]  # (nsteps,1)
    ts = (1 - alphas) * t0 + alphas * t1  # (nsteps,3)

    out = np.repeat(H[None, :, :], nsteps, axis=0)  # copy H
    out[:, :3, 3] = ts  # overwrite translations
    return out


def interp_xyz(p0: np.ndarray, p1: np.ndarray, nsteps: int) -> np.ndarray:
    """
    Linear interpolation between two 3-D points.

    Parameters
    ----------
    p0 : (3,) array-like
        Start position (x, y, z).
    p1 : (3,) array-like
        End position (x, y, z).
    nsteps : int
        Number of points to return (≥ 2).

    Returns
    -------
    pts : (nsteps, 3) ndarray
        Rows are the linearly interpolated positions from p0 to p1,
        inclusive.
    """
    if nsteps < 2:
        raise ValueError("nsteps must be ≥ 2")

    p0 = np.asarray(p0, dtype=float)
    p1 = np.asarray(p1, dtype=float)
    alphas = np.linspace(0.0, 1.0, nsteps)[:, None]  # column vector
    pts = (1 - alphas) * p0 + alphas * p1  # broadcast blend
    return pts


import numpy as np


def pad_trajectory_edges(traj: np.ndarray, pad_len: int = 100) -> np.ndarray:
    """
    Pre-/post-pad a joint-angle trajectory by repeating its first and last
    configurations.

    Parameters
    ----------
    traj : np.ndarray (n_steps, dof)
        Each row = full joint-angle vector (radians, degrees, etc.—match your data).
    pad_len : int, default 100
        How many times to replicate the first row at the start *and*
        the last row at the end.

    Returns
    -------
    np.ndarray (n_steps + 2*pad_len, dof)
        Padded trajectory.
    """
    if traj.ndim != 2:
        raise ValueError("traj must be 2-D (n_steps, dof)")

    first_pad = np.repeat(traj[0:1], pad_len, axis=0)  # (pad_len, dof)
    last_pad = np.repeat(traj[-1:], pad_len, axis=0)  # (pad_len, dof)

    return np.vstack((first_pad, traj, last_pad))


world = World()

project_root = Path(__file__).parent.parent


small = (
    project_root
    / "generated/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370/IRB1010_1_5kg_370.usd"
)
big = project_root / "generated/IRB8700_800_350_v1/IRB8700_800_350/IRB8700_800_350.usd"


world.scene.add_default_ground_plane()

camera_traj = interp_xyz(np.array([2, 0, 0.25]), np.array([20, 2, 1.5]), 300)
camera_traj = pad_trajectory_edges(camera_traj, pad_len=200)

camera_orientation_xyzw = R.from_euler("xyz", [0, 0, 180], degrees=True).as_quat()
camera_orientation_wxyz = [camera_orientation_xyzw[-1], *camera_orientation_xyzw[:-1]]
camera = Camera(
    "/World/cam",
    name="cam",
    resolution=(1920, 1080),
    position=camera_traj[0],
    orientation=camera_orientation_wxyz,
)


big_prim_path = "/World/bigbot"
small_prim_path = "/World/smallbot"

add_reference_to_stage(str(big), big_prim_path)
add_reference_to_stage(str(small), small_prim_path)

set_xform(big_prim_path, 0, 2, 0, None)
set_xform(small_prim_path, 0, 0, 0, euler_xyz_deg_to_rot_wxyz(0, 0, -90))

bigbot = SingleArticulation(prim_path=big_prim_path)
smallbot = SingleArticulation(prim_path=small_prim_path)

robots = {"big": bigbot, "small": smallbot}

render_dir = project_root / "ignore_render"
if render_dir.exists():
    shutil.rmtree(render_dir)
render_dir.mkdir(exist_ok=False)

world.reset()
for robot in robots.values():
    robot.initialize()
camera.initialize()
i = 0
while True:
    i += 1
    world.step(render=True)
    for name, robot in robots.items():
        ndof = len(robot.get_joint_positions())
        joints = [0] * ndof
        joints[0] = np.sin(i / 50)
        joints[1] = -np.sin(i / 50) * 0.7
        if len(joints) >= 3:
            joints[2] = np.sin(i / 50) * 0.5
        if len(joints) >= 4:
            joints[3] = np.sin(i / 50) * 0.7
        if len(joints) >= 5:
            joints[4] = np.sin(i / 50) * 0.7
        if len(joints) >= 6:
            joints[5] = np.sin(i / 50)

        robot.set_joint_positions(positions=np.array(joints))

    if i >= len(camera_traj):
        i = 0
    new_pos = camera_traj[i]
    print(new_pos)
    camera.set_world_pose(position=new_pos)

    rgba = camera.get_current_frame()["rgba"][..., :-1][..., ::-1]
    cv2.imwrite(f"ignore_render/{i}.png", rgba)
