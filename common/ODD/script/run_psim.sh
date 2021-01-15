#!/bin/bash

xhost +

docker run -id --rm \
    -v /AutowareArchitectureProposal/install \
    --name=exe-ros2 \
    ghcr.io/autocore-ai/exe-foxy-pc

docker run -id --rm \
    -v /data \
    --name=data-ros2 \
    ghcr.io/autocore-ai/data-foxy

docker run -d --gpus=all --rm \
    --name=runtime-ros2 \
    --volumes-from exe-ros2 \
    --volumes-from data-ros2 \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --env "DISPLAY" \
    --privileged \
    ghcr.io/autocore-ai/devel-foxy-pc /bin/bash -c "/data/psim/run.sh"

docker stop exe-ros2 data-ros2