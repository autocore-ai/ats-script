// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_debug_msgs:msg/Int64Stamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_DEBUG_MSGS__MSG__DETAIL__INT64_STAMPED__TRAITS_HPP_
#define AUTOWARE_DEBUG_MSGS__MSG__DETAIL__INT64_STAMPED__TRAITS_HPP_

#include "autoware_debug_msgs/msg/detail/int64_stamped__struct.hpp"
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
  const autoware_debug_msgs::msg::Int64Stamped & msg,
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

  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "data: ";
    value_to_yaml(msg.data, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_debug_msgs::msg::Int64Stamped & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_debug_msgs::msg::Int64Stamped>()
{
  return "autoware_debug_msgs::msg::Int64Stamped";
}

template<>
inline const char * name<autoware_debug_msgs::msg::Int64Stamped>()
{
  return "autoware_debug_msgs/msg/Int64Stamped";
}

template<>
struct has_fixed_size<autoware_debug_msgs::msg::Int64Stamped>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<autoware_debug_msgs::msg::Int64Stamped>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<autoware_debug_msgs::msg::Int64Stamped>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_DEBUG_MSGS__MSG__DETAIL__INT64_STAMPED__TRAITS_HPP_
