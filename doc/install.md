# Deployment
## ros1

## python3.6 - ubuntu with python3.6, don't need to install
## Install JDK
```
sudo apt-get update
sudo apt-get install openjdk-8-jdk
sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_version/bin/java
java -version  # show version make sure install successfully
```
  
## Install Allure
curl -o allure-2.7.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.tgz
sudo tar -zxvf allure-2.7.0.tgz -C /opt/
sudo ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure
rm -rf allure-2.7.0.tgz
allure --version


## install pip3
```
sudo apt-get install python3-pip
```

## install autotest frame
```
git clone 
cd autotest
pip3 install -r requirements.txt
```