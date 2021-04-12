// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from autoware_perception_msgs:msg/LampState.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__STRUCT_HPP_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__autoware_perception_msgs__msg__LampState __attribute__((deprecated))
#else
# define DEPRECATED__autoware_perception_msgs__msg__LampState __declspec(deprecated)
#endif

namespace autoware_perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LampState_
{
  using Type = LampState_<ContainerAllocator>;

  explicit LampState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->type = 0ul;
      this->confidence = 0.0f;
    }
  }

  explicit LampState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->type = 0ul;
      this->confidence = 0.0f;
    }
  }

  // field types and members
  using _type_type =
    uint32_t;
  _type_type type;
  using _confidence_type =
    float;
  _confidence_type confidence;

  // setters for named parameter idiom
  Type & set__type(
    const uint32_t & _arg)
  {
    this->type = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t UNKNOWN =
    0u;
  static constexpr uint8_t RED =
    1u;
  static constexpr uint8_t GREEN =
    2u;
  static constexpr uint8_t YELLOW =
    3u;
  static constexpr uint8_t LEFT =
    4u;
  static constexpr uint8_t RIGHT =
    5u;
  static constexpr uint8_t UP =
    6u;
  static constexpr uint8_t DOWN =
    7u;

  // pointer types
  using RawPtr =
    autoware_perception_msgs::msg::LampState_<ContainerAllocator> *;
  using ConstRawPtr =
    const autoware_perception_msgs::msg::LampState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<autoware_perception_msgs::msg::LampState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<autoware_perception_msgs::msg::LampState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      autoware_perception_msgs::msg::LampState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<autoware_perception_msgs::msg::LampState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      autoware_perception_msgs::msg::LampState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<autoware_perception_msgs::msg::LampState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<autoware_perception_msgs::msg::LampState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<autoware_perception_msgs::msg::LampState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__autoware_perception_msgs__msg__LampState
    std::shared_ptr<autoware_perception_msgs::msg::LampState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__autoware_perception_msgs__msg__LampState
    std::shared_ptr<autoware_perception_msgs::msg::LampState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LampState_ & other) const
  {
    if (this->type != other.type) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    return true;
  }
  bool operator!=(const LampState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LampState_

// alias to use template instance with default allocator
using LampState =
  autoware_perception_msgs::msg::LampState_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t LampState_<ContainerAllocator>::UNKNOWN;
template<typename ContainerAllocator>
constexpr uint8_t LampState_<ContainerAllocator>::RED;
template<typename ContainerAllocator>
constexpr uint8_t LampState_<ContainerAllocator>::GREEN;
template<typename ContainerAllocator>
constexpr uint8_t LampState_<ContainerAllocator>::YELLOW;
template<typename ContainerAllocator>
constexpr uint8_t LampState_<ContainerAllocator>::LEFT;
template<typename ContainerAllocator>
constexpr uint8_t LampState_<ContainerAllocator>::RIGHT;
template<typename ContainerAllocator>
constexpr uint8_t LampState_<ContainerAllocator>::UP;
template<typename ContainerAllocator>
constexpr uint8_t LampState_<ContainerAllocator>::DOWN;

}  // namespace msg

}  // namespace autoware_perception_msgs

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__LAMP_STATE__STRUCT_HPP_
