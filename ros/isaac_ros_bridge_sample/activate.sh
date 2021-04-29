DIR_WS="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
printf "Please ensure you just ran:\n\n    source activate.sh\n\n"

DIR=$DIR_WS/..
echo DIR: $DIR
echo DIR_WS: $DIR_WS

source $DIR_WS/devel/setup.bash
source $DIR_WS/venv/bin/activate
export ROS_MASTER_URI="http://$HOSTNAME:11311"
export ROS_HOSTNAME="$HOSTNAME"
