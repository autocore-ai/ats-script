// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_vehicle_msgs:msg/BatteryStatus.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__BATTERY_STATUS__TRAITS_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__BATTERY_STATUS__TRAITS_HPP_

#include "autoware_vehicle_msgs/msg/detail/battery_status__struct.hpp"
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
  const autoware_vehicle_msgs::msg::BatteryStatus & msg,
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

  // member: energy_level
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "energy_level: ";
    value_to_yaml(msg.energy_level, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_vehicle_msgs::msg::BatteryStatus & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_vehicle_msgs::msg::BatteryStatus>()
{
  return "autoware_vehicle_msgs::msg::BatteryStatus";
}

template<>
inline const char * name<autoware_vehicle_msgs::msg::BatteryStatus>()
{
  return "autoware_vehicle_msgs/msg/BatteryStatus";
}

template<>
struct has_fixed_size<autoware_vehicle_msgs::msg::BatteryStatus>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<autoware_vehicle_msgs::msg::BatteryStatus>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<autoware_vehicle_msgs::msg::BatteryStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__BATTERY_STATUS__TRAITS_HPP_
