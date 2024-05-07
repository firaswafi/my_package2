from launch import launch_description
from launch_ros.actions import Node

def generate_launch_discription():
    return launch_description([
        Node(
            package ='demo_nodes_py',
            executable='listener'
        )
    ])