// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_planning_msgs:msg/Scenario.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__SCENARIO__TRAITS_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__SCENARIO__TRAITS_HPP_

#include "autoware_planning_msgs/msg/detail/scenario__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_planning_msgs::msg::Scenario & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: current_scenario
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_scenario: ";
    value_to_yaml(msg.current_scenario, out);
    out << "\n";
  }

  // member: activating_scenarios
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.activating_scenarios.size() == 0) {
      out << "activating_scenarios: []\n";
    } else {
      out << "activating_scenarios:\n";
      for (auto item : msg.activating_scenarios) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_planning_msgs::msg::Scenario & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_planning_msgs::msg::Scenario>()
{
  return "autoware_planning_msgs::msg::Scenario";
}

template<>
inline const char * name<autoware_planning_msgs::msg::Scenario>()
{
  return "autoware_planning_msgs/msg/Scenario";
}

template<>
struct has_fixed_size<autoware_planning_msgs::msg::Scenario>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autoware_planning_msgs::msg::Scenario>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autoware_planning_msgs::msg::Scenario>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__SCENARIO__TRAITS_HPP_
