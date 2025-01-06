#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Daichi Hirose
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from pycaw.pycaw import AudioUtilities

def get_system_volume():
    """システム音量を取得する関数"""
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        return int(volume.GetMasterVolume() * 100)  # 音量を0-100%で取得

def main():
    # ROS 2ノードの初期化
    rclpy.init()
    # ノードの名前を"volume_talker"に設定
    node = Node("volume_talker")

    # トピック名 "volume_topic" に音量データを送信するパブリッシャーを作成
    pub = node.create_publisher(String, "volume_topic", 10)

    # コールバック関数: システム音量を取得してパブリッシュする
    def cb():
        msg = String()
        # 現在の音量を取得
        volume_level = get_system_volume()
        msg.data = f"Volume Level: {volume_level}%"  # ログ出力を簡潔に
        # パブリッシャーを使って送信
        pub.publish(msg)
        # ログで送信内容を確認
        node.get_logger().info(f"Published: {msg.data}")

    # タイマー - 1秒ごとにコールバック関数を実行
    node.create_timer(1.0, cb)

    # ノードの実行を開始
    rclpy.spin(node)

if __name__ == "__main__":
    main()

