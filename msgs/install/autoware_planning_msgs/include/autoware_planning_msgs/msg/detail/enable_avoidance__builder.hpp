// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/EnableAvoidance.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ENABLE_AVOIDANCE__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ENABLE_AVOIDANCE__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/enable_avoidance__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_EnableAvoidance_enable_avoidance
{
public:
  explicit Init_EnableAvoidance_enable_avoidance(::autoware_planning_msgs::msg::EnableAvoidance & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::EnableAvoidance enable_avoidance(::autoware_planning_msgs::msg::EnableAvoidance::_enable_avoidance_type arg)
  {
    msg_.enable_avoidance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::EnableAvoidance msg_;
};

class Init_EnableAvoidance_stamp
{
public:
  Init_EnableAvoidance_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_EnableAvoidance_enable_avoidance stamp(::autoware_planning_msgs::msg::EnableAvoidance::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_EnableAvoidance_enable_avoidance(msg_);
  }

private:
  ::autoware_planning_msgs::msg::EnableAvoidance msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::EnableAvoidance>()
{
  return autoware_planning_msgs::msg::builder::Init_EnableAvoidance_stamp();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ENABLE_AVOIDANCE__BUILDER_HPP_
