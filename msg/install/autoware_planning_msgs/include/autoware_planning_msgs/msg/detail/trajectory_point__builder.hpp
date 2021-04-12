// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/TrajectoryPoint.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/trajectory_point__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_TrajectoryPoint_accel
{
public:
  explicit Init_TrajectoryPoint_accel(::autoware_planning_msgs::msg::TrajectoryPoint & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::TrajectoryPoint accel(::autoware_planning_msgs::msg::TrajectoryPoint::_accel_type arg)
  {
    msg_.accel = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::TrajectoryPoint msg_;
};

class Init_TrajectoryPoint_twist
{
public:
  explicit Init_TrajectoryPoint_twist(::autoware_planning_msgs::msg::TrajectoryPoint & msg)
  : msg_(msg)
  {}
  Init_TrajectoryPoint_accel twist(::autoware_planning_msgs::msg::TrajectoryPoint::_twist_type arg)
  {
    msg_.twist = std::move(arg);
    return Init_TrajectoryPoint_accel(msg_);
  }

private:
  ::autoware_planning_msgs::msg::TrajectoryPoint msg_;
};

class Init_TrajectoryPoint_pose
{
public:
  Init_TrajectoryPoint_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrajectoryPoint_twist pose(::autoware_planning_msgs::msg::TrajectoryPoint::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return Init_TrajectoryPoint_twist(msg_);
  }

private:
  ::autoware_planning_msgs::msg::TrajectoryPoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::TrajectoryPoint>()
{
  return autoware_planning_msgs::msg::builder::Init_TrajectoryPoint_pose();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__BUILDER_HPP_
