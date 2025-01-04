#!/bin/bash

# ディレクトリ設定
dir=~
if [ "$1" != "" ]; then
    dir="$1"
fi

# ワークスペースに移動
cd "$dir/ros2_ws" || exit

# colcon buildの実行
colcon build

# 環境をセットアップ
source "$dir/.bashrc"

# 10秒間launchファイルを実行し、ログを/tmpディレクトリに保存
timeout 10 ros2 launch mypkg datetime_talk_listen.launch.py > /tmp/mypkg.log

# ログをgrepで確認し、特定の行を探す
cat /tmp/mypkg.log | grep 'Listen:'

