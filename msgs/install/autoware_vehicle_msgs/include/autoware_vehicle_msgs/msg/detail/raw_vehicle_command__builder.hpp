// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_vehicle_msgs:msg/RawVehicleCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_VEHICLE_COMMAND__BUILDER_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_VEHICLE_COMMAND__BUILDER_HPP_

#include "autoware_vehicle_msgs/msg/detail/raw_vehicle_command__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_vehicle_msgs
{

namespace msg
{

namespace builder
{

class Init_RawVehicleCommand_emergency
{
public:
  explicit Init_RawVehicleCommand_emergency(::autoware_vehicle_msgs::msg::RawVehicleCommand & msg)
  : msg_(msg)
  {}
  ::autoware_vehicle_msgs::msg::RawVehicleCommand emergency(::autoware_vehicle_msgs::msg::RawVehicleCommand::_emergency_type arg)
  {
    msg_.emergency = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawVehicleCommand msg_;
};

class Init_RawVehicleCommand_shift
{
public:
  explicit Init_RawVehicleCommand_shift(::autoware_vehicle_msgs::msg::RawVehicleCommand & msg)
  : msg_(msg)
  {}
  Init_RawVehicleCommand_emergency shift(::autoware_vehicle_msgs::msg::RawVehicleCommand::_shift_type arg)
  {
    msg_.shift = std::move(arg);
    return Init_RawVehicleCommand_emergency(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawVehicleCommand msg_;
};

class Init_RawVehicleCommand_control
{
public:
  explicit Init_RawVehicleCommand_control(::autoware_vehicle_msgs::msg::RawVehicleCommand & msg)
  : msg_(msg)
  {}
  Init_RawVehicleCommand_shift control(::autoware_vehicle_msgs::msg::RawVehicleCommand::_control_type arg)
  {
    msg_.control = std::move(arg);
    return Init_RawVehicleCommand_shift(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawVehicleCommand msg_;
};

class Init_RawVehicleCommand_header
{
public:
  Init_RawVehicleCommand_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RawVehicleCommand_control header(::autoware_vehicle_msgs::msg::RawVehicleCommand::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_RawVehicleCommand_control(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawVehicleCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_vehicle_msgs::msg::RawVehicleCommand>()
{
  return autoware_vehicle_msgs::msg::builder::Init_RawVehicleCommand_header();
}

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_VEHICLE_COMMAND__BUILDER_HPP_
