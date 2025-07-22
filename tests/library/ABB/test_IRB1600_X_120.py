import numpy as np
from pathlib import Path
import yourdfpy
import pytest

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/IRB1600_X-120_v1/IRB1600_X-120.urdf"
urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)

def _test_fk_configuration(joint_angles_degrees, expected_flange_xyz):
    """Helper function to test forward kinematics for a given configuration."""
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


# Test data: (joint_angles_degrees, expected_flange_xyz)
fk_test_cases = [
    (np.array([0, 0, 0, 0, 0, 0]), np.array([0.750, 0.0, 0.962])),
    (np.array([0, 0, -90, 0, 0, 0]), np.array([0.150, 0.0, 1.562])),
    (np.array([0, 0, 55, 0, 0, 0]), np.array([0.494, 0.0, 0.470])),
    (np.array([0, 90, -90, 0, 0, 0]), np.array([1.225, 0.0, 0.487])),
    (np.array([0, 136, -90, 0, 0, 0]), np.array([0.897, 0.0, -0.287])),
    (np.array([0, 136, -235, 0, 0, 0]), np.array([0.386, 0.0, 0.737])),
    (np.array([0, -63, 55, 0, 0, 0]), np.array([0.321, 0.0, 0.786])),
    (np.array([0, -63, -90, 0, 0, 0]), np.array([-0.808, 0.0, 0.975])),
]


@pytest.mark.parametrize("joint_angles_degrees,expected_flange_xyz", fk_test_cases)
def test_fk_parametrized(joint_angles_degrees, expected_flange_xyz):
    """Test forward kinematics for various robot configurations."""
    _test_fk_configuration(joint_angles_degrees, expected_flange_xyz)
