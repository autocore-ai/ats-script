// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_vehicle_msgs:msg/RawControlCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__BUILDER_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__BUILDER_HPP_

#include "autoware_vehicle_msgs/msg/detail/raw_control_command__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_vehicle_msgs
{

namespace msg
{

namespace builder
{

class Init_RawControlCommand_brake
{
public:
  explicit Init_RawControlCommand_brake(::autoware_vehicle_msgs::msg::RawControlCommand & msg)
  : msg_(msg)
  {}
  ::autoware_vehicle_msgs::msg::RawControlCommand brake(::autoware_vehicle_msgs::msg::RawControlCommand::_brake_type arg)
  {
    msg_.brake = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawControlCommand msg_;
};

class Init_RawControlCommand_throttle
{
public:
  explicit Init_RawControlCommand_throttle(::autoware_vehicle_msgs::msg::RawControlCommand & msg)
  : msg_(msg)
  {}
  Init_RawControlCommand_brake throttle(::autoware_vehicle_msgs::msg::RawControlCommand::_throttle_type arg)
  {
    msg_.throttle = std::move(arg);
    return Init_RawControlCommand_brake(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawControlCommand msg_;
};

class Init_RawControlCommand_steering_angle_velocity
{
public:
  explicit Init_RawControlCommand_steering_angle_velocity(::autoware_vehicle_msgs::msg::RawControlCommand & msg)
  : msg_(msg)
  {}
  Init_RawControlCommand_throttle steering_angle_velocity(::autoware_vehicle_msgs::msg::RawControlCommand::_steering_angle_velocity_type arg)
  {
    msg_.steering_angle_velocity = std::move(arg);
    return Init_RawControlCommand_throttle(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawControlCommand msg_;
};

class Init_RawControlCommand_steering_angle
{
public:
  Init_RawControlCommand_steering_angle()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RawControlCommand_steering_angle_velocity steering_angle(::autoware_vehicle_msgs::msg::RawControlCommand::_steering_angle_type arg)
  {
    msg_.steering_angle = std::move(arg);
    return Init_RawControlCommand_steering_angle_velocity(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawControlCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_vehicle_msgs::msg::RawControlCommand>()
{
  return autoware_vehicle_msgs::msg::builder::Init_RawControlCommand_steering_angle();
}

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__BUILDER_HPP_
