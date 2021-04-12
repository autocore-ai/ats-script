// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_lanelet2_msgs:msg/MapBin.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__BUILDER_HPP_
#define AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__BUILDER_HPP_

#include "autoware_lanelet2_msgs/msg/detail/map_bin__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_lanelet2_msgs
{

namespace msg
{

namespace builder
{

class Init_MapBin_data
{
public:
  explicit Init_MapBin_data(::autoware_lanelet2_msgs::msg::MapBin & msg)
  : msg_(msg)
  {}
  ::autoware_lanelet2_msgs::msg::MapBin data(::autoware_lanelet2_msgs::msg::MapBin::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_lanelet2_msgs::msg::MapBin msg_;
};

class Init_MapBin_map_version
{
public:
  explicit Init_MapBin_map_version(::autoware_lanelet2_msgs::msg::MapBin & msg)
  : msg_(msg)
  {}
  Init_MapBin_data map_version(::autoware_lanelet2_msgs::msg::MapBin::_map_version_type arg)
  {
    msg_.map_version = std::move(arg);
    return Init_MapBin_data(msg_);
  }

private:
  ::autoware_lanelet2_msgs::msg::MapBin msg_;
};

class Init_MapBin_format_version
{
public:
  explicit Init_MapBin_format_version(::autoware_lanelet2_msgs::msg::MapBin & msg)
  : msg_(msg)
  {}
  Init_MapBin_map_version format_version(::autoware_lanelet2_msgs::msg::MapBin::_format_version_type arg)
  {
    msg_.format_version = std::move(arg);
    return Init_MapBin_map_version(msg_);
  }

private:
  ::autoware_lanelet2_msgs::msg::MapBin msg_;
};

class Init_MapBin_header
{
public:
  Init_MapBin_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MapBin_format_version header(::autoware_lanelet2_msgs::msg::MapBin::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_MapBin_format_version(msg_);
  }

private:
  ::autoware_lanelet2_msgs::msg::MapBin msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_lanelet2_msgs::msg::MapBin>()
{
  return autoware_lanelet2_msgs::msg::builder::Init_MapBin_header();
}

}  // namespace autoware_lanelet2_msgs

#endif  // AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__BUILDER_HPP_
