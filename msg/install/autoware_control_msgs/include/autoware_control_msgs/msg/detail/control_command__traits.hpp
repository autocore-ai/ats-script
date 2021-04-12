// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_control_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__TRAITS_HPP_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__TRAITS_HPP_

#include "autoware_control_msgs/msg/detail/control_command__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_control_msgs::msg::ControlCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: steering_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_angle: ";
    value_to_yaml(msg.steering_angle, out);
    out << "\n";
  }

  // member: steering_angle_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_angle_velocity: ";
    value_to_yaml(msg.steering_angle_velocity, out);
    out << "\n";
  }

  // member: velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity: ";
    value_to_yaml(msg.velocity, out);
    out << "\n";
  }

  // member: acceleration
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acceleration: ";
    value_to_yaml(msg.acceleration, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_control_msgs::msg::ControlCommand & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_control_msgs::msg::ControlCommand>()
{
  return "autoware_control_msgs::msg::ControlCommand";
}

template<>
inline const char * name<autoware_control_msgs::msg::ControlCommand>()
{
  return "autoware_control_msgs/msg/ControlCommand";
}

template<>
struct has_fixed_size<autoware_control_msgs::msg::ControlCommand>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<autoware_control_msgs::msg::ControlCommand>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<autoware_control_msgs::msg::ControlCommand>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND__TRAITS_HPP_
