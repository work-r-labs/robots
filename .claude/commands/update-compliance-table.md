Update @robot_compliance_status.md so that it reflects all the robots available in @library/ .

Use the following format:

## Compliance Criteria

For a robot to be considered "fully compliant", it must have:
- ✅ URDF file with correct naming convention
- ✅ USD directory and file structure
- ✅ Meshes directory with STL files
- ✅ limits.xml file for joint limits
- ✅ USD configuration files

## Legend

- ✅ = Present and correct
- ❌ = Missing
- ⚠️ = Present but problematic
- ⚡ = Forward kinematics tests available
- Numbers in parentheses = Count of mesh files

**Test Coverage Types:**
- ✅ All robots: URDF validation tests
- ⚡ Select robots: Forward kinematics (FK) tests

## Robot Status Table

| Robot Model | URDF | USD | Meshes | Limits | Config | Tests | Status | Priority |
|-------------|------|-----|--------|--------|--------|-------|---------|----------|

Include a line at the end about when this command was last run.