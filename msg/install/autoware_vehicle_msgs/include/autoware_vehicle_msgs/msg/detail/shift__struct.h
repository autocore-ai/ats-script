// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_vehicle_msgs:msg/Shift.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT__STRUCT_H_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'NONE'.
enum
{
  autoware_vehicle_msgs__msg__Shift__NONE = 0
};

/// Constant 'PARKING'.
enum
{
  autoware_vehicle_msgs__msg__Shift__PARKING = 1
};

/// Constant 'REVERSE'.
enum
{
  autoware_vehicle_msgs__msg__Shift__REVERSE = 2
};

/// Constant 'NEUTRAL'.
enum
{
  autoware_vehicle_msgs__msg__Shift__NEUTRAL = 3
};

/// Constant 'DRIVE'.
enum
{
  autoware_vehicle_msgs__msg__Shift__DRIVE = 4
};

/// Constant 'LOW'.
enum
{
  autoware_vehicle_msgs__msg__Shift__LOW = 5
};

// Struct defined in msg/Shift in the package autoware_vehicle_msgs.
typedef struct autoware_vehicle_msgs__msg__Shift
{
  int32_t data;
} autoware_vehicle_msgs__msg__Shift;

// Struct for a sequence of autoware_vehicle_msgs__msg__Shift.
typedef struct autoware_vehicle_msgs__msg__Shift__Sequence
{
  autoware_vehicle_msgs__msg__Shift * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_vehicle_msgs__msg__Shift__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT__STRUCT_H_
