// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_localization_msgs:msg/PoseInitializationRequest.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__BUILDER_HPP_
#define AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__BUILDER_HPP_

#include "autoware_localization_msgs/msg/detail/pose_initialization_request__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_localization_msgs
{

namespace msg
{

namespace builder
{

class Init_PoseInitializationRequest_data
{
public:
  explicit Init_PoseInitializationRequest_data(::autoware_localization_msgs::msg::PoseInitializationRequest & msg)
  : msg_(msg)
  {}
  ::autoware_localization_msgs::msg::PoseInitializationRequest data(::autoware_localization_msgs::msg::PoseInitializationRequest::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_localization_msgs::msg::PoseInitializationRequest msg_;
};

class Init_PoseInitializationRequest_stamp
{
public:
  Init_PoseInitializationRequest_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PoseInitializationRequest_data stamp(::autoware_localization_msgs::msg::PoseInitializationRequest::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_PoseInitializationRequest_data(msg_);
  }

private:
  ::autoware_localization_msgs::msg::PoseInitializationRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_localization_msgs::msg::PoseInitializationRequest>()
{
  return autoware_localization_msgs::msg::builder::Init_PoseInitializationRequest_stamp();
}

}  // namespace autoware_localization_msgs

#endif  // AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__BUILDER_HPP_
