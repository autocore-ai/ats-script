// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_vehicle_msgs:msg/Shift.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT__BUILDER_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT__BUILDER_HPP_

#include "autoware_vehicle_msgs/msg/detail/shift__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_vehicle_msgs
{

namespace msg
{

namespace builder
{

class Init_Shift_data
{
public:
  Init_Shift_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::autoware_vehicle_msgs::msg::Shift data(::autoware_vehicle_msgs::msg::Shift::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_vehicle_msgs::msg::Shift msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_vehicle_msgs::msg::Shift>()
{
  return autoware_vehicle_msgs::msg::builder::Init_Shift_data();
}

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__SHIFT__BUILDER_HPP_
