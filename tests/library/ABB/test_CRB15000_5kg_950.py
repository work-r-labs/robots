import numpy as np
from pathlib import Path
import yourdfpy
import pytest

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/CRB15000_5kg_950_v1/CRB15000_5kg_950.urdf"
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
    (np.array([0, 0, 0, 0, 0, 0]), np.array([0.571, 0.0, 0.899])),
    (np.array([0, 0, -76.8, 0, 25.2, 0]), np.array([0.0, 0.0, 1.320])),
    (np.array([0, 90, -76.8, 0, 25.2, 0]), np.array([1.055, 0.0, 0.265])),
    (np.array([0, 180, -76.8, 0, 25.2, 0]), np.array([0.0, 0.0, -0.790])),
    (np.array([0, -90, -76.8, 0, 25.2, 0]), np.array([-1.055, 0.0, 0.265])),
    (np.array([0, 180, 13.2, 0, 25.2, 0]), np.array([-0.611, 0.0, -0.179])),
    (np.array([0, 180, 85, 0, 25.2, 0]), np.array([-0.191, 0.0, 0.401])),
    (np.array([0, 180, -166.8, 0, 25.2, 0]), np.array([0.611, 0.0, -0.179])),
    (np.array([0, 180, -225, 0, 25.2, 0]), np.array([0.323, 0.0, 0.340])),
]


@pytest.mark.parametrize("joint_angles_degrees,expected_flange_xyz", fk_test_cases)
def test_fk_parametrized(joint_angles_degrees, expected_flange_xyz):
    """Test forward kinematics for various robot configurations."""
    _test_fk_configuration(joint_angles_degrees, expected_flange_xyz)
