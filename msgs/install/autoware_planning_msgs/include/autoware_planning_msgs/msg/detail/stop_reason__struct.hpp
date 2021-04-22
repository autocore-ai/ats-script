// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_planning_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_HPP_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'stop_factors'
#include "autoware_planning_msgs/msg/detail/stop_factor__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autoware_planning_msgs__msg__StopReason __attribute__((deprecated))
#else
# define DEPRECATED__autoware_planning_msgs__msg__StopReason __declspec(deprecated)
#endif

namespace autoware_planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StopReason_
{
  using Type = StopReason_<ContainerAllocator>;

  explicit StopReason_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reason = "";
    }
  }

  explicit StopReason_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : reason(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reason = "";
    }
  }

  // field types and members
  using _reason_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _reason_type reason;
  using _stop_factors_type =
    std::vector<autoware_planning_msgs::msg::StopFactor_<ContainerAllocator>, typename ContainerAllocator::template rebind<autoware_planning_msgs::msg::StopFactor_<ContainerAllocator>>::other>;
  _stop_factors_type stop_factors;

  // setters for named parameter idiom
  Type & set__reason(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->reason = _arg;
    return *this;
  }
  Type & set__stop_factors(
    const std::vector<autoware_planning_msgs::msg::StopFactor_<ContainerAllocator>, typename ContainerAllocator::template rebind<autoware_planning_msgs::msg::StopFactor_<ContainerAllocator>>::other> & _arg)
  {
    this->stop_factors = _arg;
    return *this;
  }

  // constant declarations
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> INTERSECTION;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> MERGE_FROM_PRIVATE_ROAD;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> CROSSWALK;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> WALKWAY;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> STOP_LINE;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> DETECTION_AREA;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> TRAFFIC_LIGHT;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> OBSTACLE_STOP;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> SURROUND_OBSTACLE_CHECK;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> BLIND_SPOT;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> BLOCKED_BY_OBSTACLE;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> STOPPING_LANE_CHANGE;
  static const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> REMOTE_EMERGENCY_STOP;

  // pointer types
  using RawPtr =
    autoware_planning_msgs::msg::StopReason_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_planning_msgs::msg::StopReason_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_planning_msgs::msg::StopReason_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_planning_msgs::msg::StopReason_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_planning_msgs::msg::StopReason_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_planning_msgs::msg::StopReason_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_planning_msgs::msg::StopReason_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_planning_msgs::msg::StopReason_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_planning_msgs::msg::StopReason_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_planning_msgs::msg::StopReason_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_planning_msgs__msg__StopReason
    std::shared_ptr<autoware_planning_msgs::msg::StopReason_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_planning_msgs__msg__StopReason
    std::shared_ptr<autoware_planning_msgs::msg::StopReason_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StopReason_ & other) const
  {
    if (this->reason != other.reason) {
      return false;
    }
    if (this->stop_factors != other.stop_factors) {
      return false;
    }
    return true;
  }
  bool operator!=(const StopReason_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StopReason_

// alias to use template instance with default allocator
using StopReason =
  autoware_planning_msgs::msg::StopReason_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::INTERSECTION = "Intersection";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::MERGE_FROM_PRIVATE_ROAD = "MergeFromPrivateRoad";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::CROSSWALK = "Crosswalk";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::WALKWAY = "Walkway";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::STOP_LINE = "StopLine";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::DETECTION_AREA = "DetectionArea";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::TRAFFIC_LIGHT = "TrafficLight";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::OBSTACLE_STOP = "ObstacleStop";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::SURROUND_OBSTACLE_CHECK = "SurroundObstacleCheck";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::BLIND_SPOT = "BlindSpot";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::BLOCKED_BY_OBSTACLE = "BlockedByObstacle";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::STOPPING_LANE_CHANGE = "StoppingLaneChange";
template<typename ContainerAllocator>
const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>
StopReason_<ContainerAllocator>::REMOTE_EMERGENCY_STOP = "RemoteEmergencyStop";

}  // namespace msg

}  // namespace autoware_planning_msgs

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_HPP_
