// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeature.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__TRAITS_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__TRAITS_HPP_

#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'object'
#include "autoware_perception_msgs/msg/detail/dynamic_object__traits.hpp"
// Member 'feature'
#include "autoware_perception_msgs/msg/detail/feature__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_perception_msgs::msg::DynamicObjectWithFeature & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: object
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "object:\n";
    to_yaml(msg.object, out, indentation + 2);
  }

  // member: feature
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feature:\n";
    to_yaml(msg.feature, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_perception_msgs::msg::DynamicObjectWithFeature & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_perception_msgs::msg::DynamicObjectWithFeature>()
{
  return "autoware_perception_msgs::msg::DynamicObjectWithFeature";
}

template<>
inline const char * name<autoware_perception_msgs::msg::DynamicObjectWithFeature>()
{
  return "autoware_perception_msgs/msg/DynamicObjectWithFeature";
}

template<>
struct has_fixed_size<autoware_perception_msgs::msg::DynamicObjectWithFeature>
  : std::integral_constant<bool, has_fixed_size<autoware_perception_msgs::msg::DynamicObject>::value && has_fixed_size<autoware_perception_msgs::msg::Feature>::value> {};

template<>
struct has_bounded_size<autoware_perception_msgs::msg::DynamicObjectWithFeature>
  : std::integral_constant<bool, has_bounded_size<autoware_perception_msgs::msg::DynamicObject>::value && has_bounded_size<autoware_perception_msgs::msg::Feature>::value> {};

template<>
struct is_message<autoware_perception_msgs::msg::DynamicObjectWithFeature>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__TRAITS_HPP_
