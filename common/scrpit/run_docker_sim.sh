docker run --rm -i --gpus=all --net=host --name=test_docker_sim --privileged -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v $HOME/.Xauthority:$HOME/.Xauthority:rw -e ROS_MASTER_URI=${ROS_MASTER_URI} -e ROS_IP=${ROS_IP} -e DISPLAY=${DISPLAY} -e XAUTHORITY=${XAUTH} autocore/simulator_for_sdk
