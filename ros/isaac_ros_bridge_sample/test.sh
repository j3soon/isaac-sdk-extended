#!/bin/bash

source activate.sh
# Launch roscore in new terminal
roscore &
P1=$!
# Launch zed camera publisher in new terminal
rosrun isaac_ros_bridge_sample image_publisher.py &
P2=$!
# Launch zed camera listener in new terminal
rosrun isaac_ros_bridge_sample ros_image_viewer.py &
P3=$!
# Launch zed camera listener in new terminal
rosrun isaac_ros_bridge_sample isaac_image_viewer.py
kill $P3
kill $P2
kill $P1
