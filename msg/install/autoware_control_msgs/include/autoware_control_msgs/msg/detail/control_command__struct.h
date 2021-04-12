// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_control_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ControlCommand in the package autoware_control_msgs.
typedef struct autoware_control_msgs__msg__ControlCommand
{
  double steering_angle;
  double steering_angle_velocity;
  double velocity;
  double acceleration;
} autoware_control_msgs__msg__ControlCommand;

// Struct for a sequence of autoware_control_msgs__msg__ControlCommand.
typedef struct autoware_control_msgs__msg__ControlCommand__Sequence
{
  autoware_control_msgs__msg__ControlCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_control_msgs__msg__ControlCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_
