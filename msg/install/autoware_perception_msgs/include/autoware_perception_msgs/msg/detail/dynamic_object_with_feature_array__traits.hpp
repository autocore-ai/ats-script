// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeatureArray.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__TRAITS_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__TRAITS_HPP_

#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature_array__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'feature_objects'
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_perception_msgs::msg::DynamicObjectWithFeatureArray & msg,
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

  // member: feature_objects
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.feature_objects.size() == 0) {
      out << "feature_objects: []\n";
    } else {
      out << "feature_objects:\n";
      for (auto item : msg.feature_objects) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_perception_msgs::msg::DynamicObjectWithFeatureArray & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray>()
{
  return "autoware_perception_msgs::msg::DynamicObjectWithFeatureArray";
}

template<>
inline const char * name<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray>()
{
  return "autoware_perception_msgs/msg/DynamicObjectWithFeatureArray";
}

template<>
struct has_fixed_size<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__TRAITS_HPP_
