// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_control_msgs:msg/ControlCommandStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__STRUCT_H_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__STRUCT_H_

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
// Member 'control'
#include "autoware_control_msgs/msg/detail/control_command__struct.h"

// Struct defined in msg/ControlCommandStamped in the package autoware_control_msgs.
typedef struct autoware_control_msgs__msg__ControlCommandStamped
{
  std_msgs__msg__Header header;
  autoware_control_msgs__msg__ControlCommand control;
} autoware_control_msgs__msg__ControlCommandStamped;

// Struct for a sequence of autoware_control_msgs__msg__ControlCommandStamped.
typedef struct autoware_control_msgs__msg__ControlCommandStamped__Sequence
{
  autoware_control_msgs__msg__ControlCommandStamped * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_control_msgs__msg__ControlCommandStamped__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__STRUCT_H_
