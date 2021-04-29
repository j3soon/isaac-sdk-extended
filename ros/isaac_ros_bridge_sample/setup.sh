#!/bin/bash
set -e

CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Create virtual env
cd $CUR_DIR
virtualenv venv -p python3.6
source venv/bin/activate
# For python lib
pip install cython numpy opencv-python pyopengl
# For ROS package
pip install pyyaml rospkg
catkin_make
