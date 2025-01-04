import launch
import launch_ros.actions

def generate_launch_description():
    datetime_talker = launch_ros.actions.Node(
        package='mypkg',  # パッケージ名
        executable='datetime_talker',  # 実行ファイル名
    )
    datetime_listener = launch_ros.actions.Node(
        package='mypkg',  # パッケージ名
        executable='datetime_listener',  # 実行ファイル名
        output='screen',  # ログを画面に表示
    )
    return launch.LaunchDescription([datetime_talker, datetime_listener])
