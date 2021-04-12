# Deployment

## Install ros2
rolling

## python3.8.5 

ubuntu with python3.8

## Install JDK

Allure need JDK
```
sudo apt-get update
sudo apt-get install openjdk-8-jdk
java -version  # show version make sure install successfully
```
  
## Install Allure
To generate beautiful test reports

```
curl -o allure-2.7.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.tgz
sudo tar -zxvf allure-2.7.0.tgz -C /opt/
sudo ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure
rm -rf allure-2.7.0.tgz
allure --version
```

## Install pip3
```
sudo apt-get install python3-pip
```

## Install autotest frame
```
git clone https://gitlab.com/autocore/AutoTest/autotest.git
cd autotest
pip3 install -r requirements.txt
```

## Download perception and planning dockers
```
cd autotest/common/script
. run_rosbag.sh  // download perception docker
. run_psim.sh  // download planning docker
```

## Change to use bash

After execute 'ls -l /bin/sh', if the result is /bin/sh -> dash, you need to exec:

    - sudo  dpkg-reconfigure dash

    - choose no

    - exec 'ls -l /bin/sh', make sure result is '/bin/sh -> bash'

## build msg， generate Python autoware message data module

1. copy autoware4's msg to local dir
   
2. cd msg
   
3. source /opt/ros/rolling/setup.bash
   
4. colcon build

5. After build successful, source ./install/setup.bash

And now, you can to run cases.
