// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/Feature.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__FEATURE__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__FEATURE__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/feature__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_Feature_roi
{
public:
  explicit Init_Feature_roi(::autoware_perception_msgs::msg::Feature & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::Feature roi(::autoware_perception_msgs::msg::Feature::_roi_type arg)
  {
    msg_.roi = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::Feature msg_;
};

class Init_Feature_cluster
{
public:
  Init_Feature_cluster()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Feature_roi cluster(::autoware_perception_msgs::msg::Feature::_cluster_type arg)
  {
    msg_.cluster = std::move(arg);
    return Init_Feature_roi(msg_);
  }

private:
  ::autoware_perception_msgs::msg::Feature msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::Feature>()
{
  return autoware_perception_msgs::msg::builder::Init_Feature_cluster();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__FEATURE__BUILDER_HPP_
