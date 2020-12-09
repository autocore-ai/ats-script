#! /bin/bash

docker run -d --rm \
    -v /AutowareArchitectureProposal/install \
    --name=debug \
    actst/debug /bin/sh -c "sleep 30s"

docker run -d --rm \
    -v /AutowareArchitectureProposal/data \
    --name=data \
    actst/data /bin/sh -c "sleep 30s"

docker run -it --net=host --gpus=all --rm \
    --name=runtime \
    --name=autoware4_open \
    --volumes-from debug \
    --volumes-from data \
    -volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --env "DISPLAY" \
    --privileged \
    actst/devel /bin/bash -c  \
    "cd /AutowareArchitectureProposal &&
    source install/setup.bash &&
    export ROS_IP=${ROS_IP} && export ROS_MASTER_URI=${ROS_MASTER_URI} &&
    roslaunch autoware_launch logging_simulator.launch map_path:=/AutowareArchitectureProposal/data/rosbag vehicle_model:=lexus sensor_model:=aip_xx1 rosbag:=true"