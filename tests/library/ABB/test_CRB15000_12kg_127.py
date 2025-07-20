import numpy as np
from pathlib import Path
import yourdfpy
import pytest

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/CRB15000_12kg_127_v1/CRB15000_12kg_127.urdf"
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
    (np.array([0, 0, 0, 0, 0, 0]), np.array([0.635, 0.0, 1.235])),
    (np.array([0, 0, -78.4, 0, 26.7, 0]), np.array([0.0, 0.0, 1.719])),
    (np.array([0, 90, -78.4, 0, 26.7, 0]), np.array([1.381, 0.0, 0.338])),
    (np.array([0, 180, -78.4, 0, 26.7, 0]), np.array([0.0, 0.0, -1.043])),
    (np.array([0, -90, -78.4, 0, 26.7, 0]), np.array([-1.381, 0.0, 0.338])),
    (np.array([0, 180, 11.6, 0, 26.7, 0]), np.array([-0.674, 0.0, -0.369])),
    (np.array([0, 180, 85, 0, 26.7, 0]), np.array([-0.193, 0.0, 0.2768])),
    (np.array([0, 180, -168.4, 0, 26.7, 0]), np.array([0.674, 0.0, -0.369])),
    (np.array([0, 180, -225, 0, 26.7, 0]), np.array([0.3706, 0.0, 0.194])),
]


@pytest.mark.parametrize("joint_angles_degrees,expected_flange_xyz", fk_test_cases)
def test_fk_parametrized(joint_angles_degrees, expected_flange_xyz):
    """Test forward kinematics for various robot configurations."""
    _test_fk_configuration(joint_angles_degrees, expected_flange_xyz)
