// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_planning_msgs:msg/StopReasonArray.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON_ARRAY__TRAITS_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON_ARRAY__TRAITS_HPP_

#include "autoware_planning_msgs/msg/detail/stop_reason_array__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'stop_reasons'
#include "autoware_planning_msgs/msg/detail/stop_reason__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_planning_msgs::msg::StopReasonArray & msg,
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

  // member: stop_reasons
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.stop_reasons.size() == 0) {
      out << "stop_reasons: []\n";
    } else {
      out << "stop_reasons:\n";
      for (auto item : msg.stop_reasons) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_planning_msgs::msg::StopReasonArray & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_planning_msgs::msg::StopReasonArray>()
{
  return "autoware_planning_msgs::msg::StopReasonArray";
}

template<>
inline const char * name<autoware_planning_msgs::msg::StopReasonArray>()
{
  return "autoware_planning_msgs/msg/StopReasonArray";
}

template<>
struct has_fixed_size<autoware_planning_msgs::msg::StopReasonArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autoware_planning_msgs::msg::StopReasonArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autoware_planning_msgs::msg::StopReasonArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON_ARRAY__TRAITS_HPP_
