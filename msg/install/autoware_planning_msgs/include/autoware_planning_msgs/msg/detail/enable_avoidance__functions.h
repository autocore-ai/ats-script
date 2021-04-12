// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from autoware_planning_msgs:msg/EnableAvoidance.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ENABLE_AVOIDANCE__FUNCTIONS_H_
#define AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ENABLE_AVOIDANCE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "autoware_planning_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "autoware_planning_msgs/msg/detail/enable_avoidance__struct.h"

/// Initialize msg/EnableAvoidance message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * autoware_planning_msgs__msg__EnableAvoidance
 * )) before or use
 * autoware_planning_msgs__msg__EnableAvoidance__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_planning_msgs
bool
autoware_planning_msgs__msg__EnableAvoidance__init(autoware_planning_msgs__msg__EnableAvoidance * msg);

/// Finalize msg/EnableAvoidance message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_planning_msgs
void
autoware_planning_msgs__msg__EnableAvoidance__fini(autoware_planning_msgs__msg__EnableAvoidance * msg);

/// Create msg/EnableAvoidance message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * autoware_planning_msgs__msg__EnableAvoidance__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_planning_msgs
autoware_planning_msgs__msg__EnableAvoidance *
autoware_planning_msgs__msg__EnableAvoidance__create();

/// Destroy msg/EnableAvoidance message.
/**
 * It calls
 * autoware_planning_msgs__msg__EnableAvoidance__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_planning_msgs
void
autoware_planning_msgs__msg__EnableAvoidance__destroy(autoware_planning_msgs__msg__EnableAvoidance * msg);


/// Initialize array of msg/EnableAvoidance messages.
/**
 * It allocates the memory for the number of elements and calls
 * autoware_planning_msgs__msg__EnableAvoidance__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_planning_msgs
bool
autoware_planning_msgs__msg__EnableAvoidance__Sequence__init(autoware_planning_msgs__msg__EnableAvoidance__Sequence * array, size_t size);

/// Finalize array of msg/EnableAvoidance messages.
/**
 * It calls
 * autoware_planning_msgs__msg__EnableAvoidance__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_planning_msgs
void
autoware_planning_msgs__msg__EnableAvoidance__Sequence__fini(autoware_planning_msgs__msg__EnableAvoidance__Sequence * array);

/// Create array of msg/EnableAvoidance messages.
/**
 * It allocates the memory for the array and calls
 * autoware_planning_msgs__msg__EnableAvoidance__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_planning_msgs
autoware_planning_msgs__msg__EnableAvoidance__Sequence *
autoware_planning_msgs__msg__EnableAvoidance__Sequence__create(size_t size);

/// Destroy array of msg/EnableAvoidance messages.
/**
 * It calls
 * autoware_planning_msgs__msg__EnableAvoidance__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_planning_msgs
void
autoware_planning_msgs__msg__EnableAvoidance__Sequence__destroy(autoware_planning_msgs__msg__EnableAvoidance__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PLANNING_MSGS__MSG__DETAIL__ENABLE_AVOIDANCE__FUNCTIONS_H_
