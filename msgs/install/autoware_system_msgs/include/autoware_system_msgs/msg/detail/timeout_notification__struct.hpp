// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_system_msgs:msg/TimeoutNotification.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__STRUCT_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autoware_system_msgs__msg__TimeoutNotification __attribute__((deprecated))
#else
# define DEPRECATED__autoware_system_msgs__msg__TimeoutNotification __declspec(deprecated)
#endif

namespace autoware_system_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TimeoutNotification_
{
  using Type = TimeoutNotification_<ContainerAllocator>;

  explicit TimeoutNotification_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_timeout = false;
    }
  }

  explicit TimeoutNotification_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_timeout = false;
    }
  }

  // field types and members
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;
  using _is_timeout_type =
    bool;
  _is_timeout_type is_timeout;

  // setters for named parameter idiom
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }
  Type & set__is_timeout(
    const bool & _arg)
  {
    this->is_timeout = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_system_msgs__msg__TimeoutNotification
    std::shared_ptr<autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_system_msgs__msg__TimeoutNotification
    std::shared_ptr<autoware_system_msgs::msg::TimeoutNotification_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TimeoutNotification_ & other) const
  {
    if (this->stamp != other.stamp) {
      return false;
    }
    if (this->is_timeout != other.is_timeout) {
      return false;
    }
    return true;
  }
  bool operator!=(const TimeoutNotification_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TimeoutNotification_

// alias to use template instance with default allocator
using TimeoutNotification =
  autoware_system_msgs::msg::TimeoutNotification_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_system_msgs

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__TIMEOUT_NOTIFICATION__STRUCT_HPP_
