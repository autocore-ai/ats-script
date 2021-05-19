FROM ros:rolling
ADD . /autotest
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y vim
RUN apt-get install -y openjdk-8-jdk && java -version
RUN apt-get install -y wget && wget https://github.com/allure-framework/allure2/releases/download/2.7.0/allure-2.7.0.tgz
RUN tar -zxvf allure-2.7.0.tgz -C /opt/ && ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure && allure --version && rm -rf allure-2.7.0.tgz
WORKDIR  /autotest/testSDV/msgs
RUN /bin/bash -c "source /opt/ros/rolling/setup.bash && colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release"
WORKDIR /autotest
RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple
RUN /bin/bash -c "source /opt/ros/rolling/setup.bash && source /autotest/testSDV/msgs/install/setup.bash"
ENTRYPOINT ["bash", "./start.sh"]
