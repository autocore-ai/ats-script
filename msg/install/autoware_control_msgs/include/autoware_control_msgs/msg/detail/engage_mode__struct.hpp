// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_control_msgs:msg/EngageMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__STRUCT_HPP_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__autoware_control_msgs__msg__EngageMode __attribute__((deprecated))
#else
# define DEPRECATED__autoware_control_msgs__msg__EngageMode __declspec(deprecated)
#endif

namespace autoware_control_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct EngageMode_
{
  using Type = EngageMode_<ContainerAllocator>;

  explicit EngageMode_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_engaged = false;
    }
  }

  explicit EngageMode_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_engaged = false;
    }
  }

  // field types and members
  using _is_engaged_type =
    bool;
  _is_engaged_type is_engaged;

  // setters for named parameter idiom
  Type & set__is_engaged(
    const bool & _arg)
  {
    this->is_engaged = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_control_msgs::msg::EngageMode_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_control_msgs::msg::EngageMode_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_control_msgs::msg::EngageMode_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_control_msgs::msg::EngageMode_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_control_msgs::msg::EngageMode_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_control_msgs::msg::EngageMode_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_control_msgs::msg::EngageMode_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_control_msgs::msg::EngageMode_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_control_msgs::msg::EngageMode_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_control_msgs::msg::EngageMode_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_control_msgs__msg__EngageMode
    std::shared_ptr<autoware_control_msgs::msg::EngageMode_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_control_msgs__msg__EngageMode
    std::shared_ptr<autoware_control_msgs::msg::EngageMode_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EngageMode_ & other) const
  {
    if (this->is_engaged != other.is_engaged) {
      return false;
    }
    return true;
  }
  bool operator!=(const EngageMode_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EngageMode_

// alias to use template instance with default allocator
using EngageMode =
  autoware_control_msgs::msg::EngageMode_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_control_msgs

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__ENGAGE_MODE__STRUCT_HPP_
