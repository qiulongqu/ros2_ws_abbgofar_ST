# ros2_ws_abbgofar 使用说明

## 1. 工作区构建

第一次使用，或修改了 `urdf/xacro/moveit_config` 之后，先重新编译：

```bash
cd /home/yunhao/ros2_ws_abbgofar
source /opt/ros/jazzy/setup.bash
colcon build
```

## 2. 启动 ABB CRB15000 12/1.27 的 MoveIt 演示

```bash
cd /home/yunhao/ros2_ws_abbgofar
source /opt/ros/jazzy/setup.bash
source install/setup.bash
export ROS_HOME=/tmp/ros_home
export ROS_LOG_DIR=/tmp/ros_logs
ros2 launch abb_crb15000_12_127_moveit_config demo.launch.py
```

说明：

- 这里启动的是本工程中已经生成好的 MoveIt 配置包 `abb_crb15000_12_127_moveit_config`
- RViz 会自动加载专用配置文件，并把固定坐标系设置为 `world`
- 正常情况下，启动后应能看到 ABB 机械臂模型和 MoveIt 的 `MotionPlanning` 面板

## 3. 如果 RViz 中提示 `Frame [map] does not exist`

这通常说明 RViz 没有加载本工程自带的配置文件，或者固定坐标系被手动改掉了。

请检查：

- `Global Options -> Fixed Frame` 是否为 `world`
- 左侧 `Displays` 中的 `MotionPlanning` 是否已启用
- `MotionPlanning -> Planning Group` 是否为 `manipulator`

如果 RViz 配置被改乱，可以直接重新启动上一节的命令。

## 4. 当前工程中用到的主要包

- `abb_crb15000_support`
  - 机械臂的 URDF/Xacro 和 mesh
- `abb_resources`
  - 公共材质和资源文件
- `abb_crb15000_12_127_moveit_config`
  - 为 `crb15000_12_127` 直接生成的 MoveIt 配置包骨架

## 5. 当前已知问题

当前环境中，MoveIt 规划已经可以正常启动，但轨迹执行控制器可能还没有安装完整。

如果终端里出现类似下面的报错：

- `Loader for controller 'joint_state_broadcaster' not found`
- `Loader for controller 'crb15000_arm_controller' not found`

说明系统里缺少 ros2_control 控制器插件。可以安装：

```bash
sudo apt install ros-jazzy-ros2-controllers
```

或者单独安装：

```bash
sudo apt install ros-jazzy-joint-state-broadcaster ros-jazzy-joint-trajectory-controller
```

说明：

- 缺少这些控制器时，通常仍然可以打开 RViz 并进行运动规划
- 但执行轨迹、联动假控制器或后续 Python 运动脚本时会受影响

## 6. 关于 Setup Assistant

本工程当前已经绕过 `moveit_setup_assistant`，直接提供了可用的 MoveIt 配置骨架。

因此目前不必依赖：

```bash
ros2 run moveit_setup_assistant moveit_setup_assistant
```

后续如果只是继续调试 ABB 机械臂模型、MoveIt 配置或 Python 控制脚本，直接使用本工作区现有包即可。

## 7. Python 最小关节运动示例

本工程已经添加了一个最小 Python 示例包：

- `abb_crb15000_py_demo`

其中示例脚本会向控制器动作接口发送一段简单的关节轨迹：

- `joint_1` 到 `joint_6` 先从零位运动到一个目标姿态
- 然后再运动到第二个姿态
- 最后回到零位

运行步骤：

1. 先启动 MoveIt 演示

```bash
cd /home/yunhao/ros2_ws_abbgofar
source /opt/ros/jazzy/setup.bash
source install/setup.bash
export ROS_HOME=/tmp/ros_home
export ROS_LOG_DIR=/tmp/ros_logs
ros2 launch abb_crb15000_12_127_moveit_config demo.launch.py
```

2. 另开一个终端运行 Python 示例

```bash
cd /home/yunhao/ros2_ws_abbgofar
source /opt/ros/jazzy/setup.bash
source install/setup.bash
ros2 run abb_crb15000_py_demo joint_motion_demo
```

说明：

- 脚本文件位置：`src/abb_crb15000_py_demo/abb_crb15000_py_demo/joint_motion_demo.py`
- 脚本通过 `/crb15000_arm_controller/follow_joint_trajectory` 发送轨迹
- 如果控制器没有正确安装或没有启动，脚本会提示 action server 不可用
