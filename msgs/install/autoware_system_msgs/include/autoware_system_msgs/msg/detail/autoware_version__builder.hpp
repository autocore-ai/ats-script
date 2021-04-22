// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_system_msgs:msg/AutowareVersion.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__BUILDER_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__BUILDER_HPP_

#include "autoware_system_msgs/msg/detail/autoware_version__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_system_msgs
{

namespace msg
{

namespace builder
{

class Init_AutowareVersion_ros_distro
{
public:
  explicit Init_AutowareVersion_ros_distro(::autoware_system_msgs::msg::AutowareVersion & msg)
  : msg_(msg)
  {}
  ::autoware_system_msgs::msg::AutowareVersion ros_distro(::autoware_system_msgs::msg::AutowareVersion::_ros_distro_type arg)
  {
    msg_.ros_distro = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_system_msgs::msg::AutowareVersion msg_;
};

class Init_AutowareVersion_ros_version
{
public:
  Init_AutowareVersion_ros_version()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AutowareVersion_ros_distro ros_version(::autoware_system_msgs::msg::AutowareVersion::_ros_version_type arg)
  {
    msg_.ros_version = std::move(arg);
    return Init_AutowareVersion_ros_distro(msg_);
  }

private:
  ::autoware_system_msgs::msg::AutowareVersion msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_system_msgs::msg::AutowareVersion>()
{
  return autoware_system_msgs::msg::builder::Init_AutowareVersion_ros_version();
}

}  // namespace autoware_system_msgs

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__BUILDER_HPP_
