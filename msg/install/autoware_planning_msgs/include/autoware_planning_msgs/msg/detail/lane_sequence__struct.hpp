// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_planning_msgs:msg/LaneSequence.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_SEQUENCE__STRUCT_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_SEQUENCE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__autoware_planning_msgs__msg__LaneSequence __attribute__((deprecated))
#else
# define DEPRECATED__autoware_planning_msgs__msg__LaneSequence __declspec(deprecated)
#endif

namespace autoware_planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LaneSequence_
{
  using Type = LaneSequence_<ContainerAllocator>;

  explicit LaneSequence_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit LaneSequence_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _lane_ids_type =
    std::vector<int64_t, typename ContainerAllocator::template rebind<int64_t>::other>;
  _lane_ids_type lane_ids;

  // setters for named parameter idiom
  Type & set__lane_ids(
    const std::vector<int64_t, typename ContainerAllocator::template rebind<int64_t>::other> & _arg)
  {
    this->lane_ids = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_planning_msgs__msg__LaneSequence
    std::shared_ptr<autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_planning_msgs__msg__LaneSequence
    std::shared_ptr<autoware_planning_msgs::msg::LaneSequence_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LaneSequence_ & other) const
  {
    if (this->lane_ids != other.lane_ids) {
      return false;
    }
    return true;
  }
  bool operator!=(const LaneSequence_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LaneSequence_

// alias to use template instance with default allocator
using LaneSequence =
  autoware_planning_msgs::msg::LaneSequence_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__LANE_SEQUENCE__STRUCT_HPP_
