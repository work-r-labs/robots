import numpy as np
from pathlib import Path
import yourdfpy

project_root = Path(__file__).parent.parent.parent.parent

np.set_printoptions(suppress=True)

urdf_path = project_root / "library/ABB/CRB15000_12kg_127_v1/CRB15000_12kg_127.urdf"
urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)


def test_fk_pos0():
    joint_angles_degrees = np.array([0, 0, 0, 0, 0, 0])
    expected_flange_xz = np.array([0.635, 1.235])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )


def test_fk_pos1():
    joint_angles_degrees = np.array([0, 0, -78.4, 0, 26.7, 0])
    expected_flange_xz = np.array([0.0, 1.719])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )


def test_fk_pos2():
    joint_angles_degrees = np.array([90, 0, -78.4, 0, 26.7, 0])
    expected_flange_xz = np.array([1.381, 0.338])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )


def test_fk_pos3():
    joint_angles_degrees = np.array([180, 0, -78.4, 0, 26.7, 0])
    expected_flange_xz = np.array([0.0, -1.043])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )


def test_fk_pos4():
    joint_angles_degrees = np.array([-90, 0, -78.4, 0, 26.7, 0])
    expected_flange_xz = np.array([-1.381, 0.338])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )


def test_fk_pos5():
    joint_angles_degrees = np.array([180, 0, 11.6, 0, 26.7, 0])
    expected_flange_xz = np.array([-0.674, -0.369])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )


def test_fk_pos6():
    joint_angles_degrees = np.array([180, 0, 85, 0, 26.7, 0])
    expected_flange_xz = np.array([-0.193, 0.2768])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )


def test_fk_pos7():
    joint_angles_degrees = np.array([180, 0, -168.4, 0, 26.7, 0])
    expected_flange_xz = np.array([0.674, -0.369])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )


def test_fk_pos8():
    joint_angles_degrees = np.array([180, 0, -225, 0, 26.7, 0])
    expected_flange_xz = np.array([0.3706, 0.194])
    urdf.update_cfg(np.deg2rad(joint_angles_degrees))
    result_flange_xz: np.ndarray = urdf.get_transform(
        frame_to="flange", frame_from="base_link"
    )[:3, 3][[0, 2]]
    errors = expected_flange_xz - result_flange_xz
    assert np.sum(np.abs(errors)) < 0.01, (
        f"{expected_flange_xz}-{result_flange_xz}={errors}"
    )