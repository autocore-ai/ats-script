// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_control_msgs:msg/GateMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__GATE_MODE__TRAITS_HPP_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__GATE_MODE__TRAITS_HPP_

#include "autoware_control_msgs/msg/detail/gate_mode__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_control_msgs::msg::GateMode & msg,
  std::ostream & out, size_t indentation = 0)
{
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

inline std::string to_yaml(const autoware_control_msgs::msg::GateMode & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_control_msgs::msg::GateMode>()
{
  return "autoware_control_msgs::msg::GateMode";
}

template<>
inline const char * name<autoware_control_msgs::msg::GateMode>()
{
  return "autoware_control_msgs/msg/GateMode";
}

template<>
struct has_fixed_size<autoware_control_msgs::msg::GateMode>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<autoware_control_msgs::msg::GateMode>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<autoware_control_msgs::msg::GateMode>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__GATE_MODE__TRAITS_HPP_
