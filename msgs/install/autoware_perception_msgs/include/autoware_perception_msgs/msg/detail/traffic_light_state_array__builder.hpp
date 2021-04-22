// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/TrafficLightStateArray.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_ARRAY__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_ARRAY__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/traffic_light_state_array__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_TrafficLightStateArray_states
{
public:
  explicit Init_TrafficLightStateArray_states(::autoware_perception_msgs::msg::TrafficLightStateArray & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::TrafficLightStateArray states(::autoware_perception_msgs::msg::TrafficLightStateArray::_states_type arg)
  {
    msg_.states = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::TrafficLightStateArray msg_;
};

class Init_TrafficLightStateArray_header
{
public:
  Init_TrafficLightStateArray_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrafficLightStateArray_states header(::autoware_perception_msgs::msg::TrafficLightStateArray::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_TrafficLightStateArray_states(msg_);
  }

private:
  ::autoware_perception_msgs::msg::TrafficLightStateArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::TrafficLightStateArray>()
{
  return autoware_perception_msgs::msg::builder::Init_TrafficLightStateArray_header();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_ARRAY__BUILDER_HPP_
