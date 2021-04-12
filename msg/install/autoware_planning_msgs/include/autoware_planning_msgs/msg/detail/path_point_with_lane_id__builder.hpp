// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/PathPointWithLaneId.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__PATH_POINT_WITH_LANE_ID__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__PATH_POINT_WITH_LANE_ID__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/path_point_with_lane_id__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_PathPointWithLaneId_lane_ids
{
public:
  explicit Init_PathPointWithLaneId_lane_ids(::autoware_planning_msgs::msg::PathPointWithLaneId & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::PathPointWithLaneId lane_ids(::autoware_planning_msgs::msg::PathPointWithLaneId::_lane_ids_type arg)
  {
    msg_.lane_ids = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::PathPointWithLaneId msg_;
};

class Init_PathPointWithLaneId_point
{
public:
  Init_PathPointWithLaneId_point()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PathPointWithLaneId_lane_ids point(::autoware_planning_msgs::msg::PathPointWithLaneId::_point_type arg)
  {
    msg_.point = std::move(arg);
    return Init_PathPointWithLaneId_lane_ids(msg_);
  }

private:
  ::autoware_planning_msgs::msg::PathPointWithLaneId msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::PathPointWithLaneId>()
{
  return autoware_planning_msgs::msg::builder::Init_PathPointWithLaneId_point();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__PATH_POINT_WITH_LANE_ID__BUILDER_HPP_
