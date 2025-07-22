import numpy as np
from pathlib import Path
import yourdfpy
import pytest

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/IRB1200H_7_70_STD_v1/IRB1200H_7_70_STD.urdf"
urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)


def _test_fk_configuration(joint_angles_degrees, expected_flange_xyz):
    """Helper function to test forward kinematics for a given configuration."""
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="link_5", frame_from="base_link"
    )[:3, 3]
    assert np.allclose(expected_flange_xyz, result_flange_xyz, atol=0.01), (
        f"{expected_flange_xyz} {result_flange_xyz}"
    )
    # errors = expected_flange_xyz - result_flange_xyz
    # assert np.sum(np.abs(errors)) < 0.01, (
    #     f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    # )


# Test data: (joint_angles_degrees, expected_flange_xyz)
fk_test_cases = [
    ([0, 0, 0, 0, 0, 0], [0.351, 0, 0.791]),
    ([0, 0, -83, 0, 0, 0], [0, 0, 1.102]),
    # ([0, 0, 70, 0, 0, 0], [160, 0, 424]),
    ([0, 90, -83, 0, 0, 0], [0.703, 0, 0.398]),
    ([0, 135, -83, 0, 0, 0], [0.497, 0, -0.099]),
    ([0, -100, -200, 0, 0, 0], [-0.133, 0, 0.055]),
    # ([0, -100, 70, 0, 0, 0], [-0.62, 0, 0.550]),
    ([0, -90, -83, 0, 0, 0], [-0.703, 0, 0.400]),
    ([0, -100, -83, 0, 0, 0], [-0.693, 0, 0.278]),
    ([0, 135, -200, 0, 0, 0], [0.358, 0, 0.488]),
]


@pytest.mark.parametrize("joint_angles_degrees,expected_flange_xyz", fk_test_cases)
def test_fk_parametrized(joint_angles_degrees, expected_flange_xyz):
    """Test forward kinematics for various robot configurations."""
    _test_fk_configuration(joint_angles_degrees, expected_flange_xyz)
