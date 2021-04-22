// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_planning_msgs:msg/RouteSection.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE_SECTION__STRUCT_H_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE_SECTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'lane_ids'
// Member 'continued_lane_ids'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in msg/RouteSection in the package autoware_planning_msgs.
typedef struct autoware_planning_msgs__msg__RouteSection
{
  rosidl_runtime_c__int64__Sequence lane_ids;
  int64_t preferred_lane_id;
  rosidl_runtime_c__int64__Sequence continued_lane_ids;
} autoware_planning_msgs__msg__RouteSection;

// Struct for a sequence of autoware_planning_msgs__msg__RouteSection.
typedef struct autoware_planning_msgs__msg__RouteSection__Sequence
{
  autoware_planning_msgs__msg__RouteSection * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_planning_msgs__msg__RouteSection__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE_SECTION__STRUCT_H_
