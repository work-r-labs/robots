import numpy as np
from scipy.spatial.transform import Rotation as R


def tx(x: float | int) -> np.ndarray:
    """
    Create a homogeneous transformation matrix that translates by x in the x-axis.
    """
    return np.array(
        [
            [1, 0, 0, x],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )


def ty(y: float | int) -> np.ndarray:
    """
    Create a homogeneous transformation matrix that translates by y in the y-axis.
    """
    return np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, y],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )


def tz(z: float | int) -> np.ndarray:
    """
    Create a homogeneous transformation matrix that translates by z in the z direction.
    """
    return np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, z],
            [0, 0, 0, 1],
        ]
    )


def txyz(x, y, z) -> np.ndarray:
    return tx(x) @ ty(y) @ tz(z)


def rx_deg(theta) -> np.ndarray:
    """
    Create a homogeneous transformation matrix for rotation around the x-axis.
    """
    r = R.from_euler("x", theta, degrees=True).as_matrix()
    m = np.eye(4)
    m[:3, :3] = r
    return m


def ry_deg(theta) -> np.ndarray:
    """
    Create a homogeneous transformation matrix for rotation around the y-axis.
    """
    r = R.from_euler("y", theta, degrees=True).as_matrix()
    m = np.eye(4)
    m[:3, :3] = r
    return m


def rz_deg(theta) -> np.ndarray:
    """
    Create a homogeneous transformation matrix for rotation around the z-axis.
    """
    r = R.from_euler("z", theta, degrees=True).as_matrix()
    m = np.eye(4)
    m[:3, :3] = r
    return m


def rxyz_deg(x, y, z) -> np.ndarray:
    return rz_deg(z) @ ry_deg(y) @ rx_deg(x)
