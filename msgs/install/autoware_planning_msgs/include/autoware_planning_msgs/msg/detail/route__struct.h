// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_planning_msgs:msg/Route.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__STRUCT_H_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__STRUCT_H_

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
// Member 'goal_pose'
#include "geometry_msgs/msg/detail/pose__struct.h"
// Member 'route_sections'
#include "autoware_planning_msgs/msg/detail/route_section__struct.h"

// Struct defined in msg/Route in the package autoware_planning_msgs.
typedef struct autoware_planning_msgs__msg__Route
{
  std_msgs__msg__Header header;
  geometry_msgs__msg__Pose goal_pose;
  autoware_planning_msgs__msg__RouteSection__Sequence route_sections;
} autoware_planning_msgs__msg__Route;

// Struct for a sequence of autoware_planning_msgs__msg__Route.
typedef struct autoware_planning_msgs__msg__Route__Sequence
{
  autoware_planning_msgs__msg__Route * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_planning_msgs__msg__Route__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__STRUCT_H_
