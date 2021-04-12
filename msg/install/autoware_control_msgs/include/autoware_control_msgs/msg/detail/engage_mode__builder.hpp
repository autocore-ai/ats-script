// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_control_msgs:msg/EngageMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__BUILDER_HPP_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__BUILDER_HPP_

#include "autoware_control_msgs/msg/detail/engage_mode__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_control_msgs
{

namespace msg
{

namespace builder
{

class Init_EngageMode_is_engaged
{
public:
  Init_EngageMode_is_engaged()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::autoware_control_msgs::msg::EngageMode is_engaged(::autoware_control_msgs::msg::EngageMode::_is_engaged_type arg)
  {
    msg_.is_engaged = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_control_msgs::msg::EngageMode msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_control_msgs::msg::EngageMode>()
{
  return autoware_control_msgs::msg::builder::Init_EngageMode_is_engaged();
}

}  // namespace autoware_control_msgs

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__BUILDER_HPP_
