# Deployment

## Install ros1 
http://wiki.ros.org/melodic/Installation

## python3.6 

ubuntu with python3.6

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

## update config

   - cd */autotes
   - vi config.py
   - update ROS1_SETUP, value is your ros1's setup.bash, such as: "ROS1_SETUP= '/opt/ros/melodic/setup.bash'"
   
And now, you can to run cases.
