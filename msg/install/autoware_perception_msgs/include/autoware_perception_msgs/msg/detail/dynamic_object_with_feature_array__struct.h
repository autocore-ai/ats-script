// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeatureArray.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__STRUCT_H_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__STRUCT_H_

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
// Member 'feature_objects'
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__struct.h"

// Struct defined in msg/DynamicObjectWithFeatureArray in the package autoware_perception_msgs.
typedef struct autoware_perception_msgs__msg__DynamicObjectWithFeatureArray
{
  std_msgs__msg__Header header;
  autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence feature_objects;
} autoware_perception_msgs__msg__DynamicObjectWithFeatureArray;

// Struct for a sequence of autoware_perception_msgs__msg__DynamicObjectWithFeatureArray.
typedef struct autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence
{
  autoware_perception_msgs__msg__DynamicObjectWithFeatureArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__STRUCT_H_
