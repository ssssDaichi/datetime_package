import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def main():
    # ROS2ノードの初期化
    rclpy.init()
    # ノードの名前を "datetime_listener" に設定
    node = Node("datetime_listener")

    # コールバック関数: メッセージを受信して表示する
    def cb(msg):
        # ログに受信内容を出力
        node.get_logger().info(f"Listen: {msg.data}")

    # トピック "datetime_topic" を購読するサブスクライバーを作成
    node.create_subscription(String, "datetime_topic", cb, 10)

    # ノードの実行を開始
    rclpy.spin(node)

if __name__ == "__main__":
    main()
