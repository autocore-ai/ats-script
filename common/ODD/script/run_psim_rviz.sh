#! /bin/bash
xhost +

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
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --env "DISPLAY" \
    --privileged \
    autocore/ats-devel /bin/bash -c  \
    "cd /ros1_workspace && \
    source install/setup.bash && \
    roslaunch autoware_launch planning_simulator.launch map_path:=/data/psim vehicle_model:=lexus sensor_model:=aip_xx1"
