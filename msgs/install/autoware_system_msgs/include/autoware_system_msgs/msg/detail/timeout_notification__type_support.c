// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from autoware_system_msgs:msg/TimeoutNotification.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "autoware_system_msgs/msg/detail/timeout_notification__rosidl_typesupport_introspection_c.h"
#include "autoware_system_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "autoware_system_msgs/msg/detail/timeout_notification__functions.h"
#include "autoware_system_msgs/msg/detail/timeout_notification__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  autoware_system_msgs__msg__TimeoutNotification__init(message_memory);
}

void TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_fini_function(void * message_memory)
{
  autoware_system_msgs__msg__TimeoutNotification__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_member_array[2] = {
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_system_msgs__msg__TimeoutNotification, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "is_timeout",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_system_msgs__msg__TimeoutNotification, is_timeout),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_members = {
  "autoware_system_msgs__msg",  // message namespace
  "TimeoutNotification",  // message name
  2,  // number of fields
  sizeof(autoware_system_msgs__msg__TimeoutNotification),
  TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_member_array,  // message members
  TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_init_function,  // function to initialize message memory (memory has to be allocated)
  TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_type_support_handle = {
  0,
  &TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autoware_system_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_system_msgs, msg, TimeoutNotification)() {
  TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_type_support_handle.typesupport_identifier) {
    TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TimeoutNotification__rosidl_typesupport_introspection_c__TimeoutNotification_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
