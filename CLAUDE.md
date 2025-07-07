# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains a collection of ABB industrial robot models in URDF format for use with ROS and Isaac Sim. The main structure includes:

- `ABB/` - Contains URDF robot descriptions for various ABB robot models
- `generated/` - Contains converted USD format files for Isaac Sim
- `scripts/` - Contains utility scripts for viewing and working with robot models

## Robot Model Structure

Each robot model follows the ROS package structure:
- `<robot_name>_description/` - ROS package containing the robot description
  - `urdf/` - URDF files (.urdf, .xacro, .gazebo, .trans)
  - `meshes/` - STL mesh files for visual and collision geometry
  - `launch/` - Launch files for controllers, display, and simulation
  - `package.xml` - ROS package manifest
  - `CMakeLists.txt` - Build configuration

## Common Commands

### Viewing robots in Isaac Sim
```bash
# Run the visualization script
python scripts/view.py
```

## Key Files

- `scripts/view.py` - Isaac Sim visualization script that loads multiple robot models
- `README.md` - Contains link to ABB robot models spreadsheet
- `README.md` - Contains table of supported robots and links to their URDF and USD files inside the repo

## Working with Robot Models

When working with robot models in this repository:

1. **URDF Files**: The main robot descriptions are in URDF/XACRO format located in each robot's `urdf/` directory
2. **Mesh Files**: All visual and collision meshes are STL files in the `meshes/` directory
3. **Generated USD**: Isaac Sim compatible USD files are generated in the `generated/` directory
4. **Material Definitions**: Each robot has a `materials.xacro` file defining visual materials

## Converting Process

The conversion process uses Claude Code to process URDF files with the `/prepare-for-isaacsim $INPUT_FILE` prompt which prepares
the input XACRO/URDF file for importing into IsaacSim. This makes sure expansions/naming/filepaths are all correct.
The processed URDF file is then manually imported into IsaacSim where a USD file is created.

## Isaac Sim Integration

The `scripts/view.py` script demonstrates how to:
- Load multiple robot models in Isaac Sim
- Position them in a scene
- Set up basic simulation environment
