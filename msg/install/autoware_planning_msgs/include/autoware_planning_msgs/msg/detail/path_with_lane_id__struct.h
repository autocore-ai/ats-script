// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_planning_msgs:msg/PathWithLaneId.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__PATH_WITH_LANE_ID__STRUCT_H_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__PATH_WITH_LANE_ID__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'points'
#include "autoware_planning_msgs/msg/detail/path_point_with_lane_id__struct.h"
// Member 'drivable_area'
#include "nav_msgs/msg/detail/occupancy_grid__struct.h"

// Struct defined in msg/PathWithLaneId in the package autoware_planning_msgs.
typedef struct autoware_planning_msgs__msg__PathWithLaneId
{
  std_msgs__msg__Header header;
  autoware_planning_msgs__msg__PathPointWithLaneId__Sequence points;
  nav_msgs__msg__OccupancyGrid drivable_area;
} autoware_planning_msgs__msg__PathWithLaneId;

// Struct for a sequence of autoware_planning_msgs__msg__PathWithLaneId.
typedef struct autoware_planning_msgs__msg__PathWithLaneId__Sequence
{
  autoware_planning_msgs__msg__PathWithLaneId * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_planning_msgs__msg__PathWithLaneId__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__PATH_WITH_LANE_ID__STRUCT_H_
