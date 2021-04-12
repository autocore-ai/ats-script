// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/VelocityLimit.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__VELOCITY_LIMIT__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__VELOCITY_LIMIT__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/velocity_limit__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_VelocityLimit_data
{
public:
  explicit Init_VelocityLimit_data(::autoware_planning_msgs::msg::VelocityLimit & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::VelocityLimit data(::autoware_planning_msgs::msg::VelocityLimit::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::VelocityLimit msg_;
};

class Init_VelocityLimit_stamp
{
public:
  Init_VelocityLimit_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_VelocityLimit_data stamp(::autoware_planning_msgs::msg::VelocityLimit::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_VelocityLimit_data(msg_);
  }

private:
  ::autoware_planning_msgs::msg::VelocityLimit msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::VelocityLimit>()
{
  return autoware_planning_msgs::msg::builder::Init_VelocityLimit_stamp();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__VELOCITY_LIMIT__BUILDER_HPP_
