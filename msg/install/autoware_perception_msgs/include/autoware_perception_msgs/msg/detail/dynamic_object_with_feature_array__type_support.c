// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeatureArray.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature_array__rosidl_typesupport_introspection_c.h"
#include "autoware_perception_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature_array__functions.h"
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature_array__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `feature_objects`
#include "autoware_perception_msgs/msg/dynamic_object_with_feature.h"
// Member `feature_objects`
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__init(message_memory);
}

void DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_fini_function(void * message_memory)
{
  autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__fini(message_memory);
}

size_t DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__size_function__DynamicObjectWithFeature__feature_objects(
  const void * untyped_member)
{
  const autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * member =
    (const autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence *)(untyped_member);
  return member->size;
}

const void * DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__get_const_function__DynamicObjectWithFeature__feature_objects(
  const void * untyped_member, size_t index)
{
  const autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * member =
    (const autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence *)(untyped_member);
  return &member->data[index];
}

void * DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__get_function__DynamicObjectWithFeature__feature_objects(
  void * untyped_member, size_t index)
{
  autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * member =
    (autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence *)(untyped_member);
  return &member->data[index];
}

bool DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__resize_function__DynamicObjectWithFeature__feature_objects(
  void * untyped_member, size_t size)
{
  autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * member =
    (autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence *)(untyped_member);
  autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__fini(member);
  return autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_member_array[2] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "feature_objects",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray, feature_objects),  // bytes offset in struct
    NULL,  // default value
    DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__size_function__DynamicObjectWithFeature__feature_objects,  // size() function pointer
    DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__get_const_function__DynamicObjectWithFeature__feature_objects,  // get_const(index) function pointer
    DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__get_function__DynamicObjectWithFeature__feature_objects,  // get(index) function pointer
    DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__resize_function__DynamicObjectWithFeature__feature_objects  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_members = {
  "autoware_perception_msgs__msg",  // message namespace
  "DynamicObjectWithFeatureArray",  // message name
  2,  // number of fields
  sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray),
  DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_member_array,  // message members
  DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_init_function,  // function to initialize message memory (memory has to be allocated)
  DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_type_support_handle = {
  0,
  &DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_autoware_perception_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_perception_msgs, msg, DynamicObjectWithFeatureArray)() {
  DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, autoware_perception_msgs, msg, DynamicObjectWithFeature)();
  if (!DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_type_support_handle.typesupport_identifier) {
    DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &DynamicObjectWithFeatureArray__rosidl_typesupport_introspection_c__DynamicObjectWithFeatureArray_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
