# ABB GoFa CRB15000 ROS 2 Control

ROS 2 (Jazzy Jalisco) workspace for controlling the **ABB CRB15000 12/1.27 GoFa collaborative robot**.

## Overview

This project provides ROS 2 motion planning and trajectory execution for the ABB GoFa CRB15000 12/1.27 robot. It is adapted from [ros-industrial/abb](https://github.com/ros-industrial/abb) with ROS 1 → ROS 2 conversion and manual MoveIt configuration.

## Packages

| Package | Type | Description |
|---------|------|-------------|
| `abb_resources` | ament_cmake | Shared materials and color definitions |
| `abb_crb15000_support` | ament_cmake | URDF/Xacro robot descriptions and meshes |
| `abb_crb15000_12_127_moveit_config` | ament_cmake | MoveIt configuration (6-DOF, planning group `manipulator`) |
| `abb_crb15000_py_demo` | ament_python | Python demo for joint trajectory execution |

## Requirements

- ROS 2 Jazzy Jalisco
- MoveIt 2
- `ros2_controllers` & `joint_trajectory_controller`
- `xacro`
- `control_msgs`

Install missing dependencies:

```bash
sudo apt install ros-jazzy-ros2-controls ros-jazzy-moveit
```

## Build

```bash
cd /path/to/ros2_ws_abbgofar_ST
source /opt/ros/jazzy/setup.bash
colcon build
```

## Run

**1. Launch MoveIt with RViz:**

```bash
source install/setup.bash
export ROS_HOME=/tmp/ros_home
ros2 launch abb_crb15000_12_127_moveit_config demo.launch.py
```

**2. Run the trajectory demo (in another terminal):**

```bash
source install/setup.bash
ros2 run abb_crb15000_py_demo joint_motion_demo
```

## Project Structure

```
src/
├── abb_resources/
├── abb_crb15000_support/          # Robot description (URDF/Xacro)
├── abb_crb15000_12_127_moveit_config/  # MoveIt config & launch files
└── abb_crb15000_py_demo/          # Python demo node
explain/
├── 环境搭建.md                    # Environment setup guide (Chinese)
├── MoveIt和运动演示.md            # MoveIt tutorial (Chinese)
└── git使用.md                     # Git usage notes (Chinese)
```

## Key Features

- MoveIt motion planning with RViz visualization
- `joint_trajectory_controller` integration via ros2_control
- Python demo sending joint targets via `/crb15000_arm_controller/follow_joint_trajectory`

## Known Issues

Controller plugin errors (`joint_state_broadcaster`, `crb15000_arm_controller` not found) can be resolved with:

```bash
sudo apt install ros-jazzy-ros2-controllers
```

## License

Based on ros-industrial/abb. See parent project for license details.

## 中文部分

中文readme详见explain文件夹。

