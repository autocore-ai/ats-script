// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_perception_msgs:msg/LampState.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__STRUCT_H_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'UNKNOWN'.
enum
{
  autoware_perception_msgs__msg__LampState__UNKNOWN = 0
};

/// Constant 'RED'.
enum
{
  autoware_perception_msgs__msg__LampState__RED = 1
};

/// Constant 'GREEN'.
enum
{
  autoware_perception_msgs__msg__LampState__GREEN = 2
};

/// Constant 'YELLOW'.
enum
{
  autoware_perception_msgs__msg__LampState__YELLOW = 3
};

/// Constant 'LEFT'.
enum
{
  autoware_perception_msgs__msg__LampState__LEFT = 4
};

/// Constant 'RIGHT'.
enum
{
  autoware_perception_msgs__msg__LampState__RIGHT = 5
};

/// Constant 'UP'.
enum
{
  autoware_perception_msgs__msg__LampState__UP = 6
};

/// Constant 'DOWN'.
enum
{
  autoware_perception_msgs__msg__LampState__DOWN = 7
};

// Struct defined in msg/LampState in the package autoware_perception_msgs.
typedef struct autoware_perception_msgs__msg__LampState
{
  uint32_t type;
  float confidence;
} autoware_perception_msgs__msg__LampState;

// Struct for a sequence of autoware_perception_msgs__msg__LampState.
typedef struct autoware_perception_msgs__msg__LampState__Sequence
{
  autoware_perception_msgs__msg__LampState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_perception_msgs__msg__LampState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__STRUCT_H_
