// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_lanelet2_msgs:msg/MapBin.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__STRUCT_HPP_
#define AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__STRUCT_HPP_

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
# define DEPRECATED__autoware_lanelet2_msgs__msg__MapBin __attribute__((deprecated))
#else
# define DEPRECATED__autoware_lanelet2_msgs__msg__MapBin __declspec(deprecated)
#endif

namespace autoware_lanelet2_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MapBin_
{
  using Type = MapBin_<ContainerAllocator>;

  explicit MapBin_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->format_version = "";
      this->map_version = "";
    }
  }

  explicit MapBin_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    format_version(_alloc),
    map_version(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->format_version = "";
      this->map_version = "";
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _format_version_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _format_version_type format_version;
  using _map_version_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _map_version_type map_version;
  using _data_type =
    std::vector<int8_t, typename ContainerAllocator::template rebind<int8_t>::other>;
  _data_type data;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__format_version(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->format_version = _arg;
    return *this;
  }
  Type & set__map_version(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->map_version = _arg;
    return *this;
  }
  Type & set__data(
    const std::vector<int8_t, typename ContainerAllocator::template rebind<int8_t>::other> & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_lanelet2_msgs__msg__MapBin
    std::shared_ptr<autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_lanelet2_msgs__msg__MapBin
    std::shared_ptr<autoware_lanelet2_msgs::msg::MapBin_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MapBin_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->format_version != other.format_version) {
      return false;
    }
    if (this->map_version != other.map_version) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const MapBin_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MapBin_

// alias to use template instance with default allocator
using MapBin =
  autoware_lanelet2_msgs::msg::MapBin_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_lanelet2_msgs

#endif  // AUTOWARE_LANELET2_MSGS__MSG__DETAIL__MAP_BIN__STRUCT_HPP_
