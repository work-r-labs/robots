# URDF Conventions for 6-Axis Robots

This document summarizes the standard URDF format and conventions for 6-axis robots based on the robot models in the `library/` directory.

## Robot Structure

### Link Naming Convention
- **base_link**: The fixed base of the robot
- **link_1** to **link_6**: The six articulated links of the robot arm
- **flange**: End effector mounting point (fixed to link_6)
- **tool0**: Tool center point (fixed to flange)

### Joint Naming Convention
- **joint_1** to **joint_6**: The six revolute joints of the robot
- **joint_6-flange** or **joint_flange**: Fixed joint connecting link_6 to flange
- **flange-tool0** or **joint_tool0**: Fixed joint connecting flange to tool0

## Joint Configuration

### Standard 6-Axis Joint Layout
1. **joint_1**: Base rotation (Z-axis)
2. **joint_2**: Shoulder pitch (Y-axis)
3. **joint_3**: Elbow pitch (Y-axis)
4. **joint_4**: Wrist roll (X-axis)
5. **joint_5**: Wrist pitch (Y-axis)
6. **joint_6**: Wrist yaw (X-axis)

### Joint Properties
- **Type**: All main joints are `revolute`
- **Axis**: Standard axis directions following right-hand rule
- **Limits**: Include `lower`, `upper`, `effort`, and `velocity` attributes
- **Origin**: Transformation from parent to child link

## Link Properties

### Physical Properties
Each link includes:
- **Inertial**: Mass, center of mass, and inertia tensor
- **Visual**: STL mesh file reference with scaling
- **Collision**: Collision geometry (typically same as visual)

### Mesh File Convention
- **Location**: `meshes/` subdirectory relative to URDF
- **Naming**: `base_link.stl`, `link_1.stl`, ..., `link_6.stl`
- **Scale**: Typically `0.001 0.001 0.001` (mm to m conversion)

## Tool Frame Setup

### Flange Frame
- **Purpose**: Standard mounting point for end effectors
- **Transform**: Must be Z-out. Often includes a 90° rotation about Y-axis (`rpy="0 1.57 0"`)
- **Mass**: Minimal mass (0.01-0.1 kg)

### Tool0 Frame
- **Purpose**: Standard tool center point
- **Transform**: Usually identity transform from flange
- **Mass**: Minimal mass (0.01 kg)

## Common Patterns

### Coordinate Frame Conventions
- **Base**: Robot base is at origin
- **Z-up**: Positive Z-axis points upward

### File Structure
```
RobotName_v1/
├── RobotName.urdf
├── RobotName/
│   └── RobotName.usd
├── meshes/
│   ├── base_link.stl
│   ├── link_1.stl
│   ├── link_2.stl
│   ├── link_3.stl
│   ├── link_4.stl
│   ├── link_5.stl
│   └── link_6.stl
└── limits.xml
```
## Joint Limit Patterns

### Typical Ranges
- **Joint 1**: ±270° to ±360° (base rotation)
- **Joint 2**: -100° to +130° (shoulder)
- **Joint 3**: -200° to +70° (elbow)
- **Joint 4**: ±360° (wrist roll)
- **Joint 5**: ±130° (wrist pitch)
- **Joint 6**: ±360° (wrist yaw)

### Velocity Limits
- Smaller joints (wrist): Higher velocities (3-13 rad/s)
- Larger joints (base, shoulder): Lower velocities (2-8 rad/s)

## Best Practices

1. **Consistent Naming**: Use standard link and joint names
2. **Proper Scaling**: Ensure mesh files are correctly scaled
3. **Realistic Inertials**: Include proper mass and inertia values
4. **Joint Limits**: Set realistic position, velocity, and effort limits
5. **Tool Frame**: Include flange and tool0 frames for end effector mounting
6. **Collision Geometry**: Use appropriate collision meshes for safety
7. **Validation**: Test URDF files with validation tools
