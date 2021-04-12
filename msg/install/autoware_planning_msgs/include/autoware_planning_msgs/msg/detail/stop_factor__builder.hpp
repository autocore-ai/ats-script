// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/StopFactor.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_FACTOR__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_FACTOR__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/stop_factor__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_StopFactor_stop_factor_points
{
public:
  explicit Init_StopFactor_stop_factor_points(::autoware_planning_msgs::msg::StopFactor & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::StopFactor stop_factor_points(::autoware_planning_msgs::msg::StopFactor::_stop_factor_points_type arg)
  {
    msg_.stop_factor_points = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::StopFactor msg_;
};

class Init_StopFactor_dist_to_stop_pose
{
public:
  explicit Init_StopFactor_dist_to_stop_pose(::autoware_planning_msgs::msg::StopFactor & msg)
  : msg_(msg)
  {}
  Init_StopFactor_stop_factor_points dist_to_stop_pose(::autoware_planning_msgs::msg::StopFactor::_dist_to_stop_pose_type arg)
  {
    msg_.dist_to_stop_pose = std::move(arg);
    return Init_StopFactor_stop_factor_points(msg_);
  }

private:
  ::autoware_planning_msgs::msg::StopFactor msg_;
};

class Init_StopFactor_stop_pose
{
public:
  Init_StopFactor_stop_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StopFactor_dist_to_stop_pose stop_pose(::autoware_planning_msgs::msg::StopFactor::_stop_pose_type arg)
  {
    msg_.stop_pose = std::move(arg);
    return Init_StopFactor_dist_to_stop_pose(msg_);
  }

private:
  ::autoware_planning_msgs::msg::StopFactor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::StopFactor>()
{
  return autoware_planning_msgs::msg::builder::Init_StopFactor_stop_pose();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_FACTOR__BUILDER_HPP_
