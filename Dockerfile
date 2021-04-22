FROM ros:rolling
ADD . /autotest
RUN apt-get update && apt-get install -y python3-pip
WORKDIR  /autotest/testSDV/msgs
RUN "source /opt/ros/rolling/setup.bash && colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release"
WORKDIR /autotest
RUN pip3 install -r requirements.txt
RUN "source /opt/ros/rolling/setup.bash && source /autotest/testSDV/msgs/install/setup.bash"
ENTRYPOINT ["bash", "./start.sh"]
