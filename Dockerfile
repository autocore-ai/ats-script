FROM ros:rolling
ADD ./autotest/ /autotest
WORKDIR /autotest