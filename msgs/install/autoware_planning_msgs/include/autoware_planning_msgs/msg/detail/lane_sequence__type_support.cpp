// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from autoware_planning_msgs:msg/LaneSequence.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "autoware_planning_msgs/msg/detail/lane_sequence__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace autoware_planning_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void LaneSequence_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) autoware_planning_msgs::msg::LaneSequence(_init);
}

void LaneSequence_fini_function(void * message_memory)
{
  auto typed_message = static_cast<autoware_planning_msgs::msg::LaneSequence *>(message_memory);
  typed_message->~LaneSequence();
}

size_t size_function__LaneSequence__lane_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int64_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__LaneSequence__lane_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int64_t> *>(untyped_member);
  return &member[index];
}

void * get_function__LaneSequence__lane_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int64_t> *>(untyped_member);
  return &member[index];
}

void resize_function__LaneSequence__lane_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int64_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember LaneSequence_message_member_array[1] = {
  {
    "lane_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(autoware_planning_msgs::msg::LaneSequence, lane_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__LaneSequence__lane_ids,  // size() function pointer
    get_const_function__LaneSequence__lane_ids,  // get_const(index) function pointer
    get_function__LaneSequence__lane_ids,  // get(index) function pointer
    resize_function__LaneSequence__lane_ids  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers LaneSequence_message_members = {
  "autoware_planning_msgs::msg",  // message namespace
  "LaneSequence",  // message name
  1,  // number of fields
  sizeof(autoware_planning_msgs::msg::LaneSequence),
  LaneSequence_message_member_array,  // message members
  LaneSequence_init_function,  // function to initialize message memory (memory has to be allocated)
  LaneSequence_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t LaneSequence_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &LaneSequence_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace autoware_planning_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<autoware_planning_msgs::msg::LaneSequence>()
{
  return &::autoware_planning_msgs::msg::rosidl_typesupport_introspection_cpp::LaneSequence_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, autoware_planning_msgs, msg, LaneSequence)() {
  return &::autoware_planning_msgs::msg::rosidl_typesupport_introspection_cpp::LaneSequence_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
