// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_perception_msgs:msg/Semantic.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__STRUCT_H_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__STRUCT_H_

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
  autoware_perception_msgs__msg__Semantic__UNKNOWN = 0
};

/// Constant 'CAR'.
enum
{
  autoware_perception_msgs__msg__Semantic__CAR = 1
};

/// Constant 'TRUCK'.
enum
{
  autoware_perception_msgs__msg__Semantic__TRUCK = 2
};

/// Constant 'BUS'.
enum
{
  autoware_perception_msgs__msg__Semantic__BUS = 3
};

/// Constant 'BICYCLE'.
enum
{
  autoware_perception_msgs__msg__Semantic__BICYCLE = 4
};

/// Constant 'MOTORBIKE'.
enum
{
  autoware_perception_msgs__msg__Semantic__MOTORBIKE = 5
};

/// Constant 'PEDESTRIAN'.
enum
{
  autoware_perception_msgs__msg__Semantic__PEDESTRIAN = 6
};

/// Constant 'ANIMAL'.
enum
{
  autoware_perception_msgs__msg__Semantic__ANIMAL = 7
};

// Struct defined in msg/Semantic in the package autoware_perception_msgs.
typedef struct autoware_perception_msgs__msg__Semantic
{
  uint32_t type;
  double confidence;
} autoware_perception_msgs__msg__Semantic;

// Struct for a sequence of autoware_perception_msgs__msg__Semantic.
typedef struct autoware_perception_msgs__msg__Semantic__Sequence
{
  autoware_perception_msgs__msg__Semantic * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_perception_msgs__msg__Semantic__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__STRUCT_H_
