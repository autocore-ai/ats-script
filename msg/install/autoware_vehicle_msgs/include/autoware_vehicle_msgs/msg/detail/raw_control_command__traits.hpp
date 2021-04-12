// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from autoware_vehicle_msgs:msg/RawControlCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__TRAITS_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__TRAITS_HPP_

#include "autoware_vehicle_msgs/msg/detail/raw_control_command__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const autoware_vehicle_msgs::msg::RawControlCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: steering_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_angle: ";
    value_to_yaml(msg.steering_angle, out);
    out << "\n";
  }

  // member: steering_angle_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_angle_velocity: ";
    value_to_yaml(msg.steering_angle_velocity, out);
    out << "\n";
  }

  // member: throttle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "throttle: ";
    value_to_yaml(msg.throttle, out);
    out << "\n";
  }

  // member: brake
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "brake: ";
    value_to_yaml(msg.brake, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const autoware_vehicle_msgs::msg::RawControlCommand & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<autoware_vehicle_msgs::msg::RawControlCommand>()
{
  return "autoware_vehicle_msgs::msg::RawControlCommand";
}

template<>
inline const char * name<autoware_vehicle_msgs::msg::RawControlCommand>()
{
  return "autoware_vehicle_msgs/msg/RawControlCommand";
}

template<>
struct has_fixed_size<autoware_vehicle_msgs::msg::RawControlCommand>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<autoware_vehicle_msgs::msg::RawControlCommand>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<autoware_vehicle_msgs::msg::RawControlCommand>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__RAW_CONTROL_COMMAND__TRAITS_HPP_
