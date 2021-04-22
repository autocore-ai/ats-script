// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/traffic_light_state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_TrafficLightState_id
{
public:
  explicit Init_TrafficLightState_id(::autoware_perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::TrafficLightState id(::autoware_perception_msgs::msg::TrafficLightState::_id_type arg)
  {
    msg_.id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_lamp_states
{
public:
  Init_TrafficLightState_lamp_states()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrafficLightState_id lamp_states(::autoware_perception_msgs::msg::TrafficLightState::_lamp_states_type arg)
  {
    msg_.lamp_states = std::move(arg);
    return Init_TrafficLightState_id(msg_);
  }

private:
  ::autoware_perception_msgs::msg::TrafficLightState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::TrafficLightState>()
{
  return autoware_perception_msgs::msg::builder::Init_TrafficLightState_lamp_states();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__BUILDER_HPP_
