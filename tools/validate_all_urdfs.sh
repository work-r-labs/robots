#!/bin/bash

# Script to validate all URDF files in the library directory
# Uses the URDF validation tool at tools/validate_urdf.py

set -e

echo "Running URDF validation on all files in library directory..."
echo "================================================="

# Counter for tracking results
total=0
passed=0
failed=0

# Find all URDF files in library directory
while IFS= read -r -d '' urdf_file; do
    total=$((total + 1))
    echo
    echo "Validating: $urdf_file"
    echo "-------------------------------------------------"
    
    if uv run tools/validate_urdf.py "$urdf_file"; then
        passed=$((passed + 1))
        echo "✓ PASSED"
    else
        failed=$((failed + 1))
        echo "✗ FAILED"
    fi
done < <(find library -name "*.urdf" -type f -print0)

echo
echo "================================================="
echo "Validation Summary:"
echo "Total files: $total"
echo "Passed: $passed"
echo "Failed: $failed"
echo "================================================="

if [ $failed -gt 0 ]; then
    exit 1
else
    echo "All URDF files passed validation!"
    exit 0
fi