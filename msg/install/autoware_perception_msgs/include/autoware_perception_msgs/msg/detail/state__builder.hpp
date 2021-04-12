// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/State.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__STATE__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__STATE__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_State_predicted_paths
{
public:
  explicit Init_State_predicted_paths(::autoware_perception_msgs::msg::State & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::State predicted_paths(::autoware_perception_msgs::msg::State::_predicted_paths_type arg)
  {
    msg_.predicted_paths = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::State msg_;
};

class Init_State_acceleration_reliable
{
public:
  explicit Init_State_acceleration_reliable(::autoware_perception_msgs::msg::State & msg)
  : msg_(msg)
  {}
  Init_State_predicted_paths acceleration_reliable(::autoware_perception_msgs::msg::State::_acceleration_reliable_type arg)
  {
    msg_.acceleration_reliable = std::move(arg);
    return Init_State_predicted_paths(msg_);
  }

private:
  ::autoware_perception_msgs::msg::State msg_;
};

class Init_State_acceleration_covariance
{
public:
  explicit Init_State_acceleration_covariance(::autoware_perception_msgs::msg::State & msg)
  : msg_(msg)
  {}
  Init_State_acceleration_reliable acceleration_covariance(::autoware_perception_msgs::msg::State::_acceleration_covariance_type arg)
  {
    msg_.acceleration_covariance = std::move(arg);
    return Init_State_acceleration_reliable(msg_);
  }

private:
  ::autoware_perception_msgs::msg::State msg_;
};

class Init_State_twist_reliable
{
public:
  explicit Init_State_twist_reliable(::autoware_perception_msgs::msg::State & msg)
  : msg_(msg)
  {}
  Init_State_acceleration_covariance twist_reliable(::autoware_perception_msgs::msg::State::_twist_reliable_type arg)
  {
    msg_.twist_reliable = std::move(arg);
    return Init_State_acceleration_covariance(msg_);
  }

private:
  ::autoware_perception_msgs::msg::State msg_;
};

class Init_State_twist_covariance
{
public:
  explicit Init_State_twist_covariance(::autoware_perception_msgs::msg::State & msg)
  : msg_(msg)
  {}
  Init_State_twist_reliable twist_covariance(::autoware_perception_msgs::msg::State::_twist_covariance_type arg)
  {
    msg_.twist_covariance = std::move(arg);
    return Init_State_twist_reliable(msg_);
  }

private:
  ::autoware_perception_msgs::msg::State msg_;
};

class Init_State_orientation_reliable
{
public:
  explicit Init_State_orientation_reliable(::autoware_perception_msgs::msg::State & msg)
  : msg_(msg)
  {}
  Init_State_twist_covariance orientation_reliable(::autoware_perception_msgs::msg::State::_orientation_reliable_type arg)
  {
    msg_.orientation_reliable = std::move(arg);
    return Init_State_twist_covariance(msg_);
  }

private:
  ::autoware_perception_msgs::msg::State msg_;
};

class Init_State_pose_covariance
{
public:
  Init_State_pose_covariance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_State_orientation_reliable pose_covariance(::autoware_perception_msgs::msg::State::_pose_covariance_type arg)
  {
    msg_.pose_covariance = std::move(arg);
    return Init_State_orientation_reliable(msg_);
  }

private:
  ::autoware_perception_msgs::msg::State msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::State>()
{
  return autoware_perception_msgs::msg::builder::Init_State_pose_covariance();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__STATE__BUILDER_HPP_
