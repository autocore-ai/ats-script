// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'lamp_states'
#include "autoware_perception_msgs/msg/detail/lamp_state__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__autoware_perception_msgs__msg__TrafficLightState __attribute__((deprecated))
#else
# define DEPRECATED__autoware_perception_msgs__msg__TrafficLightState __declspec(deprecated)
#endif

namespace autoware_perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TrafficLightState_
{
  using Type = TrafficLightState_<ContainerAllocator>;

  explicit TrafficLightState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
    }
  }

  explicit TrafficLightState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
    }
  }

  // field types and members
  using _lamp_states_type =
    std::vector<autoware_perception_msgs::msg::LampState_<ContainerAllocator>, typename ContainerAllocator::template rebind<autoware_perception_msgs::msg::LampState_<ContainerAllocator>>::other>;
  _lamp_states_type lamp_states;
  using _id_type =
    int32_t;
  _id_type id;

  // setters for named parameter idiom
  Type & set__lamp_states(
    const std::vector<autoware_perception_msgs::msg::LampState_<ContainerAllocator>, typename ContainerAllocator::template rebind<autoware_perception_msgs::msg::LampState_<ContainerAllocator>>::other> & _arg)
  {
    this->lamp_states = _arg;
    return *this;
  }
  Type & set__id(
    const int32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_perception_msgs__msg__TrafficLightState
    std::shared_ptr<autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_perception_msgs__msg__TrafficLightState
    std::shared_ptr<autoware_perception_msgs::msg::TrafficLightState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrafficLightState_ & other) const
  {
    if (this->lamp_states != other.lamp_states) {
      return false;
    }
    if (this->id != other.id) {
      return false;
    }
    return true;
  }
  bool operator!=(const TrafficLightState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrafficLightState_

// alias to use template instance with default allocator
using TrafficLightState =
  autoware_perception_msgs::msg::TrafficLightState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_HPP_
