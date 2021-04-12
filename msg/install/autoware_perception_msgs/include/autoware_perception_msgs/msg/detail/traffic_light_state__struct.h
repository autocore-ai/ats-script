// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_H_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'lamp_states'
#include "autoware_perception_msgs/msg/detail/lamp_state__struct.h"

// Struct defined in msg/TrafficLightState in the package autoware_perception_msgs.
typedef struct autoware_perception_msgs__msg__TrafficLightState
{
  autoware_perception_msgs__msg__LampState__Sequence lamp_states;
  int32_t id;
} autoware_perception_msgs__msg__TrafficLightState;

// Struct for a sequence of autoware_perception_msgs__msg__TrafficLightState.
typedef struct autoware_perception_msgs__msg__TrafficLightState__Sequence
{
  autoware_perception_msgs__msg__TrafficLightState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_perception_msgs__msg__TrafficLightState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_H_
