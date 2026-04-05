import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircleMotionPublisher(Node):
    def __init__(self) -> None:
        super().__init__('circle_motion')
        self.publisher_ = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )
        self.timer = self.create_timer(0.1, self.publish_velocity)
        self.get_logger().info('Circle Motion Publisher started! Publishing to /cmd_vel')

    def publish_velocity(self) -> None:
        msg = Twist()
        msg.linear.x = 0.3
        msg.angular.z = 0.5
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Publishing velocity: linear={msg.linear.x}, angular={msg.angular.z}'
        )


def main(args=None) -> None:
    rclpy.init(args=args)
    node = CircleMotionPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
