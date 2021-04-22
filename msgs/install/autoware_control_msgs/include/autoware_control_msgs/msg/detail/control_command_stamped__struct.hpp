// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_control_msgs:msg/ControlCommandStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__STRUCT_HPP_
#define AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__STRUCT_HPP_

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
// Member 'control'
#include "autoware_control_msgs/msg/detail/control_command__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autoware_control_msgs__msg__ControlCommandStamped __attribute__((deprecated))
#else
# define DEPRECATED__autoware_control_msgs__msg__ControlCommandStamped __declspec(deprecated)
#endif

namespace autoware_control_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ControlCommandStamped_
{
  using Type = ControlCommandStamped_<ContainerAllocator>;

  explicit ControlCommandStamped_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    control(_init)
  {
    (void)_init;
  }

  explicit ControlCommandStamped_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    control(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _control_type =
    autoware_control_msgs::msg::ControlCommand_<ContainerAllocator>;
  _control_type control;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__control(
    const autoware_control_msgs::msg::ControlCommand_<ContainerAllocator> & _arg)
  {
    this->control = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_control_msgs__msg__ControlCommandStamped
    std::shared_ptr<autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_control_msgs__msg__ControlCommandStamped
    std::shared_ptr<autoware_control_msgs::msg::ControlCommandStamped_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControlCommandStamped_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->control != other.control) {
      return false;
    }
    return true;
  }
  bool operator!=(const ControlCommandStamped_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControlCommandStamped_

// alias to use template instance with default allocator
using ControlCommandStamped =
  autoware_control_msgs::msg::ControlCommandStamped_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_control_msgs

#endif  // AUTOWARE_CONTROL_MSGS__MSG__DETAIL__CONTROL_COMMAND_STAMPED__STRUCT_HPP_
