# Add planning Cases

## 1. insert cases
sample csv:

![planning](/docs/images/planning_cases.png)

Fields description:

|  Field   | Required  | Description  |
|  ----  | ----  | ----  |
| Priority  | Yes  | Use case priority, can be one of blocker/critical/normal/minor/trivial |
| Story  | Yes | Test case story  |
| CaseName  | Yes | Test case name, it will be function name of tested case. So it must start with 'test_'  |
| Title  | Yes | Title of cases, the description of the use case |
|start.position.x | YES | extract from /initialpose
|start.position.y|YES | extract from /initialpose
|start.position.z|YES | extract from /initialpose
|start.orientation.x|YES| extract from /initialpose
|start.orientation.y|YES| extract from /initialpose
|start.orientation.z|YES| extract from /initialpose
|start.orientation.w|YES| extract from /initialpose
|end.position.x|YES| extract from /planning/mission_planning/goal
|end.position.y|YES| extract from /planning/mission_planning/goal
|end.position.z|YES| extract from /planning/mission_planning/goal
|end.orientation.x|YES| extract from /planning/mission_planning/goal
|end.orientation.y|YES| extract from /planning/mission_planning/goal
|end.orientation.z|YES| extract from /planning/mission_planning/goal
|end.orientation.w|YES| extract from /planning/mission_planning/goal
|bag_name|YES| groundtruth bag file name 
|duration|YES | groundtruth bag info duration 

## 2. Prepare groundtruth bag and extract the coordinate information of starting , ending ,obstacles info
      1. open rviz 
      2. rosbag record:  rosbag record -o <package-name> 
      3. setting start point end point, obstacle opsition 
      4. end recording
      5. check rosbag : rosbag info  <package-name>
## 3. Save bag to the specified path
        eg.: if you named your testcase name : gt_01
        bag file : ../autotest/bags/planning/gt_01/gt_01.bag
## 4. Store the coordinate information of starting ， ending and obstacles to the specified CSV file


## 5 Support cases
        Current test version support: test planning a straight route 
        includes following topics : planning/scenario_planning/trajectory /current_pose " \
         "/vehicle/status/twist /vehicle/status/velocity /planning/mission_planning/route"
         
        The later version would support the information :
                1. detection of turning left and right and 
                2. adding obstacles : moving, static
                3. traffic light 
                4. parking scenario 
                5. crossing roads , intersaction , sidewalk , blind spots