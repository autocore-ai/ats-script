// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from autoware_perception_msgs:msg/TrafficLightStateStamped.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "autoware_perception_msgs/msg/detail/traffic_light_state_stamped__rosidl_typesupport_introspection_c.h"
#include "autoware_perception_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "autoware_perception_msgs/msg/detail/traffic_light_state_stamped__functions.h"
#include "autoware_perception_msgs/msg/detail/traffic_light_state_stamped__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `state`
#include "autoware_perception_msgs/msg/traffic_light_state.h"
// Member `state`
#include "autoware_perception_msgs/msg/detail/traffic_light_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  autoware_perception_msgs__msg__TrafficLightStateStamped__init(message_memory);
}

void TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_fini_function(void * message_memory)
{
  autoware_perception_msgs__msg__TrafficLightStateStamped__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_member_array[2] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_perception_msgs__msg__TrafficLightStateStamped, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_perception_msgs__msg__TrafficLightStateStamped, state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_members = {
  "autoware_perception_msgs__msg",  // message namespace
  "TrafficLightStateStamped",  // message name
  2,  // number of fields
  sizeof(autoware_perception_msgs__msg__TrafficLightStateStamped),
  TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_member_array,  // message members
  TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_init_function,  // function to initialize message memory (memory has to be allocated)
  TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_type_support_handle = {
  0,
  &TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autoware_perception_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_perception_msgs, msg, TrafficLightStateStamped)() {
  TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_perception_msgs, msg, TrafficLightState)();
  if (!TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_type_support_handle.typesupport_identifier) {
    TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TrafficLightStateStamped__rosidl_typesupport_introspection_c__TrafficLightStateStamped_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
