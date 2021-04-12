// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_control_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_

#include "autoware_control_msgs/msg/detail/control_command__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_control_msgs
{

namespace msg
{

namespace builder
{

class Init_ControlCommand_acceleration
{
public:
  explicit Init_ControlCommand_acceleration(::autoware_control_msgs::msg::ControlCommand & msg)
  : msg_(msg)
  {}
  ::autoware_control_msgs::msg::ControlCommand acceleration(::autoware_control_msgs::msg::ControlCommand::_acceleration_type arg)
  {
    msg_.acceleration = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_control_msgs::msg::ControlCommand msg_;
};

class Init_ControlCommand_velocity
{
public:
  explicit Init_ControlCommand_velocity(::autoware_control_msgs::msg::ControlCommand & msg)
  : msg_(msg)
  {}
  Init_ControlCommand_acceleration velocity(::autoware_control_msgs::msg::ControlCommand::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return Init_ControlCommand_acceleration(msg_);
  }

private:
  ::autoware_control_msgs::msg::ControlCommand msg_;
};

class Init_ControlCommand_steering_angle_velocity
{
public:
  explicit Init_ControlCommand_steering_angle_velocity(::autoware_control_msgs::msg::ControlCommand & msg)
  : msg_(msg)
  {}
  Init_ControlCommand_velocity steering_angle_velocity(::autoware_control_msgs::msg::ControlCommand::_steering_angle_velocity_type arg)
  {
    msg_.steering_angle_velocity = std::move(arg);
    return Init_ControlCommand_velocity(msg_);
  }

private:
  ::autoware_control_msgs::msg::ControlCommand msg_;
};

class Init_ControlCommand_steering_angle
{
public:
  Init_ControlCommand_steering_angle()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlCommand_steering_angle_velocity steering_angle(::autoware_control_msgs::msg::ControlCommand::_steering_angle_type arg)
  {
    msg_.steering_angle = std::move(arg);
    return Init_ControlCommand_steering_angle_velocity(msg_);
  }

private:
  ::autoware_control_msgs::msg::ControlCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_control_msgs::msg::ControlCommand>()
{
  return autoware_control_msgs::msg::builder::Init_ControlCommand_steering_angle();
}

}  // namespace autoware_control_msgs

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_
