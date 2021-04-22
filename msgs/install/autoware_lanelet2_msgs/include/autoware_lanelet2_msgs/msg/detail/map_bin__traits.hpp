// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_lanelet2_msgs:msg/MapBin.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__TRAITS_HPP_
#define AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__TRAITS_HPP_

#include "autoware_lanelet2_msgs/msg/detail/map_bin__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_lanelet2_msgs::msg::MapBin & msg,
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

  // member: format_version
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "format_version: ";
    value_to_yaml(msg.format_version, out);
    out << "\n";
  }

  // member: map_version
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "map_version: ";
    value_to_yaml(msg.map_version, out);
    out << "\n";
  }

  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.data.size() == 0) {
      out << "data: []\n";
    } else {
      out << "data:\n";
      for (auto item : msg.data) {
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

inline std::string to_yaml(const autoware_lanelet2_msgs::msg::MapBin & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_lanelet2_msgs::msg::MapBin>()
{
  return "autoware_lanelet2_msgs::msg::MapBin";
}

template<>
inline const char * name<autoware_lanelet2_msgs::msg::MapBin>()
{
  return "autoware_lanelet2_msgs/msg/MapBin";
}

template<>
struct has_fixed_size<autoware_lanelet2_msgs::msg::MapBin>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<autoware_lanelet2_msgs::msg::MapBin>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<autoware_lanelet2_msgs::msg::MapBin>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__TRAITS_HPP_
