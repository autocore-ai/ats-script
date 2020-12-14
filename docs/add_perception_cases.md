# Add Perception Cases
## 1. insert cases in perception cases csv file
sample csv:

![perception](/home/duan/PycharmProjects/auto_test/docs/images/perception_cases.png)

Fields description:

|  Field   | Required  | Description  |
|  ----  | ----  | ----  |
| Priority  | Yes  | Use case priority, can be one of blocker/critical/normal/minor/trivial |
| Story  | Yes | Test case story  |
| CaseName  | Yes | Test case name, it will be function name of tested case. So it must start with 'test_'  |
| Title  | Yes | Title of cases, the description of the use case |
| bag_name  | Yes | Name of rosbag, it will be played as the case is executed |
| bag_duration  | Yes | bag duration, it will be used in record perception's topic|


## 2. put your rosbag to the directory
 - cd */autotest/bags/perception_open
 - mkdir your bagname
 - cp your rosbag to dir
 
## ３．get your ground truth rosbag 
 
 - playing rosbag in a good environment
 - recording topic, command: rosbag record -O expect.bag --duration {bag_time} /perception/object_recognition/objects
 - check expect.bag data, you can use script[*/autotest/common/script/percep] to check. The script will analysis expect.bag, if you think the bag is not ok, can play and record bag until ok.

## 4．copy expected rosbag to dir
 - copy the expect.bag to '*/autotest/bags/perception_open/{your_rosbag_name}/'

