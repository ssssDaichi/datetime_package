import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

def main():
    # ROS2ノードの初期化
    rclpy.init()
    # ノードの名前を "datetime_talker" に設定
    node = Node("datetime_talker")

    # トピック名 "datetime_topic" に文字列型データを送信するパブリッシャーを作成
    pub = node.create_publisher(String, "datetime_topic", 10)

    # コールバック関数: 毎回日時を取得してパブリッシュする
    def cb():
        msg = String()
        # 現在の日時を取得してフォーマット
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg.data = f"現在の日時: {current_datetime}"
        # パブリッシャーを使って送信
        pub.publish(msg)
        # ログで送信内容を確認
        node.get_logger().info(f"Published: {msg.data}")

    # タイマー: 1秒ごとにコールバック関数を実行
    node.create_timer(1.0, cb)

    # ノードの実行を開始
    rclpy.spin(node)

if __name__ == "__main__":
    main()
