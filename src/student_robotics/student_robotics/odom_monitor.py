import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class OdomMonitor(Node):
    def __init__(self) -> None:
        super().__init__('odom_monitor')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10,
        )
        self.get_logger().info('Odom Monitor started! Listening to /odom')

    def odom_callback(self, msg: Odometry) -> None:
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        vx = msg.twist.twist.linear.x
        vz = msg.twist.twist.angular.z
        self.get_logger().info(
            f'Position: x={x:.2f}, y={y:.2f} | '
            f'Velocity: vx={vx:.2f}, vz={vz:.2f}'
        )


def main(args=None) -> None:
    rclpy.init(args=args)
    node = OdomMonitor()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
