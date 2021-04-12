// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_vehicle_msgs:msg/RawControlCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__STRUCT_H_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/RawControlCommand in the package autoware_vehicle_msgs.
typedef struct autoware_vehicle_msgs__msg__RawControlCommand
{
  double steering_angle;
  double steering_angle_velocity;
  double throttle;
  double brake;
} autoware_vehicle_msgs__msg__RawControlCommand;

// Struct for a sequence of autoware_vehicle_msgs__msg__RawControlCommand.
typedef struct autoware_vehicle_msgs__msg__RawControlCommand__Sequence
{
  autoware_vehicle_msgs__msg__RawControlCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_vehicle_msgs__msg__RawControlCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__STRUCT_H_
