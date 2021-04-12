FROM ros:rolling
ADD . /autotest
WORKDIR /autotest
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
CMD source /opt/ros/rolling/setup.bash && source msg/install/setup.bash