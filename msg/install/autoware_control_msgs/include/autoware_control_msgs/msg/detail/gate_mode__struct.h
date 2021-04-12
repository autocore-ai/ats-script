// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_control_msgs:msg/GateMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__GATE_MODE__STRUCT_H_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__GATE_MODE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'AUTO'.
enum
{
  autoware_control_msgs__msg__GateMode__AUTO = 0
};

/// Constant 'REMOTE'.
enum
{
  autoware_control_msgs__msg__GateMode__REMOTE = 1
};

// Struct defined in msg/GateMode in the package autoware_control_msgs.
typedef struct autoware_control_msgs__msg__GateMode
{
  uint8_t data;
} autoware_control_msgs__msg__GateMode;

// Struct for a sequence of autoware_control_msgs__msg__GateMode.
typedef struct autoware_control_msgs__msg__GateMode__Sequence
{
  autoware_control_msgs__msg__GateMode * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_control_msgs__msg__GateMode__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__GATE_MODE__STRUCT_H_
