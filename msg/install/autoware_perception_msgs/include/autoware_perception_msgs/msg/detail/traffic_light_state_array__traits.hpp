// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_perception_msgs:msg/TrafficLightStateArray.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_ARRAY__TRAITS_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_ARRAY__TRAITS_HPP_

#include "autoware_perception_msgs/msg/detail/traffic_light_state_array__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'states'
#include "autoware_perception_msgs/msg/detail/traffic_light_state__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_perception_msgs::msg::TrafficLightStateArray & msg,
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

  // member: states
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.states.size() == 0) {
      out << "states: []\n";
    } else {
      out << "states:\n";
      for (auto item : msg.states) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_perception_msgs::msg::TrafficLightStateArray & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_perception_msgs::msg::TrafficLightStateArray>()
{
  return "autoware_perception_msgs::msg::TrafficLightStateArray";
}

template<>
inline const char * name<autoware_perception_msgs::msg::TrafficLightStateArray>()
{
  return "autoware_perception_msgs/msg/TrafficLightStateArray";
}

template<>
struct has_fixed_size<autoware_perception_msgs::msg::TrafficLightStateArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autoware_perception_msgs::msg::TrafficLightStateArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autoware_perception_msgs::msg::TrafficLightStateArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE_ARRAY__TRAITS_HPP_
