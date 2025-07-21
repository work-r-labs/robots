import numpy as np
from pathlib import Path
import yourdfpy
import pytest

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/IRB1200H_5_90_STD_v1/IRB1200H_5_90_STD.urdf"
urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)


def _test_fk_configuration(joint_angles_degrees, expected_flange_xyz):
    """Helper function to test forward kinematics for a given configuration."""
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="link_5", frame_from="base_link"
    )[:3, 3]
    assert np.allclose(expected_flange_xyz, result_flange_xyz, atol=0.001), (
        f"{expected_flange_xyz} {result_flange_xyz}"
    )
    # errors = expected_flange_xyz - result_flange_xyz
    # assert np.sum(np.abs(errors)) < 0.01, (
    #     f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    # )


# Test data: (joint_angles_degrees, expected_flange_xyz)
# Based on manual calculations from IRB1200_5_90_STD_CASES
fk_test_cases = [
    ([0, 0, 0, 0, 0, 0], [0.451, 0, 0.889]),
    # ([0, 0, -85, 0, 0, 0], [0, 0, 1.300]),
    ([0, 0, 70, 0, 0, 0], [0.194, 0, 0.438]),
    ([0, 90, -85, 0, 0, 0], [0.901, 0, 0.402]),
    ([0, 130, -85, 0, 0, 0], [0.692, 0, -0.178]),
    ([0, -100, -200, 0, 0, 0], [-0.179, 0, -0.048]),
    ([0, -100, 70, 0, 0, 0], [-0.072, 0, 0.583]),
    ([0, -90, -85, 0, 0, 0], [-0.901, 0, 0.397]),
    ([0, -100, -85, 0, 0, 0], [-0.887, 0, 0.240]),
    ([0, 130, -200, 0, 0, 0], [0.458, 0, 0.549]),
]


@pytest.mark.parametrize("joint_angles_degrees,expected_flange_xyz", fk_test_cases)
def test_fk_parametrized(joint_angles_degrees, expected_flange_xyz):
    """Test forward kinematics for various robot configurations."""
    _test_fk_configuration(joint_angles_degrees, expected_flange_xyz)
