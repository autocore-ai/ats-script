// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeature.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__STRUCT_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'object'
#include "autoware_perception_msgs/msg/detail/dynamic_object__struct.hpp"
// Member 'feature'
#include "autoware_perception_msgs/msg/detail/feature__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autoware_perception_msgs__msg__DynamicObjectWithFeature __attribute__((deprecated))
#else
# define DEPRECATED__autoware_perception_msgs__msg__DynamicObjectWithFeature __declspec(deprecated)
#endif

namespace autoware_perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DynamicObjectWithFeature_
{
  using Type = DynamicObjectWithFeature_<ContainerAllocator>;

  explicit DynamicObjectWithFeature_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : object(_init),
    feature(_init)
  {
    (void)_init;
  }

  explicit DynamicObjectWithFeature_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : object(_alloc, _init),
    feature(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _object_type =
    autoware_perception_msgs::msg::DynamicObject_<ContainerAllocator>;
  _object_type object;
  using _feature_type =
    autoware_perception_msgs::msg::Feature_<ContainerAllocator>;
  _feature_type feature;

  // setters for named parameter idiom
  Type & set__object(
    const autoware_perception_msgs::msg::DynamicObject_<ContainerAllocator> & _arg)
  {
    this->object = _arg;
    return *this;
  }
  Type & set__feature(
    const autoware_perception_msgs::msg::Feature_<ContainerAllocator> & _arg)
  {
    this->feature = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_perception_msgs__msg__DynamicObjectWithFeature
    std::shared_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_perception_msgs__msg__DynamicObjectWithFeature
    std::shared_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DynamicObjectWithFeature_ & other) const
  {
    if (this->object != other.object) {
      return false;
    }
    if (this->feature != other.feature) {
      return false;
    }
    return true;
  }
  bool operator!=(const DynamicObjectWithFeature_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DynamicObjectWithFeature_

// alias to use template instance with default allocator
using DynamicObjectWithFeature =
  autoware_perception_msgs::msg::DynamicObjectWithFeature_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__STRUCT_HPP_
