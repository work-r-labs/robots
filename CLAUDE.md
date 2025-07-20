# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a repository of ABB robot models providing plug-and-play USD and URDF assets for use in IsaacSim and other robotics applications. The repository contains 32+ ABB robot models including cobots, industrial robots, SCARA robots, palletizing robots, paint robots, and positioners.

## Key Directory Structure

- `library/` - Reeady to use robot assets (URDF, USD, meshes, limits.xml)
- `sources/` - Source ROS packages with original robot descriptions
- `scripts/` - Demo scripts for IsaacSim integration
- `tools/` - Validation and utility scripts
- `isaacsim_typings/` - Type stubs for IsaacSim (git submodule)
- `dev_utils/` - Development utilities for scene generation
- `docs/` - various docs about the project and robot information from the manufacturer
- `tests/` - test suite for ensuring FK matches manuals

## Common Development Commands

### Environment Setup
```bash
# Clone with submodules (required for IsaacSim typings)
git clone --recurse-submodules https://github.com/work-r-labs/robots.git

# Create Python environment
uv venv
uv pip install -r requirements.txt
```

### Unit Tests

```bash
uv run pytest
```

### URDF Validation
```bash
# Validate a single URDF
uv run tools/validate_urdf.py path/to/robot.urdf

# Validate with verbose output
uv run tools/validate_urdf.py -v path/to/robot.urdf

# Validate all URDFs in repository
bash tools/validate_all_urdfs.sh
```

### Code Formatting
```bash
# Format Python code
uv run ruff format
```

### Running IsaacSim Demos
```bash
# Basic hello world demo
~/isaacsim/python.sh scripts/hello_world.py library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152.urdf

# Interactive inverse kinematics demo (requires PyRoKi)
~/isaacsim/python.sh -m pip install git+https://github.com/chungmin99/pyroki
~/isaacsim/python.sh scripts/ikdemo.py library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152.urdf
```

## Architecture

### Robot Asset Structure
Each robot model follows this structure:
```
library/ABB/RobotName_v1/
├── RobotName.urdf           # URDF file
├── RobotName/               # USD directory
│   └── RobotName.usd        # USD file
├── meshes/                  # STL mesh files
│   ├── base_link.stl
│   └── link_*.stl
└── limits.xml               # Joint limits (if available)
```

### IsaacSim Integration
- Robot models are designed for IsaacSim with proper USD conversion
- Scripts use `SingleArticulation` for robot control
- Inverse kinematics integration through PyRoKi library
- Spatial transformation utilities in `spatial_utils.py`

### Source to Generated Workflow
- `sources/` contains original ROS packages from ABB
- `library/` contains processed assets ready for use
- Use git status to see deleted files from `sources/` that were processed

## Development Notes

### Working with Robot Models
- Always test new robot models with the validation script
- URDF files should be paired with corresponding USD files
- Mesh files must be in `meshes/` subdirectory relative to URDF
- Joint limits should be properly defined for articulated robots

### IsaacSim Scripts
- Use `~/isaacsim/python.sh` to run scripts with IsaacSim Python
- Import IsaacSim modules after creating SimulationApp
- Use `SingleArticulation` for robot control
- Always call `world.reset()` and `articulation.initialize()` before simulation

### Type Checking
- IsaacSim type stubs are available in `isaacsim_typings/` submodule
- Use `typings` symlink for IDE support
- Python environment requires `yourdfpy` and `ruff` packages

## Important Files

- `tools/validate_all_urdfs.sh` - Validates all URDF files in repository
- `tools/validate_urdf.py` - URDF validation tool with detailed checks
- `scripts/_ik_demo_utils.py` - IK solving utilities using PyRoKi
- `ruff.toml` - Code formatting configuration
- `.claude/commands/update-info-table.md` - Command to update README robot table