// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_planning_msgs:msg/StopSpeedExceeded.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_SPEED_EXCEEDED__TRAITS_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_SPEED_EXCEEDED__TRAITS_HPP_

#include "autoware_planning_msgs/msg/detail/stop_speed_exceeded__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_planning_msgs::msg::StopSpeedExceeded & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_yaml(msg.stamp, out, indentation + 2);
  }

  // member: stop_speed_exceeded
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stop_speed_exceeded: ";
    value_to_yaml(msg.stop_speed_exceeded, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_planning_msgs::msg::StopSpeedExceeded & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_planning_msgs::msg::StopSpeedExceeded>()
{
  return "autoware_planning_msgs::msg::StopSpeedExceeded";
}

template<>
inline const char * name<autoware_planning_msgs::msg::StopSpeedExceeded>()
{
  return "autoware_planning_msgs/msg/StopSpeedExceeded";
}

template<>
struct has_fixed_size<autoware_planning_msgs::msg::StopSpeedExceeded>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<autoware_planning_msgs::msg::StopSpeedExceeded>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<autoware_planning_msgs::msg::StopSpeedExceeded>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_SPEED_EXCEEDED__TRAITS_HPP_
