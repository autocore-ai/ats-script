// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_control_msgs:msg/EmergencyMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__EMERGENCY_MODE__STRUCT_H_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__EMERGENCY_MODE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/EmergencyMode in the package autoware_control_msgs.
typedef struct autoware_control_msgs__msg__EmergencyMode
{
  bool is_emergency;
} autoware_control_msgs__msg__EmergencyMode;

// Struct for a sequence of autoware_control_msgs__msg__EmergencyMode.
typedef struct autoware_control_msgs__msg__EmergencyMode__Sequence
{
  autoware_control_msgs__msg__EmergencyMode * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_control_msgs__msg__EmergencyMode__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__EMERGENCY_MODE__STRUCT_H_
