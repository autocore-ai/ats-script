// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_vehicle_msgs:msg/Steering.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__STEERING__STRUCT_H_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__STEERING__STRUCT_H_

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

// Struct defined in msg/Steering in the package autoware_vehicle_msgs.
typedef struct autoware_vehicle_msgs__msg__Steering
{
  std_msgs__msg__Header header;
  float data;
} autoware_vehicle_msgs__msg__Steering;

// Struct for a sequence of autoware_vehicle_msgs__msg__Steering.
typedef struct autoware_vehicle_msgs__msg__Steering__Sequence
{
  autoware_vehicle_msgs__msg__Steering * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_vehicle_msgs__msg__Steering__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__STEERING__STRUCT_H_
