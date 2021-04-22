// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_system_msgs:msg/AutowareVersion.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__TRAITS_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__TRAITS_HPP_

#include "autoware_system_msgs/msg/detail/autoware_version__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_system_msgs::msg::AutowareVersion & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ros_version
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ros_version: ";
    value_to_yaml(msg.ros_version, out);
    out << "\n";
  }

  // member: ros_distro
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ros_distro: ";
    value_to_yaml(msg.ros_distro, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_system_msgs::msg::AutowareVersion & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_system_msgs::msg::AutowareVersion>()
{
  return "autoware_system_msgs::msg::AutowareVersion";
}

template<>
inline const char * name<autoware_system_msgs::msg::AutowareVersion>()
{
  return "autoware_system_msgs/msg/AutowareVersion";
}

template<>
struct has_fixed_size<autoware_system_msgs::msg::AutowareVersion>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autoware_system_msgs::msg::AutowareVersion>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autoware_system_msgs::msg::AutowareVersion>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__TRAITS_HPP_
