// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_system_msgs:msg/HazardStatusStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS_STAMPED__STRUCT_H_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS_STAMPED__STRUCT_H_

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
// Member 'status'
#include "autoware_system_msgs/msg/detail/hazard_status__struct.h"

// Struct defined in msg/HazardStatusStamped in the package autoware_system_msgs.
typedef struct autoware_system_msgs__msg__HazardStatusStamped
{
  std_msgs__msg__Header header;
  autoware_system_msgs__msg__HazardStatus status;
} autoware_system_msgs__msg__HazardStatusStamped;

// Struct for a sequence of autoware_system_msgs__msg__HazardStatusStamped.
typedef struct autoware_system_msgs__msg__HazardStatusStamped__Sequence
{
  autoware_system_msgs__msg__HazardStatusStamped * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_system_msgs__msg__HazardStatusStamped__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS_STAMPED__STRUCT_H_
