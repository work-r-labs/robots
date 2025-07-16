import numpy as np
from pathlib import Path
import yourdfpy

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/CRB15000_5kg_950_v1/CRB15000_5kg_950.urdf"
urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)


def test_fk_one():
    joint_angles_degrees = np.array([0, 0, 0, 0, 0, 0])
    expected_flange_xyz = np.array([0.571, 0.0, 0.899])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_two():
    joint_angles_degrees = np.array([0, 0, -76.8, 0, 25.2, 0])
    expected_flange_xyz = np.array([0.0, 0.0, 1.320])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_three():
    joint_angles_degrees = np.array([0, 90, -76.8, 0, 25.2, 0])
    expected_flange_xyz = np.array([1.055, 0.0, 0.265])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_four():
    joint_angles_degrees = np.array([0, 180, -76.8, 0, 25.2, 0])
    expected_flange_xyz = np.array([0.0, 0.0, -0.790])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_five():
    joint_angles_degrees = np.array([0, -90, -76.8, 0, 25.2, 0])
    expected_flange_xyz = np.array([-1.055, 0.0, 0.265])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_six():
    joint_angles_degrees = np.array([0, 180, 13.2, 0, 25.2, 0])
    expected_flange_xyz = np.array([-0.611, 0.0, -0.179])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_seven():
    joint_angles_degrees = np.array([0, 180, 85, 0, 25.2, 0])
    expected_flange_xyz = np.array([-0.191, 0.0, 0.401])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_eight():
    joint_angles_degrees = np.array([0, 180, -166.8, 0, 25.2, 0])
    expected_flange_xyz = np.array([0.611, 0.0, -0.179])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )


def test_fk_nine():
    joint_angles_degrees = np.array([0, 180, -225, 0, 25.2, 0])
    expected_flange_xyz = np.array([0.323, 0.0, 0.340])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xyz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3]
    errors = expected_flange_xyz - result_flange_xyz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xyz}-{result_flange_xyz}={errors}"
    )
