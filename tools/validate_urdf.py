#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
import yourdfpy

# Get project root
project_root = Path(__file__).parent.parent


def validate_urdf(urdf_path: Path) -> bool:
    """Validate a URDF file and return True if valid, False otherwise."""
    errors = []
    warnings = []

    # Check if file exists
    if not urdf_path.exists():
        print(f"❌ Error: URDF file not found: {urdf_path}")
        return False

    print(f"📄 Validating URDF: {urdf_path}")

    try:
        # Load URDF
        urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)
        robot = urdf.robot
        print(f"✅ Successfully loaded URDF")

        # Validate robot structure
        if not robot.links:
            errors.append("No links found in robot")

        if not robot.joints:
            warnings.append("No joints found in robot (static robot)")

        # Check for base link
        base_links = [
            link
            for link in robot.links
            if not any(joint.child == link.name for joint in robot.joints)
        ]
        if len(base_links) == 0:
            errors.append("No base link found (circular dependency)")
        elif len(base_links) > 1:
            warnings.append(
                f"Multiple potential base links: {[link.name for link in base_links]}"
            )

        # Validate joints
        joint_issues = []
        for joint in robot.joints:
            # Check parent/child links exist
            parent_exists = any(link.name == joint.parent for link in robot.links)
            child_exists = any(link.name == joint.child for link in robot.links)

            if not parent_exists:
                joint_issues.append(
                    f"Joint '{joint.name}' references non-existent parent link '{joint.parent}'"
                )
            if not child_exists:
                joint_issues.append(
                    f"Joint '{joint.name}' references non-existent child link '{joint.child}'"
                )

            # Check joint limits for revolute/prismatic joints
            if joint.type in ["revolute", "prismatic"]:
                if joint.limit is None:
                    warnings.append(
                        f"Joint '{joint.name}' ({joint.type}) has no limits defined"
                    )
                elif joint.limit.lower is None or joint.limit.upper is None:
                    warnings.append(
                        f"Joint '{joint.name}' has incomplete limit definition"
                    )

        errors.extend(joint_issues)

        # Check mesh files
        mesh_dir = urdf_path.parent / "meshes"
        missing_meshes = []

        for link in robot.links:
            if link.visuals:
                for visual in link.visuals:
                    if (
                        visual.geometry
                        and hasattr(visual.geometry, "mesh")
                        and visual.geometry.mesh
                        and hasattr(visual.geometry.mesh, "filename")
                    ):
                        mesh_filename = Path(visual.geometry.mesh.filename).name
                        mesh_path = mesh_dir / mesh_filename
                        if not mesh_path.exists():
                            missing_meshes.append(f"Visual mesh not found: {mesh_path}")

            if link.collisions:
                for collision in link.collisions:
                    if (
                        collision.geometry
                        and hasattr(collision.geometry, "mesh")
                        and collision.geometry.mesh
                        and hasattr(collision.geometry.mesh, "filename")
                    ):
                        mesh_filename = Path(collision.geometry.mesh.filename).name
                        mesh_path = mesh_dir / mesh_filename
                        if not mesh_path.exists():
                            missing_meshes.append(
                                f"Collision mesh not found: {mesh_path}"
                            )

        if missing_meshes:
            warnings.extend(missing_meshes)

        # Print summary
        print(f"\n📊 Validation Summary:")
        print(f"  Links: {len(robot.links)}")
        print(f"  Joints: {len(robot.joints)}")

        if warnings:
            print(f"\n⚠️  Warnings ({len(warnings)}):")
            for warning in warnings:
                print(f"  - {warning}")

        if errors:
            print(f"\n❌ Errors ({len(errors)}):")
            for error in errors:
                print(f"  - {error}")
            return False
        else:
            print(f"\n✅ URDF validation passed!")
            return True

    except Exception as e:
        print(f"❌ Error loading URDF: {e}")
        return False


def print_robot_info(urdf_path: Path):
    """Print detailed robot information."""
    try:
        urdf = yourdfpy.URDF.load(urdf_path, mesh_dir=urdf_path.parent)
        robot = urdf.robot

        print("\n🔗 Links:")
        for link in robot.links:
            print(f"  - {link.name}")

        print("\n⚙️  Joints:")
        for joint in robot.joints:
            limit_str = ""
            if joint.limit:
                if joint.limit.lower is not None and joint.limit.upper is not None:
                    limit_str += (
                        f" | limits: [{joint.limit.lower:.3f}, {joint.limit.upper:.3f}]"
                    )
                if joint.limit.velocity is not None:
                    limit_str += f" | velocity: {joint.limit.velocity:.3f}"
                if joint.limit.effort is not None:
                    limit_str += f" | effort: {joint.limit.effort:.3f}"
            print(
                f"  - {joint.name} ({joint.type}): {joint.parent} → {joint.child}{limit_str}"
            )

    except Exception as e:
        print(f"❌ Error printing robot info: {e}")


def main():
    parser = argparse.ArgumentParser(description="Validate URDF files for ABB robots")
    parser.add_argument("urdf_path", help="Path to URDF file")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Show detailed robot information"
    )

    args = parser.parse_args()

    urdf_path = Path(args.urdf_path)

    is_valid = validate_urdf(urdf_path)

    if args.verbose and is_valid:
        print_robot_info(urdf_path)

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
