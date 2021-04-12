// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__TRAITS_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__TRAITS_HPP_

#include "autoware_perception_msgs/msg/detail/traffic_light_state__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'lamp_states'
#include "autoware_perception_msgs/msg/detail/lamp_state__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_perception_msgs::msg::TrafficLightState & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: lamp_states
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.lamp_states.size() == 0) {
      out << "lamp_states: []\n";
    } else {
      out << "lamp_states:\n";
      for (auto item : msg.lamp_states) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "id: ";
    value_to_yaml(msg.id, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_perception_msgs::msg::TrafficLightState & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_perception_msgs::msg::TrafficLightState>()
{
  return "autoware_perception_msgs::msg::TrafficLightState";
}

template<>
inline const char * name<autoware_perception_msgs::msg::TrafficLightState>()
{
  return "autoware_perception_msgs/msg/TrafficLightState";
}

template<>
struct has_fixed_size<autoware_perception_msgs::msg::TrafficLightState>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autoware_perception_msgs::msg::TrafficLightState>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autoware_perception_msgs::msg::TrafficLightState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__TRAITS_HPP_
