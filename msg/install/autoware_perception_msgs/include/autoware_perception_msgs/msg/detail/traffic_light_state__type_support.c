// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from autoware_perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "autoware_perception_msgs/msg/detail/traffic_light_state__rosidl_typesupport_introspection_c.h"
#include "autoware_perception_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "autoware_perception_msgs/msg/detail/traffic_light_state__functions.h"
#include "autoware_perception_msgs/msg/detail/traffic_light_state__struct.h"


// Include directives for member types
// Member `lamp_states`
#include "autoware_perception_msgs/msg/lamp_state.h"
// Member `lamp_states`
#include "autoware_perception_msgs/msg/detail/lamp_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  autoware_perception_msgs__msg__TrafficLightState__init(message_memory);
}

void TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_fini_function(void * message_memory)
{
  autoware_perception_msgs__msg__TrafficLightState__fini(message_memory);
}

size_t TrafficLightState__rosidl_typesupport_introspection_c__size_function__LampState__lamp_states(
  const void * untyped_member)
{
  const autoware_perception_msgs__msg__LampState__Sequence * member =
    (const autoware_perception_msgs__msg__LampState__Sequence *)(untyped_member);
  return member->size;
}

const void * TrafficLightState__rosidl_typesupport_introspection_c__get_const_function__LampState__lamp_states(
  const void * untyped_member, size_t index)
{
  const autoware_perception_msgs__msg__LampState__Sequence * member =
    (const autoware_perception_msgs__msg__LampState__Sequence *)(untyped_member);
  return &member->data[index];
}

void * TrafficLightState__rosidl_typesupport_introspection_c__get_function__LampState__lamp_states(
  void * untyped_member, size_t index)
{
  autoware_perception_msgs__msg__LampState__Sequence * member =
    (autoware_perception_msgs__msg__LampState__Sequence *)(untyped_member);
  return &member->data[index];
}

bool TrafficLightState__rosidl_typesupport_introspection_c__resize_function__LampState__lamp_states(
  void * untyped_member, size_t size)
{
  autoware_perception_msgs__msg__LampState__Sequence * member =
    (autoware_perception_msgs__msg__LampState__Sequence *)(untyped_member);
  autoware_perception_msgs__msg__LampState__Sequence__fini(member);
  return autoware_perception_msgs__msg__LampState__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_member_array[2] = {
  {
    "lamp_states",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_perception_msgs__msg__TrafficLightState, lamp_states),  // bytes offset in struct
    NULL,  // default value
    TrafficLightState__rosidl_typesupport_introspection_c__size_function__LampState__lamp_states,  // size() function pointer
    TrafficLightState__rosidl_typesupport_introspection_c__get_const_function__LampState__lamp_states,  // get_const(index) function pointer
    TrafficLightState__rosidl_typesupport_introspection_c__get_function__LampState__lamp_states,  // get(index) function pointer
    TrafficLightState__rosidl_typesupport_introspection_c__resize_function__LampState__lamp_states  // resize(index) function pointer
  },
  {
    "id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_perception_msgs__msg__TrafficLightState, id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_members = {
  "autoware_perception_msgs__msg",  // message namespace
  "TrafficLightState",  // message name
  2,  // number of fields
  sizeof(autoware_perception_msgs__msg__TrafficLightState),
  TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_member_array,  // message members
  TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_init_function,  // function to initialize message memory (memory has to be allocated)
  TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_type_support_handle = {
  0,
  &TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autoware_perception_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_perception_msgs, msg, TrafficLightState)() {
  TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_perception_msgs, msg, LampState)();
  if (!TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_type_support_handle.typesupport_identifier) {
    TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TrafficLightState__rosidl_typesupport_introspection_c__TrafficLightState_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
