// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_planning_msgs:msg/LaneChangeStatus.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_STATUS__STRUCT_H_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

// Struct defined in msg/LaneChangeStatus in the package autoware_planning_msgs.
typedef struct autoware_planning_msgs__msg__LaneChangeStatus
{
  builtin_interfaces__msg__Time stamp;
  bool status;
} autoware_planning_msgs__msg__LaneChangeStatus;

// Struct for a sequence of autoware_planning_msgs__msg__LaneChangeStatus.
typedef struct autoware_planning_msgs__msg__LaneChangeStatus__Sequence
{
  autoware_planning_msgs__msg__LaneChangeStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_planning_msgs__msg__LaneChangeStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_STATUS__STRUCT_H_
