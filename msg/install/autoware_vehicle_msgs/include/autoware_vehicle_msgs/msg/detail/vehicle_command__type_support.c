// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from autoware_vehicle_msgs:msg/VehicleCommand.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "autoware_vehicle_msgs/msg/detail/vehicle_command__rosidl_typesupport_introspection_c.h"
#include "autoware_vehicle_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "autoware_vehicle_msgs/msg/detail/vehicle_command__functions.h"
#include "autoware_vehicle_msgs/msg/detail/vehicle_command__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `control`
#include "autoware_control_msgs/msg/control_command.h"
// Member `control`
#include "autoware_control_msgs/msg/detail/control_command__rosidl_typesupport_introspection_c.h"
// Member `shift`
#include "autoware_vehicle_msgs/msg/shift.h"
// Member `shift`
#include "autoware_vehicle_msgs/msg/detail/shift__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  autoware_vehicle_msgs__msg__VehicleCommand__init(message_memory);
}

void VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_fini_function(void * message_memory)
{
  autoware_vehicle_msgs__msg__VehicleCommand__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_member_array[4] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_vehicle_msgs__msg__VehicleCommand, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "control",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_vehicle_msgs__msg__VehicleCommand, control),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "shift",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_vehicle_msgs__msg__VehicleCommand, shift),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "emergency",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_vehicle_msgs__msg__VehicleCommand, emergency),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_members = {
  "autoware_vehicle_msgs__msg",  // message namespace
  "VehicleCommand",  // message name
  4,  // number of fields
  sizeof(autoware_vehicle_msgs__msg__VehicleCommand),
  VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_member_array,  // message members
  VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_init_function,  // function to initialize message memory (memory has to be allocated)
  VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_type_support_handle = {
  0,
  &VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autoware_vehicle_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_vehicle_msgs, msg, VehicleCommand)() {
  VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_control_msgs, msg, ControlCommand)();
  VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_vehicle_msgs, msg, Shift)();
  if (!VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_type_support_handle.typesupport_identifier) {
    VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &VehicleCommand__rosidl_typesupport_introspection_c__VehicleCommand_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
