import rclpy
from rclpy.node import Node
from std_msgs.msg import String
 
 
class MinimalSubscriber(Node):
    """A minimal ROS2 subscriber node that listens on the 'topic' topic."""
 
    def __init__(self):
        super().__init__('minimal_subscriber')
 
        # Create subscription: message type, topic name, callback, queue size
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10  # QoS depth
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Subscriber node started. Waiting for messages...')
 
    def listener_callback(self, msg: String):
        self.get_logger().info(f'Received: "{msg.data}"')
 
 
def main(args=None):
    rclpy.init(args=args)
 
    node = MinimalSubscriber()
 
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Subscriber stopped by user.')
    finally:
        node.destroy_node()
        rclpy.shutdown()
 
 
if __name__ == '__main__':
    main()