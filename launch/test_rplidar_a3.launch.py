from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            node_name='rplidar_composition',
            package='rplidar_ros',
            node_executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyTHS1',
                'serial_baudrate': 115200,
                'frame_id': 'laser',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Sensitivity',
            }],
        ),
        Node(
            node_name='rplidarNodeClient',
            package='rplidar_ros',
            node_executable='rplidarNodeClient',
            output='screen',
        ),
    ])
