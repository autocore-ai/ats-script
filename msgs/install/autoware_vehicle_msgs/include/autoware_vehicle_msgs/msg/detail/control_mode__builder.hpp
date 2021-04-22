// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_vehicle_msgs:msg/ControlMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__BUILDER_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__BUILDER_HPP_

#include "autoware_vehicle_msgs/msg/detail/control_mode__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_vehicle_msgs
{

namespace msg
{

namespace builder
{

class Init_ControlMode_data
{
public:
  explicit Init_ControlMode_data(::autoware_vehicle_msgs::msg::ControlMode & msg)
  : msg_(msg)
  {}
  ::autoware_vehicle_msgs::msg::ControlMode data(::autoware_vehicle_msgs::msg::ControlMode::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::ControlMode msg_;
};

class Init_ControlMode_header
{
public:
  Init_ControlMode_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlMode_data header(::autoware_vehicle_msgs::msg::ControlMode::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ControlMode_data(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::ControlMode msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_vehicle_msgs::msg::ControlMode>()
{
  return autoware_vehicle_msgs::msg::builder::Init_ControlMode_header();
}

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__BUILDER_HPP_
