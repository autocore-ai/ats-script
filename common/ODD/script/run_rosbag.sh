#! /bin/bash

docker run -d --rm \
    -v /ros1_workspace/install \
    --name=debug \
    autocore/ats-exe /bin/sh -c "sleep 30s"

docker run -d --rm \
    -v /data \
    --name=data \
    autocore/ats-data /bin/sh -c "sleep 30s"

docker run -t --net=host --gpus=all --rm \
    --name=runtime \
    --volumes-from debug \
    --volumes-from data \
    --privileged \
    autocore/ats-devel /bin/bash -c  \
    "cd /ros1_workspace && \
    source install/setup.bash && \
    roslaunch autoware_launch logging_simulator.launch map_path:=/data/rosbag vehicle_model:=lexus sensor_model:=aip_xx1 rosbag:=true"
