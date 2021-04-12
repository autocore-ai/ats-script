// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_control_msgs:msg/ControlCommandStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__BUILDER_HPP_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__BUILDER_HPP_

#include "autoware_control_msgs/msg/detail/control_command_stamped__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_control_msgs
{

namespace msg
{

namespace builder
{

class Init_ControlCommandStamped_control
{
public:
  explicit Init_ControlCommandStamped_control(::autoware_control_msgs::msg::ControlCommandStamped & msg)
  : msg_(msg)
  {}
  ::autoware_control_msgs::msg::ControlCommandStamped control(::autoware_control_msgs::msg::ControlCommandStamped::_control_type arg)
  {
    msg_.control = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_control_msgs::msg::ControlCommandStamped msg_;
};

class Init_ControlCommandStamped_header
{
public:
  Init_ControlCommandStamped_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlCommandStamped_control header(::autoware_control_msgs::msg::ControlCommandStamped::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ControlCommandStamped_control(msg_);
  }

private:
  ::autoware_control_msgs::msg::ControlCommandStamped msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_control_msgs::msg::ControlCommandStamped>()
{
  return autoware_control_msgs::msg::builder::Init_ControlCommandStamped_header();
}

}  // namespace autoware_control_msgs

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__BUILDER_HPP_
