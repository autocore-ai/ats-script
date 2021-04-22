// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/StopSpeedExceeded.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_SPEED_EXCEEDED__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_SPEED_EXCEEDED__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/stop_speed_exceeded__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_StopSpeedExceeded_stop_speed_exceeded
{
public:
  explicit Init_StopSpeedExceeded_stop_speed_exceeded(::autoware_planning_msgs::msg::StopSpeedExceeded & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::StopSpeedExceeded stop_speed_exceeded(::autoware_planning_msgs::msg::StopSpeedExceeded::_stop_speed_exceeded_type arg)
  {
    msg_.stop_speed_exceeded = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::StopSpeedExceeded msg_;
};

class Init_StopSpeedExceeded_stamp
{
public:
  Init_StopSpeedExceeded_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StopSpeedExceeded_stop_speed_exceeded stamp(::autoware_planning_msgs::msg::StopSpeedExceeded::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_StopSpeedExceeded_stop_speed_exceeded(msg_);
  }

private:
  ::autoware_planning_msgs::msg::StopSpeedExceeded msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::StopSpeedExceeded>()
{
  return autoware_planning_msgs::msg::builder::Init_StopSpeedExceeded_stamp();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_SPEED_EXCEEDED__BUILDER_HPP_
