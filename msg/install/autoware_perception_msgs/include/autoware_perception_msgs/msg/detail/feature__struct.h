// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_perception_msgs:msg/Feature.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__FEATURE__STRUCT_H_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__FEATURE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'cluster'
#include "sensor_msgs/msg/detail/point_cloud2__struct.h"
// Member 'roi'
#include "sensor_msgs/msg/detail/region_of_interest__struct.h"

// Struct defined in msg/Feature in the package autoware_perception_msgs.
typedef struct autoware_perception_msgs__msg__Feature
{
  sensor_msgs__msg__PointCloud2 cluster;
  sensor_msgs__msg__RegionOfInterest roi;
} autoware_perception_msgs__msg__Feature;

// Struct for a sequence of autoware_perception_msgs__msg__Feature.
typedef struct autoware_perception_msgs__msg__Feature__Sequence
{
  autoware_perception_msgs__msg__Feature * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_perception_msgs__msg__Feature__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__FEATURE__STRUCT_H_
