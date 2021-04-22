// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_system_msgs:msg/TimeoutNotification.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__BUILDER_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__BUILDER_HPP_

#include "autoware_system_msgs/msg/detail/timeout_notification__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_system_msgs
{

namespace msg
{

namespace builder
{

class Init_TimeoutNotification_is_timeout
{
public:
  explicit Init_TimeoutNotification_is_timeout(::autoware_system_msgs::msg::TimeoutNotification & msg)
  : msg_(msg)
  {}
  ::autoware_system_msgs::msg::TimeoutNotification is_timeout(::autoware_system_msgs::msg::TimeoutNotification::_is_timeout_type arg)
  {
    msg_.is_timeout = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_system_msgs::msg::TimeoutNotification msg_;
};

class Init_TimeoutNotification_stamp
{
public:
  Init_TimeoutNotification_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TimeoutNotification_is_timeout stamp(::autoware_system_msgs::msg::TimeoutNotification::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_TimeoutNotification_is_timeout(msg_);
  }

private:
  ::autoware_system_msgs::msg::TimeoutNotification msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_system_msgs::msg::TimeoutNotification>()
{
  return autoware_system_msgs::msg::builder::Init_TimeoutNotification_stamp();
}

}  // namespace autoware_system_msgs

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__BUILDER_HPP_
