// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_perception_msgs:msg/Semantic.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__TRAITS_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__TRAITS_HPP_

#include "autoware_perception_msgs/msg/detail/semantic__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_perception_msgs::msg::Semantic & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "type: ";
    value_to_yaml(msg.type, out);
    out << "\n";
  }

  // member: confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "confidence: ";
    value_to_yaml(msg.confidence, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_perception_msgs::msg::Semantic & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_perception_msgs::msg::Semantic>()
{
  return "autoware_perception_msgs::msg::Semantic";
}

template<>
inline const char * name<autoware_perception_msgs::msg::Semantic>()
{
  return "autoware_perception_msgs/msg/Semantic";
}

template<>
struct has_fixed_size<autoware_perception_msgs::msg::Semantic>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<autoware_perception_msgs::msg::Semantic>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<autoware_perception_msgs::msg::Semantic>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__TRAITS_HPP_
