from rclpy.action import ActionClient
from rclpy.duration import Duration
import rclpy
from rclpy.node import Node

from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint


class JointMotionDemo(Node):
    def __init__(self):
        super().__init__("crb15000_joint_motion_demo")
        self._client = ActionClient(
            self,
            FollowJointTrajectory,
            "/crb15000_arm_controller/follow_joint_trajectory",
        )
        self._joint_names = [
            "joint_1",
            "joint_2",
            "joint_3",
            "joint_4",
            "joint_5",
            "joint_6",
        ]

    def run(self):
        self.get_logger().info("Waiting for trajectory action server...")
        if not self._client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error(
                "Trajectory action server not available. "
                "Start the MoveIt demo launch and make sure ros2_control controllers are installed."
            )
            return 1

        goal = FollowJointTrajectory.Goal()
        goal.trajectory.joint_names = self._joint_names
        goal.trajectory.points = [
            self._make_point([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 2.0),
            self._make_point([0.3, -0.5, 0.4, 0.0, 0.3, 0.0], 5.0),
            self._make_point([-0.3, -0.2, 0.2, 0.2, -0.3, 0.1], 8.0),
            self._make_point([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 11.0),
        ]
        goal.goal_time_tolerance = Duration(seconds=1.0).to_msg()

        self.get_logger().info("Sending demo joint trajectory...")
        send_future = self._client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self, send_future)

        goal_handle = send_future.result()
        if goal_handle is None or not goal_handle.accepted:
            self.get_logger().error("Trajectory goal was rejected.")
            return 1

        self.get_logger().info("Trajectory goal accepted, waiting for result...")
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        result = result_future.result()
        if result is None:
            self.get_logger().error("No result returned from trajectory action.")
            return 1

        error_code = result.result.error_code
        error_string = result.result.error_string
        if error_code != 0:
            self.get_logger().error(
                f"Trajectory execution failed with code {error_code}: {error_string}"
            )
            return 1

        self.get_logger().info("Trajectory execution completed successfully.")
        return 0

    def _make_point(self, positions, time_from_start_sec):
        point = JointTrajectoryPoint()
        point.positions = positions
        point.time_from_start = Duration(seconds=time_from_start_sec).to_msg()
        return point


def main():
    rclpy.init()
    node = JointMotionDemo()
    try:
        raise_code = node.run()
    finally:
        node.destroy_node()
        rclpy.shutdown()
    raise SystemExit(raise_code)
