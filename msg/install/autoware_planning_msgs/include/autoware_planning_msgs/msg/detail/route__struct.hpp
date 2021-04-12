// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_planning_msgs:msg/Route.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__STRUCT_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__STRUCT_HPP_

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
// Member 'goal_pose'
#include "geometry_msgs/msg/detail/pose__struct.hpp"
// Member 'route_sections'
#include "autoware_planning_msgs/msg/detail/route_section__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autoware_planning_msgs__msg__Route __attribute__((deprecated))
#else
# define DEPRECATED__autoware_planning_msgs__msg__Route __declspec(deprecated)
#endif

namespace autoware_planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Route_
{
  using Type = Route_<ContainerAllocator>;

  explicit Route_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    goal_pose(_init)
  {
    (void)_init;
  }

  explicit Route_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    goal_pose(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _goal_pose_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _goal_pose_type goal_pose;
  using _route_sections_type =
    std::vector<autoware_planning_msgs::msg::RouteSection_<ContainerAllocator>, typename ContainerAllocator::template rebind<autoware_planning_msgs::msg::RouteSection_<ContainerAllocator>>::other>;
  _route_sections_type route_sections;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__goal_pose(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->goal_pose = _arg;
    return *this;
  }
  Type & set__route_sections(
    const std::vector<autoware_planning_msgs::msg::RouteSection_<ContainerAllocator>, typename ContainerAllocator::template rebind<autoware_planning_msgs::msg::RouteSection_<ContainerAllocator>>::other> & _arg)
  {
    this->route_sections = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_planning_msgs::msg::Route_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_planning_msgs::msg::Route_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_planning_msgs::msg::Route_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_planning_msgs::msg::Route_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_planning_msgs::msg::Route_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_planning_msgs::msg::Route_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_planning_msgs::msg::Route_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_planning_msgs::msg::Route_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_planning_msgs::msg::Route_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_planning_msgs::msg::Route_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_planning_msgs__msg__Route
    std::shared_ptr<autoware_planning_msgs::msg::Route_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_planning_msgs__msg__Route
    std::shared_ptr<autoware_planning_msgs::msg::Route_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Route_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->goal_pose != other.goal_pose) {
      return false;
    }
    if (this->route_sections != other.route_sections) {
      return false;
    }
    return true;
  }
  bool operator!=(const Route_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Route_

// alias to use template instance with default allocator
using Route =
  autoware_planning_msgs::msg::Route_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ROUTE__STRUCT_HPP_
