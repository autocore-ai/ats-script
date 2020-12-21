# Add planning Cases


##1. Prepare the planning bag and extract the coordinate information of starting , ending ,obstacles info

##2. Save bag to the specified path
        eg.: if you named your testcase name : gt_01
        bag file : ../autotest/bags/planning/gt_01/gt_01.bag
##3. Store the coordinate information of starting ， ending and obstacles to the specified CSV file
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
|bag_name|YES| your bag file name 
|duration|YES | your bag info duration 