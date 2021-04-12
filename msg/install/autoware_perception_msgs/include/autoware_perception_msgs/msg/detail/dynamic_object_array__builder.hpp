// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/DynamicObjectArray.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_ARRAY__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_ARRAY__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/dynamic_object_array__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_DynamicObjectArray_objects
{
public:
  explicit Init_DynamicObjectArray_objects(::autoware_perception_msgs::msg::DynamicObjectArray & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::DynamicObjectArray objects(::autoware_perception_msgs::msg::DynamicObjectArray::_objects_type arg)
  {
    msg_.objects = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::DynamicObjectArray msg_;
};

class Init_DynamicObjectArray_header
{
public:
  Init_DynamicObjectArray_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DynamicObjectArray_objects header(::autoware_perception_msgs::msg::DynamicObjectArray::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_DynamicObjectArray_objects(msg_);
  }

private:
  ::autoware_perception_msgs::msg::DynamicObjectArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::DynamicObjectArray>()
{
  return autoware_perception_msgs::msg::builder::Init_DynamicObjectArray_header();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_ARRAY__BUILDER_HPP_
