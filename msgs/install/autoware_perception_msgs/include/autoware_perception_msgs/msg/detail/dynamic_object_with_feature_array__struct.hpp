// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeatureArray.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__STRUCT_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'feature_objects'
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autoware_perception_msgs__msg__DynamicObjectWithFeatureArray __attribute__((deprecated))
#else
# define DEPRECATED__autoware_perception_msgs__msg__DynamicObjectWithFeatureArray __declspec(deprecated)
#endif

namespace autoware_perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DynamicObjectWithFeatureArray_
{
  using Type = DynamicObjectWithFeatureArray_<ContainerAllocator>;

  explicit DynamicObjectWithFeatureArray_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    (void)_init;
  }

  explicit DynamicObjectWithFeatureArray_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _feature_objects_type =
    std::vector<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>, typename ContainerAllocator::template rebind<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>>::other>;
  _feature_objects_type feature_objects;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__feature_objects(
    const std::vector<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>, typename ContainerAllocator::template rebind<autoware_perception_msgs::msg::DynamicObjectWithFeature_<ContainerAllocator>>::other> & _arg)
  {
    this->feature_objects = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_perception_msgs__msg__DynamicObjectWithFeatureArray
    std::shared_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_perception_msgs__msg__DynamicObjectWithFeatureArray
    std::shared_ptr<autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DynamicObjectWithFeatureArray_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->feature_objects != other.feature_objects) {
      return false;
    }
    return true;
  }
  bool operator!=(const DynamicObjectWithFeatureArray_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DynamicObjectWithFeatureArray_

// alias to use template instance with default allocator
using DynamicObjectWithFeatureArray =
  autoware_perception_msgs::msg::DynamicObjectWithFeatureArray_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE_ARRAY__STRUCT_HPP_
