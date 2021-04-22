// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/LaneChangeStatus.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_STATUS__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_STATUS__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/lane_change_status__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_LaneChangeStatus_status
{
public:
  explicit Init_LaneChangeStatus_status(::autoware_planning_msgs::msg::LaneChangeStatus & msg)
  : msg_(msg)
  {}
  ::autoware_planning_msgs::msg::LaneChangeStatus status(::autoware_planning_msgs::msg::LaneChangeStatus::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::LaneChangeStatus msg_;
};

class Init_LaneChangeStatus_stamp
{
public:
  Init_LaneChangeStatus_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LaneChangeStatus_status stamp(::autoware_planning_msgs::msg::LaneChangeStatus::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_LaneChangeStatus_status(msg_);
  }

private:
  ::autoware_planning_msgs::msg::LaneChangeStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::LaneChangeStatus>()
{
  return autoware_planning_msgs::msg::builder::Init_LaneChangeStatus_stamp();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_CHANGE_STATUS__BUILDER_HPP_
