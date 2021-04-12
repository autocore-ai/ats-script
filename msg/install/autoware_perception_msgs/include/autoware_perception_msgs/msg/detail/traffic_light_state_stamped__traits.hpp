// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_perception_msgs:msg/TrafficLightStateStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_STAMPED__TRAITS_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_STAMPED__TRAITS_HPP_

#include "autoware_perception_msgs/msg/detail/traffic_light_state_stamped__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'state'
#include "autoware_perception_msgs/msg/detail/traffic_light_state__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_perception_msgs::msg::TrafficLightStateStamped & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_yaml(msg.header, out, indentation + 2);
  }

  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state:\n";
    to_yaml(msg.state, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_perception_msgs::msg::TrafficLightStateStamped & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_perception_msgs::msg::TrafficLightStateStamped>()
{
  return "autoware_perception_msgs::msg::TrafficLightStateStamped";
}

template<>
inline const char * name<autoware_perception_msgs::msg::TrafficLightStateStamped>()
{
  return "autoware_perception_msgs/msg/TrafficLightStateStamped";
}

template<>
struct has_fixed_size<autoware_perception_msgs::msg::TrafficLightStateStamped>
  : std::integral_constant<bool, has_fixed_size<autoware_perception_msgs::msg::TrafficLightState>::value && has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<autoware_perception_msgs::msg::TrafficLightStateStamped>
  : std::integral_constant<bool, has_bounded_size<autoware_perception_msgs::msg::TrafficLightState>::value && has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<autoware_perception_msgs::msg::TrafficLightStateStamped>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_STAMPED__TRAITS_HPP_
