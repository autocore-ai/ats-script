// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_planning_msgs:msg/LaneChangeCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_COMMAND__STRUCT_H_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_COMMAND__STRUCT_H_

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

// Struct defined in msg/LaneChangeCommand in the package autoware_planning_msgs.
typedef struct autoware_planning_msgs__msg__LaneChangeCommand
{
  builtin_interfaces__msg__Time stamp;
  bool command;
} autoware_planning_msgs__msg__LaneChangeCommand;

// Struct for a sequence of autoware_planning_msgs__msg__LaneChangeCommand.
typedef struct autoware_planning_msgs__msg__LaneChangeCommand__Sequence
{
  autoware_planning_msgs__msg__LaneChangeCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_planning_msgs__msg__LaneChangeCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_COMMAND__STRUCT_H_
