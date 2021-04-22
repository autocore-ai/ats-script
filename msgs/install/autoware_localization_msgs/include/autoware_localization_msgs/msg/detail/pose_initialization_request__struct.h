// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_localization_msgs:msg/PoseInitializationRequest.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__STRUCT_H_
#define AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

// Struct defined in msg/PoseInitializationRequest in the package autoware_localization_msgs.
typedef struct autoware_localization_msgs__msg__PoseInitializationRequest
{
  builtin_interfaces__msg__Time stamp;
  bool data;
} autoware_localization_msgs__msg__PoseInitializationRequest;

// Struct for a sequence of autoware_localization_msgs__msg__PoseInitializationRequest.
typedef struct autoware_localization_msgs__msg__PoseInitializationRequest__Sequence
{
  autoware_localization_msgs__msg__PoseInitializationRequest * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_localization_msgs__msg__PoseInitializationRequest__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__STRUCT_H_
