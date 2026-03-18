import rclpy
from rclpy.node import Node
from std_msgs.msg import String
 
 
class MinimalPublisher(Node):
    """A minimal ROS2 publisher node that publishes to the 'topic' topic."""
 
    def __init__(self):
        super().__init__('minimal_publisher')
 
        # Create publisher: message type, topic name, queue size (QoS depth)
        self.publisher_ = self.create_publisher(String, 'topic', 10)
 
        # Create a timer that fires every 0.5 seconds
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
 
        self.i = 0  # message counter
        self.get_logger().info('Publisher node started.')
 
    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, ROS2! Count: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1
 
 
def main(args=None):
    rclpy.init(args=args)
 
    node = MinimalPublisher()
 
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Publisher stopped by user.')
    finally:
        node.destroy_node()
        rclpy.shutdown()
 
 
if __name__ == '__main__':
    main()
 