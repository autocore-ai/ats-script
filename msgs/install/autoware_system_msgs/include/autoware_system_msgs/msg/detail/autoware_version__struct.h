// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_system_msgs:msg/AutowareVersion.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__STRUCT_H_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'ROS_VERSION_1'.
enum
{
  autoware_system_msgs__msg__AutowareVersion__ROS_VERSION_1 = 1ul
};

/// Constant 'ROS_VERSION_2'.
enum
{
  autoware_system_msgs__msg__AutowareVersion__ROS_VERSION_2 = 2ul
};

/// Constant 'ROS_DISTRO_MELODIC'.
static const char * const autoware_system_msgs__msg__AutowareVersion__ROS_DISTRO_MELODIC = "melodic";

/// Constant 'ROS_DISTRO_NOETIC'.
static const char * const autoware_system_msgs__msg__AutowareVersion__ROS_DISTRO_NOETIC = "noetic";

/// Constant 'ROS_DISTRO_FOXY'.
static const char * const autoware_system_msgs__msg__AutowareVersion__ROS_DISTRO_FOXY = "foxy";

// Include directives for member types
// Member 'ros_distro'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/AutowareVersion in the package autoware_system_msgs.
typedef struct autoware_system_msgs__msg__AutowareVersion
{
  uint32_t ros_version;
  rosidl_runtime_c__String ros_distro;
} autoware_system_msgs__msg__AutowareVersion;

// Struct for a sequence of autoware_system_msgs__msg__AutowareVersion.
typedef struct autoware_system_msgs__msg__AutowareVersion__Sequence
{
  autoware_system_msgs__msg__AutowareVersion * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_system_msgs__msg__AutowareVersion__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__STRUCT_H_
