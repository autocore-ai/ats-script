// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_control_msgs:msg/EmergencyMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__EMERGENCY_MODE__BUILDER_HPP_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__EMERGENCY_MODE__BUILDER_HPP_

#include "autoware_control_msgs/msg/detail/emergency_mode__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_control_msgs
{

namespace msg
{

namespace builder
{

class Init_EmergencyMode_is_emergency
{
public:
  Init_EmergencyMode_is_emergency()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::autoware_control_msgs::msg::EmergencyMode is_emergency(::autoware_control_msgs::msg::EmergencyMode::_is_emergency_type arg)
  {
    msg_.is_emergency = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_control_msgs::msg::EmergencyMode msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_control_msgs::msg::EmergencyMode>()
{
  return autoware_control_msgs::msg::builder::Init_EmergencyMode_is_emergency();
}

}  // namespace autoware_control_msgs

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__EMERGENCY_MODE__BUILDER_HPP_
