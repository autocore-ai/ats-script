// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_vehicle_msgs:msg/VehicleCommand.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__VEHICLE_COMMAND__STRUCT_HPP_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__VEHICLE_COMMAND__STRUCT_HPP_

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
// Member 'shift'
#include "autoware_vehicle_msgs/msg/detail/shift__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autoware_vehicle_msgs__msg__VehicleCommand __attribute__((deprecated))
#else
# define DEPRECATED__autoware_vehicle_msgs__msg__VehicleCommand __declspec(deprecated)
#endif

namespace autoware_vehicle_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct VehicleCommand_
{
  using Type = VehicleCommand_<ContainerAllocator>;

  explicit VehicleCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    control(_init),
    shift(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->emergency = 0l;
    }
  }

  explicit VehicleCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    control(_alloc, _init),
    shift(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->emergency = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _control_type =
    autoware_control_msgs::msg::ControlCommand_<ContainerAllocator>;
  _control_type control;
  using _shift_type =
    autoware_vehicle_msgs::msg::Shift_<ContainerAllocator>;
  _shift_type shift;
  using _emergency_type =
    int32_t;
  _emergency_type emergency;

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
  Type & set__shift(
    const autoware_vehicle_msgs::msg::Shift_<ContainerAllocator> & _arg)
  {
    this->shift = _arg;
    return *this;
  }
  Type & set__emergency(
    const int32_t & _arg)
  {
    this->emergency = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_vehicle_msgs__msg__VehicleCommand
    std::shared_ptr<autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_vehicle_msgs__msg__VehicleCommand
    std::shared_ptr<autoware_vehicle_msgs::msg::VehicleCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const VehicleCommand_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->control != other.control) {
      return false;
    }
    if (this->shift != other.shift) {
      return false;
    }
    if (this->emergency != other.emergency) {
      return false;
    }
    return true;
  }
  bool operator!=(const VehicleCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct VehicleCommand_

// alias to use template instance with default allocator
using VehicleCommand =
  autoware_vehicle_msgs::msg::VehicleCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_vehicle_msgs

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__VEHICLE_COMMAND__STRUCT_HPP_
