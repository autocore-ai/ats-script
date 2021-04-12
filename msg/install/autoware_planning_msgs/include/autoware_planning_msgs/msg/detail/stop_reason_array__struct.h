// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_planning_msgs:msg/StopReasonArray.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON_ARRAY__STRUCT_H_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON_ARRAY__STRUCT_H_

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
// Member 'stop_reasons'
#include "autoware_planning_msgs/msg/detail/stop_reason__struct.h"

// Struct defined in msg/StopReasonArray in the package autoware_planning_msgs.
typedef struct autoware_planning_msgs__msg__StopReasonArray
{
  std_msgs__msg__Header header;
  autoware_planning_msgs__msg__StopReason__Sequence stop_reasons;
} autoware_planning_msgs__msg__StopReasonArray;

// Struct for a sequence of autoware_planning_msgs__msg__StopReasonArray.
typedef struct autoware_planning_msgs__msg__StopReasonArray__Sequence
{
  autoware_planning_msgs__msg__StopReasonArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_planning_msgs__msg__StopReasonArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON_ARRAY__STRUCT_H_
