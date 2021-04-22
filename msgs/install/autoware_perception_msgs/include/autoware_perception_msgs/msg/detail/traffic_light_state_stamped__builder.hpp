// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/TrafficLightStateStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_STAMPED__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_STAMPED__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/traffic_light_state_stamped__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_TrafficLightStateStamped_state
{
public:
  explicit Init_TrafficLightStateStamped_state(::autoware_perception_msgs::msg::TrafficLightStateStamped & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::TrafficLightStateStamped state(::autoware_perception_msgs::msg::TrafficLightStateStamped::_state_type arg)
  {
    msg_.state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::TrafficLightStateStamped msg_;
};

class Init_TrafficLightStateStamped_header
{
public:
  Init_TrafficLightStateStamped_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrafficLightStateStamped_state header(::autoware_perception_msgs::msg::TrafficLightStateStamped::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_TrafficLightStateStamped_state(msg_);
  }

private:
  ::autoware_perception_msgs::msg::TrafficLightStateStamped msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::TrafficLightStateStamped>()
{
  return autoware_perception_msgs::msg::builder::Init_TrafficLightStateStamped_header();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_STAMPED__BUILDER_HPP_
