// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_system_msgs:msg/DrivingCapability.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__STRUCT_H_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/DrivingCapability in the package autoware_system_msgs.
typedef struct autoware_system_msgs__msg__DrivingCapability
{
  bool manual_driving;
  bool autonomous_driving;
  bool remote_control;
  bool safe_stop;
  bool emergency_stop;
} autoware_system_msgs__msg__DrivingCapability;

// Struct for a sequence of autoware_system_msgs__msg__DrivingCapability.
typedef struct autoware_system_msgs__msg__DrivingCapability__Sequence
{
  autoware_system_msgs__msg__DrivingCapability * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_system_msgs__msg__DrivingCapability__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__STRUCT_H_
