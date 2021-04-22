// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_planning_msgs:msg/LaneSequence.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_SEQUENCE__BUILDER_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_SEQUENCE__BUILDER_HPP_

#include "autoware_planning_msgs/msg/detail/lane_sequence__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_planning_msgs
{

namespace msg
{

namespace builder
{

class Init_LaneSequence_lane_ids
{
public:
  Init_LaneSequence_lane_ids()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::autoware_planning_msgs::msg::LaneSequence lane_ids(::autoware_planning_msgs::msg::LaneSequence::_lane_ids_type arg)
  {
    msg_.lane_ids = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_planning_msgs::msg::LaneSequence msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_planning_msgs::msg::LaneSequence>()
{
  return autoware_planning_msgs::msg::builder::Init_LaneSequence_lane_ids();
}

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_SEQUENCE__BUILDER_HPP_
