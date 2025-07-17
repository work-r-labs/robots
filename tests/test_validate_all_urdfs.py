#!/usr/bin/env python3

import pytest
from pathlib import Path
import sys
import os

# Add project root to path to import the validation function
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tools.validate_urdf import validate_urdf


class TestValidateAllURDFs:
    """Test class that validates all URDF files in the library directory."""

    @classmethod
    def setup_class(cls):
        """Set up test class by finding all URDF files."""
        cls.library_path = project_root / "library"
        cls.urdf_files = list(cls.library_path.rglob("*.urdf"))

        # Ensure we found some URDF files
        if not cls.urdf_files:
            pytest.fail(f"No URDF files found in {cls.library_path}")

        print(f"\nFound {len(cls.urdf_files)} URDF files to validate")

    @pytest.mark.parametrize(
        "urdf_file",
        [
            pytest.param(f, id=f.name)
            for f in (project_root / "library").rglob("*.urdf")
        ],
    )
    def test_urdf_validation(self, urdf_file):
        """Test that each URDF file passes validation."""
        print(f"\nValidating: {urdf_file}")
        print("-" * 50)

        # Call the validation function
        is_valid = validate_urdf(urdf_file)

        # Assert that validation passed
        assert is_valid, f"URDF validation failed for {urdf_file}"
        print("✓ PASSED")

    def test_urdf_files_exist(self):
        """Test that we have URDF files to validate."""
        assert len(self.urdf_files) > 0, "No URDF files found in library directory"
        print(f"Found {len(self.urdf_files)} URDF files to validate")

    def test_all_urdfs_summary(self):
        """Test that provides a summary of all URDF validations."""
        total = len(self.urdf_files)
        passed = 0
        failed = 0
        failed_files = []

        print(f"\nRunning URDF validation on all files in library directory...")
        print("=" * 50)

        for urdf_file in self.urdf_files:
            try:
                if validate_urdf(urdf_file):
                    passed += 1
                else:
                    failed += 1
                    failed_files.append(urdf_file)
            except Exception as e:
                failed += 1
                failed_files.append(urdf_file)
                print(f"Exception during validation of {urdf_file}: {e}")

        print(f"\n{'=' * 50}")
        print("Validation Summary:")
        print(f"Total files: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print("=" * 50)

        if failed > 0:
            print(f"Failed files:")
            for failed_file in failed_files:
                print(f"  - {failed_file}")
            pytest.fail(f"{failed} out of {total} URDF files failed validation")
        else:
            print("All URDF files passed validation!")
