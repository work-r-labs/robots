import numpy as np
from pathlib import Path
import yourdfpy

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152.urdf"
urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)


def test_fk_pos0():
    joint_angles_degrees = np.array([0, 0, 0, 0, 0, 0])
    expected_flange_xyz = np.array([0.888, 0.0, 1.297])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_pos1():
    joint_angles_degrees = np.array([0, 0, -80.2, 0, 28.58, 0])
    expected_flange_xyz = np.array([0.150, 0.0, 1.8823])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_pos2():
    joint_angles_degrees = np.array([0, 90, -80.2, 0, 28.58, 0])
    expected_flange_xyz = np.array([1.6323, 0.0, 0.400])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_pos3():
    joint_angles_degrees = np.array([0, 180, -80.2, 0, 28.58, 0])
    expected_flange_xyz = np.array([0.150, 0.0, -1.0823])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_pos4():
    joint_angles_degrees = np.array([0, -90, -80.2, 0, 28.58, 0])
    expected_flange_xyz = np.array([-1.3323, 0.0, 0.400])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_pos5():
    joint_angles_degrees = np.array([0, 180, 9.8, 0, 28.58, 0])
    expected_flange_xyz = np.array([-0.6253, 0.0, -0.307])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


# commented out this one because the manual is missing information here!
# def test_fk_pos6():
#     joint_angles_degrees = np.array([0, 180, 85, 0, 0, 0])
#     expected_flange_xyz = np.array([-0.048, 0.0, 0.4426])
#     urdf.update_cfg(np.deg2rad(joint_angles_degrees))
#     result_flange_xyz: np.ndarray = urdf.get_transform(
#         frame_to="flange", frame_from="base_link"
#     )[:3, 3]
#     errors = expected_flange_xyz - result_flange_xyz
#     assert np.sum(np.abs(errors)) < 0.01, (
#         f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
#     )


def test_fk_pos7():
    joint_angles_degrees = np.array([0, 180, -170.2, 0, 28.58, 0])
    expected_flange_xyz = np.array([0.9253, 0.0, -0.307])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_pos8():
    joint_angles_degrees = np.array([0, 180, -225, 0, 28.58, 0])
    expected_flange_xyz = np.array([0.5969, 0.0, 0.3265])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )
