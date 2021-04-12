// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from autoware_perception_msgs:msg/Semantic.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "autoware_perception_msgs/msg/detail/semantic__rosidl_typesupport_introspection_c.h"
#include "autoware_perception_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "autoware_perception_msgs/msg/detail/semantic__functions.h"
#include "autoware_perception_msgs/msg/detail/semantic__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void Semantic__rosidl_typesupport_introspection_c__Semantic_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  autoware_perception_msgs__msg__Semantic__init(message_memory);
}

void Semantic__rosidl_typesupport_introspection_c__Semantic_fini_function(void * message_memory)
{
  autoware_perception_msgs__msg__Semantic__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Semantic__rosidl_typesupport_introspection_c__Semantic_message_member_array[2] = {
  {
    "type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_perception_msgs__msg__Semantic, type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "confidence",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_perception_msgs__msg__Semantic, confidence),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Semantic__rosidl_typesupport_introspection_c__Semantic_message_members = {
  "autoware_perception_msgs__msg",  // message namespace
  "Semantic",  // message name
  2,  // number of fields
  sizeof(autoware_perception_msgs__msg__Semantic),
  Semantic__rosidl_typesupport_introspection_c__Semantic_message_member_array,  // message members
  Semantic__rosidl_typesupport_introspection_c__Semantic_init_function,  // function to initialize message memory (memory has to be allocated)
  Semantic__rosidl_typesupport_introspection_c__Semantic_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Semantic__rosidl_typesupport_introspection_c__Semantic_message_type_support_handle = {
  0,
  &Semantic__rosidl_typesupport_introspection_c__Semantic_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autoware_perception_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_perception_msgs, msg, Semantic)() {
  if (!Semantic__rosidl_typesupport_introspection_c__Semantic_message_type_support_handle.typesupport_identifier) {
    Semantic__rosidl_typesupport_introspection_c__Semantic_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Semantic__rosidl_typesupport_introspection_c__Semantic_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
