// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_vehicle_msgs:msg/ShiftStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT_STAMPED__BUILDER_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT_STAMPED__BUILDER_HPP_

#include "autoware_vehicle_msgs/msg/detail/shift_stamped__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_vehicle_msgs
{

namespace msg
{

namespace builder
{

class Init_ShiftStamped_shift
{
public:
  explicit Init_ShiftStamped_shift(::autoware_vehicle_msgs::msg::ShiftStamped & msg)
  : msg_(msg)
  {}
  ::autoware_vehicle_msgs::msg::ShiftStamped shift(::autoware_vehicle_msgs::msg::ShiftStamped::_shift_type arg)
  {
    msg_.shift = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::ShiftStamped msg_;
};

class Init_ShiftStamped_header
{
public:
  Init_ShiftStamped_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ShiftStamped_shift header(::autoware_vehicle_msgs::msg::ShiftStamped::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ShiftStamped_shift(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::ShiftStamped msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_vehicle_msgs::msg::ShiftStamped>()
{
  return autoware_vehicle_msgs::msg::builder::Init_ShiftStamped_header();
}

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT_STAMPED__BUILDER_HPP_
