// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_system_msgs:msg/TimeoutNotification.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__STRUCT_H_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__STRUCT_H_

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

// Struct defined in msg/TimeoutNotification in the package autoware_system_msgs.
typedef struct autoware_system_msgs__msg__TimeoutNotification
{
  builtin_interfaces__msg__Time stamp;
  bool is_timeout;
} autoware_system_msgs__msg__TimeoutNotification;

// Struct for a sequence of autoware_system_msgs__msg__TimeoutNotification.
typedef struct autoware_system_msgs__msg__TimeoutNotification__Sequence
{
  autoware_system_msgs__msg__TimeoutNotification * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_system_msgs__msg__TimeoutNotification__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__STRUCT_H_
