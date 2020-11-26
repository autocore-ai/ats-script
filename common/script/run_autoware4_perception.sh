#! /bin/bash

docker run -d --rm \
    -v /root/autoware4/src \
    --name=config \
    nuc:5000/autocore/autoware4config:0.0.4-pc-perception /bin/sh -c "sleep 10s"

docker run -id --rm \
    -v /root/autoware4/devel \
    --name=exe \
    nuc:5000/autocore/autoware4exe:0.0.2-ros-eloquent-bridge-amd64 /bin/sh -c "sleep 10s"

docker run -it --net=host --gpus=all --rm\
    --name=devel \
    --volumes-from exe \
    --volumes-from config \
    nuc:5000/autocore/autoware4runtime:0.0.1-ros-eloquent-bridge-amd64 /bin/bash -c "source /opt/ros/melodic/setup.bash && source /root/autoware4/devel/setup.bash && export ROS_IP=192.168.50.235 && export ROS_MASTER_URI=http://192.168.50.235:11311 && roslaunch autoware_launch autoware.launch"

