// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_system_msgs:msg/DrivingCapability.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__STRUCT_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__autoware_system_msgs__msg__DrivingCapability __attribute__((deprecated))
#else
# define DEPRECATED__autoware_system_msgs__msg__DrivingCapability __declspec(deprecated)
#endif

namespace autoware_system_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DrivingCapability_
{
  using Type = DrivingCapability_<ContainerAllocator>;

  explicit DrivingCapability_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->manual_driving = false;
      this->autonomous_driving = false;
      this->remote_control = false;
      this->safe_stop = false;
      this->emergency_stop = false;
    }
  }

  explicit DrivingCapability_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->manual_driving = false;
      this->autonomous_driving = false;
      this->remote_control = false;
      this->safe_stop = false;
      this->emergency_stop = false;
    }
  }

  // field types and members
  using _manual_driving_type =
    bool;
  _manual_driving_type manual_driving;
  using _autonomous_driving_type =
    bool;
  _autonomous_driving_type autonomous_driving;
  using _remote_control_type =
    bool;
  _remote_control_type remote_control;
  using _safe_stop_type =
    bool;
  _safe_stop_type safe_stop;
  using _emergency_stop_type =
    bool;
  _emergency_stop_type emergency_stop;

  // setters for named parameter idiom
  Type & set__manual_driving(
    const bool & _arg)
  {
    this->manual_driving = _arg;
    return *this;
  }
  Type & set__autonomous_driving(
    const bool & _arg)
  {
    this->autonomous_driving = _arg;
    return *this;
  }
  Type & set__remote_control(
    const bool & _arg)
  {
    this->remote_control = _arg;
    return *this;
  }
  Type & set__safe_stop(
    const bool & _arg)
  {
    this->safe_stop = _arg;
    return *this;
  }
  Type & set__emergency_stop(
    const bool & _arg)
  {
    this->emergency_stop = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_system_msgs__msg__DrivingCapability
    std::shared_ptr<autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_system_msgs__msg__DrivingCapability
    std::shared_ptr<autoware_system_msgs::msg::DrivingCapability_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DrivingCapability_ & other) const
  {
    if (this->manual_driving != other.manual_driving) {
      return false;
    }
    if (this->autonomous_driving != other.autonomous_driving) {
      return false;
    }
    if (this->remote_control != other.remote_control) {
      return false;
    }
    if (this->safe_stop != other.safe_stop) {
      return false;
    }
    if (this->emergency_stop != other.emergency_stop) {
      return false;
    }
    return true;
  }
  bool operator!=(const DrivingCapability_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DrivingCapability_

// alias to use template instance with default allocator
using DrivingCapability =
  autoware_system_msgs::msg::DrivingCapability_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_system_msgs

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__DRIVING_CAPABILITY__STRUCT_HPP_
