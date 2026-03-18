import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MoteurNode(Node):
    def __init__(self):
        super().__init__('moteur_node')

        self.last_received = ""  # stocke la dernière valeur reçue

        self._init_publishers()
        self._init_subscribers()
    
        self.create_timer(0.1, self.publisher_callback)

    def _init_publishers(self):
        self.pub_moteur = self.create_publisher(String, 'moteur_val', 10)
        self.get_logger().info("Publishers initialisés")

    def _init_subscribers(self):
        self.sub_moteur = self.create_subscription(
            String,
            '/cmdVel/moteur',
            self.subscriber_callback,
            10
        )
        self.get_logger().info("Subscribers initialisés")

    def subscriber_callback(self, msg):
        self.last_received = msg.data
        self.get_logger().info(f"Reçu: {msg.data}")

    def publisher_callback(self):
        msg = String()
        msg.data = self.last_received  # ou toute autre valeur string
        self.pub_moteur.publish(msg)
        self.get_logger().info(f"Publié: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = MoteurNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()