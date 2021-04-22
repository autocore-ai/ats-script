// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_vehicle_msgs:msg/RawVehicleCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_VEHICLE_COMMAND__STRUCT_H_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_VEHICLE_COMMAND__STRUCT_H_

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
#include "autoware_vehicle_msgs/msg/detail/raw_control_command__struct.h"
// Member 'shift'
#include "autoware_vehicle_msgs/msg/detail/shift__struct.h"

// Struct defined in msg/RawVehicleCommand in the package autoware_vehicle_msgs.
typedef struct autoware_vehicle_msgs__msg__RawVehicleCommand
{
  std_msgs__msg__Header header;
  autoware_vehicle_msgs__msg__RawControlCommand control;
  autoware_vehicle_msgs__msg__Shift shift;
  int32_t emergency;
} autoware_vehicle_msgs__msg__RawVehicleCommand;

// Struct for a sequence of autoware_vehicle_msgs__msg__RawVehicleCommand.
typedef struct autoware_vehicle_msgs__msg__RawVehicleCommand__Sequence
{
  autoware_vehicle_msgs__msg__RawVehicleCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_vehicle_msgs__msg__RawVehicleCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_VEHICLE_COMMAND__STRUCT_H_
