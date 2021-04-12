// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/IsAvoidancePossible.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__IS_AVOIDANCE_POSSIBLE__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__IS_AVOIDANCE_POSSIBLE__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/is_avoidance_possible__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_IsAvoidancePossible_is_avoidance_possible
{
public:
  explicit Init_IsAvoidancePossible_is_avoidance_possible(::autoware_planning_msgs::msg::IsAvoidancePossible & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::IsAvoidancePossible is_avoidance_possible(::autoware_planning_msgs::msg::IsAvoidancePossible::_is_avoidance_possible_type arg)
  {
    msg_.is_avoidance_possible = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::IsAvoidancePossible msg_;
};

class Init_IsAvoidancePossible_stamp
{
public:
  Init_IsAvoidancePossible_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_IsAvoidancePossible_is_avoidance_possible stamp(::autoware_planning_msgs::msg::IsAvoidancePossible::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_IsAvoidancePossible_is_avoidance_possible(msg_);
  }

private:
  ::autoware_planning_msgs::msg::IsAvoidancePossible msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::IsAvoidancePossible>()
{
  return autoware_planning_msgs::msg::builder::Init_IsAvoidancePossible_stamp();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__IS_AVOIDANCE_POSSIBLE__BUILDER_HPP_
