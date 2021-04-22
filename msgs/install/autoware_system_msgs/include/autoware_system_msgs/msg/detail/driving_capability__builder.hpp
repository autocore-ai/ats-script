// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_system_msgs:msg/DrivingCapability.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__BUILDER_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__BUILDER_HPP_

#include "autoware_system_msgs/msg/detail/driving_capability__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_system_msgs
{

namespace msg
{

namespace builder
{

class Init_DrivingCapability_remote_control
{
public:
  explicit Init_DrivingCapability_remote_control(::autoware_system_msgs::msg::DrivingCapability & msg)
  : msg_(msg)
  {}
  ::autoware_system_msgs::msg::DrivingCapability remote_control(::autoware_system_msgs::msg::DrivingCapability::_remote_control_type arg)
  {
    msg_.remote_control = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_system_msgs::msg::DrivingCapability msg_;
};

class Init_DrivingCapability_autonomous_driving
{
public:
  explicit Init_DrivingCapability_autonomous_driving(::autoware_system_msgs::msg::DrivingCapability & msg)
  : msg_(msg)
  {}
  Init_DrivingCapability_remote_control autonomous_driving(::autoware_system_msgs::msg::DrivingCapability::_autonomous_driving_type arg)
  {
    msg_.autonomous_driving = std::move(arg);
    return Init_DrivingCapability_remote_control(msg_);
  }

private:
  ::autoware_system_msgs::msg::DrivingCapability msg_;
};

class Init_DrivingCapability_header
{
public:
  Init_DrivingCapability_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DrivingCapability_autonomous_driving header(::autoware_system_msgs::msg::DrivingCapability::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_DrivingCapability_autonomous_driving(msg_);
  }

private:
  ::autoware_system_msgs::msg::DrivingCapability msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_system_msgs::msg::DrivingCapability>()
{
  return autoware_system_msgs::msg::builder::Init_DrivingCapability_header();
}

}  // namespace autoware_system_msgs

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__BUILDER_HPP_
