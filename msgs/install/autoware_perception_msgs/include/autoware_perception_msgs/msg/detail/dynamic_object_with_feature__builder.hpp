// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeature.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__BUILDER_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__BUILDER_HPP_

#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace autoware_perception_msgs
{

namespace msg
{

namespace builder
{

class Init_DynamicObjectWithFeature_feature
{
public:
  explicit Init_DynamicObjectWithFeature_feature(::autoware_perception_msgs::msg::DynamicObjectWithFeature & msg)
  : msg_(msg)
  {}
  ::autoware_perception_msgs::msg::DynamicObjectWithFeature feature(::autoware_perception_msgs::msg::DynamicObjectWithFeature::_feature_type arg)
  {
    msg_.feature = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autoware_perception_msgs::msg::DynamicObjectWithFeature msg_;
};

class Init_DynamicObjectWithFeature_object
{
public:
  Init_DynamicObjectWithFeature_object()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DynamicObjectWithFeature_feature object(::autoware_perception_msgs::msg::DynamicObjectWithFeature::_object_type arg)
  {
    msg_.object = std::move(arg);
    return Init_DynamicObjectWithFeature_feature(msg_);
  }

private:
  ::autoware_perception_msgs::msg::DynamicObjectWithFeature msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::autoware_perception_msgs::msg::DynamicObjectWithFeature>()
{
  return autoware_perception_msgs::msg::builder::Init_DynamicObjectWithFeature_object();
}

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__BUILDER_HPP_
