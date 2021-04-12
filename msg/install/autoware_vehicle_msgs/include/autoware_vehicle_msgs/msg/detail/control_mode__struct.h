// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_vehicle_msgs:msg/ControlMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__STRUCT_H_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'MANUAL'.
enum
{
  autoware_vehicle_msgs__msg__ControlMode__MANUAL = 0
};

/// Constant 'AUTO'.
enum
{
  autoware_vehicle_msgs__msg__ControlMode__AUTO = 1
};

/// Constant 'AUTO_STEER_ONLY'.
enum
{
  autoware_vehicle_msgs__msg__ControlMode__AUTO_STEER_ONLY = 2
};

/// Constant 'AUTO_PEDAL_ONLY'.
enum
{
  autoware_vehicle_msgs__msg__ControlMode__AUTO_PEDAL_ONLY = 3
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

// Struct defined in msg/ControlMode in the package autoware_vehicle_msgs.
typedef struct autoware_vehicle_msgs__msg__ControlMode
{
  std_msgs__msg__Header header;
  int32_t data;
} autoware_vehicle_msgs__msg__ControlMode;

// Struct for a sequence of autoware_vehicle_msgs__msg__ControlMode.
typedef struct autoware_vehicle_msgs__msg__ControlMode__Sequence
{
  autoware_vehicle_msgs__msg__ControlMode * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_vehicle_msgs__msg__ControlMode__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__STRUCT_H_
