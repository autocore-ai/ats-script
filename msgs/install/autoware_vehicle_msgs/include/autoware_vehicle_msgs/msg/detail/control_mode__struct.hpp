// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_vehicle_msgs:msg/ControlMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__STRUCT_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__STRUCT_HPP_

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

#ifndef _WIN32
# define DEPRECATED__autoware_vehicle_msgs__msg__ControlMode __attribute__((deprecated))
#else
# define DEPRECATED__autoware_vehicle_msgs__msg__ControlMode __declspec(deprecated)
#endif

namespace autoware_vehicle_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ControlMode_
{
  using Type = ControlMode_<ContainerAllocator>;

  explicit ControlMode_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0l;
    }
  }

  explicit ControlMode_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _data_type =
    int32_t;
  _data_type data;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__data(
    const int32_t & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t MANUAL =
    0u;
  static constexpr uint8_t AUTO =
    1u;
  static constexpr uint8_t AUTO_STEER_ONLY =
    2u;
  static constexpr uint8_t AUTO_PEDAL_ONLY =
    3u;

  // pointer types
  using RawPtr =
    autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_vehicle_msgs__msg__ControlMode
    std::shared_ptr<autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_vehicle_msgs__msg__ControlMode
    std::shared_ptr<autoware_vehicle_msgs::msg::ControlMode_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControlMode_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const ControlMode_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControlMode_

// alias to use template instance with default allocator
using ControlMode =
  autoware_vehicle_msgs::msg::ControlMode_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t ControlMode_<ContainerAllocator>::MANUAL;
template<typename ContainerAllocator>
constexpr uint8_t ControlMode_<ContainerAllocator>::AUTO;
template<typename ContainerAllocator>
constexpr uint8_t ControlMode_<ContainerAllocator>::AUTO_STEER_ONLY;
template<typename ContainerAllocator>
constexpr uint8_t ControlMode_<ContainerAllocator>::AUTO_PEDAL_ONLY;

}  // namespace msg

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__STRUCT_HPP_
