// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_system_msgs:msg/AutowareVersion.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__STRUCT_HPP_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__autoware_system_msgs__msg__AutowareVersion __attribute__((deprecated))
#else
# define DEPRECATED__autoware_system_msgs__msg__AutowareVersion __declspec(deprecated)
#endif

namespace autoware_system_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AutowareVersion_
{
  using Type = AutowareVersion_<ContainerAllocator>;

  explicit AutowareVersion_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->ros_version = 0ul;
      this->ros_distro = "";
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->ros_version = 0ul;
      this->ros_distro = "";
    }
  }

  explicit AutowareVersion_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ros_distro(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->ros_version = 0ul;
      this->ros_distro = "";
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->ros_version = 0ul;
      this->ros_distro = "";
    }
  }

  // field types and members
  using _ros_version_type =
    uint32_t;
  _ros_version_type ros_version;
  using _ros_distro_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _ros_distro_type ros_distro;

  // setters for named parameter idiom
  Type & set__ros_version(
    const uint32_t & _arg)
  {
    this->ros_version = _arg;
    return *this;
  }
  Type & set__ros_distro(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->ros_distro = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint32_t ROS_VERSION_1 =
    1u;
  static constexpr uint32_t ROS_VERSION_2 =
    2u;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> ROS_DISTRO_MELODIC;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> ROS_DISTRO_NOETIC;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> ROS_DISTRO_FOXY;

  // pointer types
  using RawPtr =
    autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_system_msgs__msg__AutowareVersion
    std::shared_ptr<autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_system_msgs__msg__AutowareVersion
    std::shared_ptr<autoware_system_msgs::msg::AutowareVersion_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AutowareVersion_ & other) const
  {
    if (this->ros_version != other.ros_version) {
      return false;
    }
    if (this->ros_distro != other.ros_distro) {
      return false;
    }
    return true;
  }
  bool operator!=(const AutowareVersion_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AutowareVersion_

// alias to use template instance with default allocator
using AutowareVersion =
  autoware_system_msgs::msg::AutowareVersion_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint32_t AutowareVersion_<ContainerAllocator>::ROS_VERSION_1;
template<typename ContainerAllocator>
constexpr uint32_t AutowareVersion_<ContainerAllocator>::ROS_VERSION_2;
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
AutowareVersion_<ContainerAllocator>::ROS_DISTRO_MELODIC = "melodic";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
AutowareVersion_<ContainerAllocator>::ROS_DISTRO_NOETIC = "noetic";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
AutowareVersion_<ContainerAllocator>::ROS_DISTRO_FOXY = "foxy";

}  // namespace msg

}  // namespace autoware_system_msgs

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__AUTOWARE_VERSION__STRUCT_HPP_
