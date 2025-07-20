# import numpy as np
# from pathlib import Path
# import yourdfpy
# import pytest

# project_root = Path(__file__).parent.parent.parent.parent

# np.set_printoptions(suppress=True)

# urdf_path = project_root / "library/ABB/IRB1100_4kg_475_STD_v1/IRB1100_4kg_475_STD.urdf"
# urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)


# def _test_fk_configuration(joint_angles_degrees, expected_wrist_center_xyz):
#     """Helper function to test forward kinematics for a given configuration."""
#     urdf.update_cfg(np.deg2rad(joint_angles_degrees))
#     # Note: We're testing wrist center position, not flange position
#     # The wrist center is typically at the intersection of axes 4, 5, and 6
#     # You may need to adjust the frame name based on your URDF structure
#     result_wrist_xyz: np.ndarray = urdf.get_transform(
#         frame_to="flange", frame_from="base_link"
#     )[:3, 3]

#     # Convert to mm for comparison (assuming URDF uses meters)
#     result_wrist_xyz_mm = result_wrist_xyz * 1000

#     errors = expected_wrist_center_xyz - result_wrist_xyz_mm
#     assert np.sum(np.abs(errors)) < 1.0, (  # 1mm tolerance
#         f"Expected: {expected_wrist_center_xyz} mm, Got: {result_wrist_xyz_mm} mm, Errors: {errors} mm"
#     )


# # Test data: (joint_angles_degrees, expected_wrist_center_xyz_mm)
# # Based on the provided table with positions at wrist center
# # Joint angles: [axis1, axis2, axis3, axis4, axis5, axis6]
# # Note: axis1 (base rotation) is not specified in the table, assuming 0°
# # axes 4, 5, 6 are wrist axes - not specified in table, assuming 0°
# fk_test_cases = [
#     # pos0: axis2=0°, axis3=0°
#     (np.array([0, 0, 0, 0, 0, 0]), np.array([314, 0, 562])),

#     # pos1: axis2=0°, axis3=-87.7°
#     (np.array([0, 0, -87.7, 0, 0, 0]), np.array([0, 0, 802])),

#     # pos2: axis2=9.7°, axis3=55°
#     (np.array([0, 9.7, 55, 0, 0, 0]), np.array([53.8, 0, 327])),

#     # pos3: axis2=90°, axis3=-87.7°
#     (np.array([0, 90, -87.7, 0, 0, 0]), np.array([475, 0, 327])),

#     # pos4: axis2=113°, axis3=-87.7°
#     (np.array([0, 113, -87.7, 0, 0, 0]), np.array([437.4, 0, 141.3])),

#     # pos5: axis2=-26.4°, axis3=-205°
#     (np.array([0, -26.4, -205, 0, 0, 0]), np.array([-248.2, 0, 327])),

#     # pos6: axis2=-115°, axis3=55°
#     (np.array([0, -115, 55, 0, 0, 0]), np.array([-87.6, 0, 453.4])),

#     # pos7: axis2=-90°, axis3=-87.7°
#     (np.array([0, -90, -87.7, 0, 0, 0]), np.array([-475, 0, 327])),

#     # pos8: axis2=-115°, axis3=-87.7°
#     (np.array([0, -115, -87.7, 0, 0, 0]), np.array([-430.7, 0, 126.2])),

#     # pos9: axis2=113°, axis3=-205°
#     (np.array([0, 113, -205, 0, 0, 0]), np.array([188.4, 0, 488.6])),
# ]


# @pytest.mark.parametrize("joint_angles_degrees,expected_wrist_center_xyz_mm", fk_test_cases)
# def test_fk_wrist_center_parametrized(joint_angles_degrees, expected_wrist_center_xyz_mm):
#     """Test forward kinematics for various robot configurations at wrist center."""
#     _test_fk_configuration(joint_angles_degrees, expected_wrist_center_xyz_mm)
