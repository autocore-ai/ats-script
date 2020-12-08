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
    --volumes-from debug \
    --volumes-from data \
    actst/devel /bin/bash -c  \
    "cd /AutowareArchitectureProposal && \
    source install/setup.bash && \
    roslaunch autoware_launch logging_simulator.launch map_path:=/AutowareArchitectureProposal/data/rosbag vehicle_model:=lexus sensor_model:=aip_xx1 rosbag:=true"