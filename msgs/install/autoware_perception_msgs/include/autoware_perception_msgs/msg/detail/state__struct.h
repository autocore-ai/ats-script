// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_perception_msgs:msg/State.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__STATE__STRUCT_H_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'pose_covariance'
#include "geometry_msgs/msg/detail/pose_with_covariance__struct.h"
// Member 'twist_covariance'
#include "geometry_msgs/msg/detail/twist_with_covariance__struct.h"
// Member 'acceleration_covariance'
#include "geometry_msgs/msg/detail/accel_with_covariance__struct.h"
// Member 'predicted_paths'
#include "autoware_perception_msgs/msg/detail/predicted_path__struct.h"

// Struct defined in msg/State in the package autoware_perception_msgs.
typedef struct autoware_perception_msgs__msg__State
{
  geometry_msgs__msg__PoseWithCovariance pose_covariance;
  bool orientation_reliable;
  geometry_msgs__msg__TwistWithCovariance twist_covariance;
  bool twist_reliable;
  geometry_msgs__msg__AccelWithCovariance acceleration_covariance;
  bool acceleration_reliable;
  autoware_perception_msgs__msg__PredictedPath__Sequence predicted_paths;
} autoware_perception_msgs__msg__State;

// Struct for a sequence of autoware_perception_msgs__msg__State.
typedef struct autoware_perception_msgs__msg__State__Sequence
{
  autoware_perception_msgs__msg__State * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_perception_msgs__msg__State__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__STATE__STRUCT_H_
