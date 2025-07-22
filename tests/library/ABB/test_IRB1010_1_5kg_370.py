import numpy as np
from pathlib import Path
import yourdfpy
import pytest

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370.urdf"
urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)


def _test_fk_configuration(joint_angles_degrees, expected_flange_xyz):
    """Helper function to test forward kinematics for a given configuration."""
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="link_5", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


# Test data: (joint_angles_degrees, expected_flange_xyz)
fk_test_cases = [
    (np.array([0, 0, 0, 0, 0, 0]), np.array([0.185, 0, 0.375])),           # pos0
    (np.array([0, 0, -90, 0, 0, 0]), np.array([0, 0, 0.560])),             # pos1
    (np.array([0, 0, 50, 0, 0, 0]), np.array([0.1189, 0, 0.2333])),        # pos2
    (np.array([0, 90, -90, 0, 0, 0]), np.array([0.370, 0, 0.190])),        # pos3
    (np.array([0, 125, -90, 0, 0, 0]), np.array([0.3031, 0, -0.0222])),    # pos4
    # (np.array([0, 125, -180, 0, 0, 0]), np.array([0.2705, 0, 0.2256])),    # pos5
    (np.array([0, -75, -180, 0, 0, 0]), np.array([-0.2266, 0, 0.0592])),   # pos6
    (np.array([0, -75, 50, 0, 0, 0]), np.array([-0.011, 0, 0.3161])),      # pos7
    (np.array([0, -75, -90, 0, 0, 0]), np.array([-0.3574, 0, 0.2858]))     # pos8
]


@pytest.mark.parametrize("joint_angles_degrees,expected_flange_xyz", fk_test_cases)
def test_fk_parametrized(joint_angles_degrees, expected_flange_xyz):
    """Test forward kinematics for various robot configurations."""
    _test_fk_configuration(joint_angles_degrees, expected_flange_xyz)
