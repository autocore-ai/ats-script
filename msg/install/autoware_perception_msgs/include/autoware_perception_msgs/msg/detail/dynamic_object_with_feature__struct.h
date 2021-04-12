// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeature.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__STRUCT_H_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'object'
#include "autoware_perception_msgs/msg/detail/dynamic_object__struct.h"
// Member 'feature'
#include "autoware_perception_msgs/msg/detail/feature__struct.h"

// Struct defined in msg/DynamicObjectWithFeature in the package autoware_perception_msgs.
typedef struct autoware_perception_msgs__msg__DynamicObjectWithFeature
{
  autoware_perception_msgs__msg__DynamicObject object;
  autoware_perception_msgs__msg__Feature feature;
} autoware_perception_msgs__msg__DynamicObjectWithFeature;

// Struct for a sequence of autoware_perception_msgs__msg__DynamicObjectWithFeature.
typedef struct autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence
{
  autoware_perception_msgs__msg__DynamicObjectWithFeature * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__STRUCT_H_
