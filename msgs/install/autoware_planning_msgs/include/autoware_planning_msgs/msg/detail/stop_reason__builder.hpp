// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/stop_reason__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_StopReason_stop_factors
{
public:
  explicit Init_StopReason_stop_factors(::autoware_planning_msgs::msg::StopReason & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::StopReason stop_factors(::autoware_planning_msgs::msg::StopReason::_stop_factors_type arg)
  {
    msg_.stop_factors = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::StopReason msg_;
};

class Init_StopReason_reason
{
public:
  Init_StopReason_reason()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StopReason_stop_factors reason(::autoware_planning_msgs::msg::StopReason::_reason_type arg)
  {
    msg_.reason = std::move(arg);
    return Init_StopReason_stop_factors(msg_);
  }

private:
  ::autoware_planning_msgs::msg::StopReason msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::StopReason>()
{
  return autoware_planning_msgs::msg::builder::Init_StopReason_reason();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__BUILDER_HPP_
