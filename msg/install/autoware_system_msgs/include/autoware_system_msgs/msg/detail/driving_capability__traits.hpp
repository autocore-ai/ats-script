// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_system_msgs:msg/DrivingCapability.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__TRAITS_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__TRAITS_HPP_

#include "autoware_system_msgs/msg/detail/driving_capability__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_system_msgs::msg::DrivingCapability & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: manual_driving
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "manual_driving: ";
    value_to_yaml(msg.manual_driving, out);
    out << "\n";
  }

  // member: autonomous_driving
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "autonomous_driving: ";
    value_to_yaml(msg.autonomous_driving, out);
    out << "\n";
  }

  // member: remote_control
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "remote_control: ";
    value_to_yaml(msg.remote_control, out);
    out << "\n";
  }

  // member: safe_stop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "safe_stop: ";
    value_to_yaml(msg.safe_stop, out);
    out << "\n";
  }

  // member: emergency_stop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "emergency_stop: ";
    value_to_yaml(msg.emergency_stop, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_system_msgs::msg::DrivingCapability & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_system_msgs::msg::DrivingCapability>()
{
  return "autoware_system_msgs::msg::DrivingCapability";
}

template<>
inline const char * name<autoware_system_msgs::msg::DrivingCapability>()
{
  return "autoware_system_msgs/msg/DrivingCapability";
}

template<>
struct has_fixed_size<autoware_system_msgs::msg::DrivingCapability>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<autoware_system_msgs::msg::DrivingCapability>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<autoware_system_msgs::msg::DrivingCapability>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__TRAITS_HPP_
