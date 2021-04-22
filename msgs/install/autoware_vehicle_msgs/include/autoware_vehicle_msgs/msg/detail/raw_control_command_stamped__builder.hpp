// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_vehicle_msgs:msg/RawControlCommandStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND_STAMPED__BUILDER_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND_STAMPED__BUILDER_HPP_

#include "autoware_vehicle_msgs/msg/detail/raw_control_command_stamped__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_vehicle_msgs
{

namespace msg
{

namespace builder
{

class Init_RawControlCommandStamped_control
{
public:
  explicit Init_RawControlCommandStamped_control(::autoware_vehicle_msgs::msg::RawControlCommandStamped & msg)
  : msg_(msg)
  {}
  ::autoware_vehicle_msgs::msg::RawControlCommandStamped control(::autoware_vehicle_msgs::msg::RawControlCommandStamped::_control_type arg)
  {
    msg_.control = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawControlCommandStamped msg_;
};

class Init_RawControlCommandStamped_header
{
public:
  Init_RawControlCommandStamped_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RawControlCommandStamped_control header(::autoware_vehicle_msgs::msg::RawControlCommandStamped::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_RawControlCommandStamped_control(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::RawControlCommandStamped msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_vehicle_msgs::msg::RawControlCommandStamped>()
{
  return autoware_vehicle_msgs::msg::builder::Init_RawControlCommandStamped_header();
}

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND_STAMPED__BUILDER_HPP_
