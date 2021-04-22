// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_planning_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__TRAITS_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__TRAITS_HPP_

#include "autoware_planning_msgs/msg/detail/stop_reason__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'stop_factors'
#include "autoware_planning_msgs/msg/detail/stop_factor__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_planning_msgs::msg::StopReason & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: reason
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reason: ";
    value_to_yaml(msg.reason, out);
    out << "\n";
  }

  // member: stop_factors
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.stop_factors.size() == 0) {
      out << "stop_factors: []\n";
    } else {
      out << "stop_factors:\n";
      for (auto item : msg.stop_factors) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_planning_msgs::msg::StopReason & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_planning_msgs::msg::StopReason>()
{
  return "autoware_planning_msgs::msg::StopReason";
}

template<>
inline const char * name<autoware_planning_msgs::msg::StopReason>()
{
  return "autoware_planning_msgs/msg/StopReason";
}

template<>
struct has_fixed_size<autoware_planning_msgs::msg::StopReason>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autoware_planning_msgs::msg::StopReason>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autoware_planning_msgs::msg::StopReason>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__TRAITS_HPP_
