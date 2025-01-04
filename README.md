# ROS 2 DatetimeTalkerで現在日時を取得
このROS 2パッケージは、DatetimeTalkerノードを使用して、システムの現在日時を定期的にパブリッシュします。また、DatetimeListenerノードがその時刻を受信し、出力を表示します。
### 概要
DatetimeTalker: 毎秒現在日時を取得してパブリッシュします。

DatetimeListener: 受信した日時を端末に出力します。
### セットアップ方法
#### リポジトリをクローン
以下のコマンドを使用してリポジトリをクローンしてください。
```
git clone https://github.com/ssssDaichi/datetime_package.git
```
#### パッケージをビルド
クローン後、ディレクトリに移動してビルドを実行します。
```
cd datetime_package
colcon build
```
#### 環境をソースする
以下のコマンドで環境をセットアップしてください。
```
source install/setup.bash
```
#### ノードを実行する
DatetimeTalkerとDatetimeListenerを起動するには以下を使用します。
```
ros2 launch mypkg datetime_talk_listen.launch.py
```
### 実行例
以下はDatetimeTalkerとDatetimeListenerの実行例です：
```
[datetime_talker]: Published: 現在の日時: 2025-01-04 16:07:23
[datetime_listener]: Listen: 現在の日時: 2025-01-04 16:07:23
```
### 動作環境
Ubuntu 22.04 LTS

ROS 2 (Humble以降)

Python 3.8以上
#### ライセンス
このリポジトリはBSD-3-Clauseライセンスのもとで公開されています。
#### Copyright
© 2025 Daichi Hirose
