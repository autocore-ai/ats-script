// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/Semantic.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/semantic__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_Semantic_confidence
{
public:
  explicit Init_Semantic_confidence(::autoware_perception_msgs::msg::Semantic & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::Semantic confidence(::autoware_perception_msgs::msg::Semantic::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::Semantic msg_;
};

class Init_Semantic_type
{
public:
  Init_Semantic_type()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Semantic_confidence type(::autoware_perception_msgs::msg::Semantic::_type_type arg)
  {
    msg_.type = std::move(arg);
    return Init_Semantic_confidence(msg_);
  }

private:
  ::autoware_perception_msgs::msg::Semantic msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::Semantic>()
{
  return autoware_perception_msgs::msg::builder::Init_Semantic_type();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__SEMANTIC__BUILDER_HPP_
