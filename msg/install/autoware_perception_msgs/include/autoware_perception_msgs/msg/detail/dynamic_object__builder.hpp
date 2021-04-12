// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/DynamicObject.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/dynamic_object__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_DynamicObject_shape
{
public:
  explicit Init_DynamicObject_shape(::autoware_perception_msgs::msg::DynamicObject & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::DynamicObject shape(::autoware_perception_msgs::msg::DynamicObject::_shape_type arg)
  {
    msg_.shape = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::DynamicObject msg_;
};

class Init_DynamicObject_state
{
public:
  explicit Init_DynamicObject_state(::autoware_perception_msgs::msg::DynamicObject & msg)
  : msg_(msg)
  {}
  Init_DynamicObject_shape state(::autoware_perception_msgs::msg::DynamicObject::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_DynamicObject_shape(msg_);
  }

private:
  ::autoware_perception_msgs::msg::DynamicObject msg_;
};

class Init_DynamicObject_semantic
{
public:
  explicit Init_DynamicObject_semantic(::autoware_perception_msgs::msg::DynamicObject & msg)
  : msg_(msg)
  {}
  Init_DynamicObject_state semantic(::autoware_perception_msgs::msg::DynamicObject::_semantic_type arg)
  {
    msg_.semantic = std::move(arg);
    return Init_DynamicObject_state(msg_);
  }

private:
  ::autoware_perception_msgs::msg::DynamicObject msg_;
};

class Init_DynamicObject_id
{
public:
  Init_DynamicObject_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DynamicObject_semantic id(::autoware_perception_msgs::msg::DynamicObject::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_DynamicObject_semantic(msg_);
  }

private:
  ::autoware_perception_msgs::msg::DynamicObject msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::DynamicObject>()
{
  return autoware_perception_msgs::msg::builder::Init_DynamicObject_id();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT__BUILDER_HPP_
