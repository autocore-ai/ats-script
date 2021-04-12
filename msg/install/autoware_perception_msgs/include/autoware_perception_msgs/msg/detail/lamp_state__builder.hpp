// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/LampState.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/lamp_state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_LampState_confidence
{
public:
  explicit Init_LampState_confidence(::autoware_perception_msgs::msg::LampState & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::LampState confidence(::autoware_perception_msgs::msg::LampState::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::LampState msg_;
};

class Init_LampState_type
{
public:
  Init_LampState_type()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LampState_confidence type(::autoware_perception_msgs::msg::LampState::_type_type arg)
  {
    msg_.type = std::move(arg);
    return Init_LampState_confidence(msg_);
  }

private:
  ::autoware_perception_msgs::msg::LampState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::LampState>()
{
  return autoware_perception_msgs::msg::builder::Init_LampState_type();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__BUILDER_HPP_
