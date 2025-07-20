import numpy as np
from pathlib import Path
import yourdfpy
import pytest

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152.urdf"
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
    (np.array([0, 0, 0, 0, 0, 0]), np.array([0.888, 0.0, 1.297])),
    (np.array([0, 0, -80.2, 0, 28.58, 0]), np.array([0.150, 0.0, 1.8823])),
    (np.array([0, 90, -80.2, 0, 28.58, 0]), np.array([1.6323, 0.0, 0.400])),
    (np.array([0, 180, -80.2, 0, 28.58, 0]), np.array([0.150, 0.0, -1.0823])),
    (np.array([0, -90, -80.2, 0, 28.58, 0]), np.array([-1.3323, 0.0, 0.400])),
    (np.array([0, 180, 9.8, 0, 28.58, 0]), np.array([-0.6253, 0.0, -0.307])),
    (np.array([0, 180, -170.2, 0, 28.58, 0]), np.array([0.9253, 0.0, -0.307])),
    (np.array([0, 180, -225, 0, 28.58, 0]), np.array([0.5969, 0.0, 0.3265])),
]


@pytest.mark.parametrize("joint_angles_degrees,expected_flange_xyz", fk_test_cases)
def test_fk_parametrized(joint_angles_degrees, expected_flange_xyz):
    """Test forward kinematics for various robot configurations."""
    _test_fk_configuration(joint_angles_degrees, expected_flange_xyz)
