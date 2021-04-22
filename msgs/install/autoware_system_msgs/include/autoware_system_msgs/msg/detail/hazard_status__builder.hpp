// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_system_msgs:msg/HazardStatus.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__BUILDER_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__BUILDER_HPP_

#include "autoware_system_msgs/msg/detail/hazard_status__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_system_msgs
{

namespace msg
{

namespace builder
{

class Init_HazardStatus_diagnostics_spf
{
public:
  explicit Init_HazardStatus_diagnostics_spf(::autoware_system_msgs::msg::HazardStatus & msg)
  : msg_(msg)
  {}
  ::autoware_system_msgs::msg::HazardStatus diagnostics_spf(::autoware_system_msgs::msg::HazardStatus::_diagnostics_spf_type arg)
  {
    msg_.diagnostics_spf = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_system_msgs::msg::HazardStatus msg_;
};

class Init_HazardStatus_diagnostics_lf
{
public:
  explicit Init_HazardStatus_diagnostics_lf(::autoware_system_msgs::msg::HazardStatus & msg)
  : msg_(msg)
  {}
  Init_HazardStatus_diagnostics_spf diagnostics_lf(::autoware_system_msgs::msg::HazardStatus::_diagnostics_lf_type arg)
  {
    msg_.diagnostics_lf = std::move(arg);
    return Init_HazardStatus_diagnostics_spf(msg_);
  }

private:
  ::autoware_system_msgs::msg::HazardStatus msg_;
};

class Init_HazardStatus_diagnostics_sf
{
public:
  explicit Init_HazardStatus_diagnostics_sf(::autoware_system_msgs::msg::HazardStatus & msg)
  : msg_(msg)
  {}
  Init_HazardStatus_diagnostics_lf diagnostics_sf(::autoware_system_msgs::msg::HazardStatus::_diagnostics_sf_type arg)
  {
    msg_.diagnostics_sf = std::move(arg);
    return Init_HazardStatus_diagnostics_lf(msg_);
  }

private:
  ::autoware_system_msgs::msg::HazardStatus msg_;
};

class Init_HazardStatus_diagnostics_nf
{
public:
  explicit Init_HazardStatus_diagnostics_nf(::autoware_system_msgs::msg::HazardStatus & msg)
  : msg_(msg)
  {}
  Init_HazardStatus_diagnostics_sf diagnostics_nf(::autoware_system_msgs::msg::HazardStatus::_diagnostics_nf_type arg)
  {
    msg_.diagnostics_nf = std::move(arg);
    return Init_HazardStatus_diagnostics_sf(msg_);
  }

private:
  ::autoware_system_msgs::msg::HazardStatus msg_;
};

class Init_HazardStatus_level
{
public:
  Init_HazardStatus_level()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HazardStatus_diagnostics_nf level(::autoware_system_msgs::msg::HazardStatus::_level_type arg)
  {
    msg_.level = std::move(arg);
    return Init_HazardStatus_diagnostics_nf(msg_);
  }

private:
  ::autoware_system_msgs::msg::HazardStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_system_msgs::msg::HazardStatus>()
{
  return autoware_system_msgs::msg::builder::Init_HazardStatus_level();
}

}  // namespace autoware_system_msgs

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__BUILDER_HPP_
