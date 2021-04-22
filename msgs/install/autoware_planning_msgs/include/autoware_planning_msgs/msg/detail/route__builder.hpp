// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/Route.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/route__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_Route_route_sections
{
public:
  explicit Init_Route_route_sections(::autoware_planning_msgs::msg::Route & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::Route route_sections(::autoware_planning_msgs::msg::Route::_route_sections_type arg)
  {
    msg_.route_sections = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::Route msg_;
};

class Init_Route_goal_pose
{
public:
  explicit Init_Route_goal_pose(::autoware_planning_msgs::msg::Route & msg)
  : msg_(msg)
  {}
  Init_Route_route_sections goal_pose(::autoware_planning_msgs::msg::Route::_goal_pose_type arg)
  {
    msg_.goal_pose = std::move(arg);
    return Init_Route_route_sections(msg_);
  }

private:
  ::autoware_planning_msgs::msg::Route msg_;
};

class Init_Route_header
{
public:
  Init_Route_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Route_goal_pose header(::autoware_planning_msgs::msg::Route::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Route_goal_pose(msg_);
  }

private:
  ::autoware_planning_msgs::msg::Route msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::Route>()
{
  return autoware_planning_msgs::msg::builder::Init_Route_header();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__BUILDER_HPP_
