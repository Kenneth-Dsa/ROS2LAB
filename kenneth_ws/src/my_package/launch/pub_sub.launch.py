#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_package',
            executable='publisher',
            name='publisher'
        ),
        Node(
            package='my_package',
            executable='subscriber',
            name='subscriber'
        )
    ])