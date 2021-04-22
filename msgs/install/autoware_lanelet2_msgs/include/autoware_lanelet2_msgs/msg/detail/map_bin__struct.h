// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_lanelet2_msgs:msg/MapBin.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__STRUCT_H_
#define AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__STRUCT_H_

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
// Member 'format_version'
// Member 'map_version'
#include "rosidl_runtime_c/string.h"
// Member 'data'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in msg/MapBin in the package autoware_lanelet2_msgs.
typedef struct autoware_lanelet2_msgs__msg__MapBin
{
  std_msgs__msg__Header header;
  rosidl_runtime_c__String format_version;
  rosidl_runtime_c__String map_version;
  rosidl_runtime_c__int8__Sequence data;
} autoware_lanelet2_msgs__msg__MapBin;

// Struct for a sequence of autoware_lanelet2_msgs__msg__MapBin.
typedef struct autoware_lanelet2_msgs__msg__MapBin__Sequence
{
  autoware_lanelet2_msgs__msg__MapBin * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_lanelet2_msgs__msg__MapBin__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__STRUCT_H_
