// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_control_msgs:msg/EngageMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__STRUCT_H_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/EngageMode in the package autoware_control_msgs.
typedef struct autoware_control_msgs__msg__EngageMode
{
  bool is_engaged;
} autoware_control_msgs__msg__EngageMode;

// Struct for a sequence of autoware_control_msgs__msg__EngageMode.
typedef struct autoware_control_msgs__msg__EngageMode__Sequence
{
  autoware_control_msgs__msg__EngageMode * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_control_msgs__msg__EngageMode__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__STRUCT_H_
