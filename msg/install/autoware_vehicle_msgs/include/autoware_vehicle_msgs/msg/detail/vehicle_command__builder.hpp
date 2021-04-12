// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_vehicle_msgs:msg/VehicleCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__VEHICLE_COMMAND__BUILDER_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__VEHICLE_COMMAND__BUILDER_HPP_

#include "autoware_vehicle_msgs/msg/detail/vehicle_command__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_vehicle_msgs
{

namespace msg
{

namespace builder
{

class Init_VehicleCommand_emergency
{
public:
  explicit Init_VehicleCommand_emergency(::autoware_vehicle_msgs::msg::VehicleCommand & msg)
  : msg_(msg)
  {}
  ::autoware_vehicle_msgs::msg::VehicleCommand emergency(::autoware_vehicle_msgs::msg::VehicleCommand::_emergency_type arg)
  {
    msg_.emergency = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::VehicleCommand msg_;
};

class Init_VehicleCommand_shift
{
public:
  explicit Init_VehicleCommand_shift(::autoware_vehicle_msgs::msg::VehicleCommand & msg)
  : msg_(msg)
  {}
  Init_VehicleCommand_emergency shift(::autoware_vehicle_msgs::msg::VehicleCommand::_shift_type arg)
  {
    msg_.shift = std::move(arg);
    return Init_VehicleCommand_emergency(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::VehicleCommand msg_;
};

class Init_VehicleCommand_control
{
public:
  explicit Init_VehicleCommand_control(::autoware_vehicle_msgs::msg::VehicleCommand & msg)
  : msg_(msg)
  {}
  Init_VehicleCommand_shift control(::autoware_vehicle_msgs::msg::VehicleCommand::_control_type arg)
  {
    msg_.control = std::move(arg);
    return Init_VehicleCommand_shift(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::VehicleCommand msg_;
};

class Init_VehicleCommand_header
{
public:
  Init_VehicleCommand_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_VehicleCommand_control header(::autoware_vehicle_msgs::msg::VehicleCommand::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_VehicleCommand_control(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::VehicleCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_vehicle_msgs::msg::VehicleCommand>()
{
  return autoware_vehicle_msgs::msg::builder::Init_VehicleCommand_header();
}

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__VEHICLE_COMMAND__BUILDER_HPP_
