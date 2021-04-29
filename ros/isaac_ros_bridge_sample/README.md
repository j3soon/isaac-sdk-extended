# isaac_ros_bridge_sample

ROS: Melodic
Python: Python 3.6

## Setup

```sh
./setup.sh
```

TODO: Test the setup script on a clean PC

## Run ROS package

```sh
./test.sh
```

## Notes on setting up the catkin workspace

```sh
# Assume already performed setup
# Assume in 'ros' directory
DIR=$(pwd)
echo $DIR
mkdir -p $DIR/isaac_ros_bridge_sample
cd $DIR/isaac_ros_bridge_sample
DIR_WS=$(pwd)
echo $DIR_WS
```

Create workspace:

```sh
cd $DIR
source /opt/ros/melodic/setup.bash
mkdir -p $DIR_WS/src
cd $DIR_WS
catkin_make
source activate.sh
```

Create package

```sh
cd $DIR/isaac_ros_bridge_sample/src
catkin_create_pkg isaac_ros_bridge_sample std_msgs rospy roscpp
cd $DIR/isaac_ros_bridge_sample
catkin_make
source activate.sh
```

Fill in TODOs in package.xml