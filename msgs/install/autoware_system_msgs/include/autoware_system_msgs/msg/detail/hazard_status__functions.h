// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from autoware_system_msgs:msg/HazardStatus.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__FUNCTIONS_H_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "autoware_system_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "autoware_system_msgs/msg/detail/hazard_status__struct.h"

/// Initialize msg/HazardStatus message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * autoware_system_msgs__msg__HazardStatus
 * )) before or use
 * autoware_system_msgs__msg__HazardStatus__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_system_msgs
bool
autoware_system_msgs__msg__HazardStatus__init(autoware_system_msgs__msg__HazardStatus * msg);

/// Finalize msg/HazardStatus message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_system_msgs
void
autoware_system_msgs__msg__HazardStatus__fini(autoware_system_msgs__msg__HazardStatus * msg);

/// Create msg/HazardStatus message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * autoware_system_msgs__msg__HazardStatus__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_system_msgs
autoware_system_msgs__msg__HazardStatus *
autoware_system_msgs__msg__HazardStatus__create();

/// Destroy msg/HazardStatus message.
/**
 * It calls
 * autoware_system_msgs__msg__HazardStatus__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_system_msgs
void
autoware_system_msgs__msg__HazardStatus__destroy(autoware_system_msgs__msg__HazardStatus * msg);


/// Initialize array of msg/HazardStatus messages.
/**
 * It allocates the memory for the number of elements and calls
 * autoware_system_msgs__msg__HazardStatus__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_system_msgs
bool
autoware_system_msgs__msg__HazardStatus__Sequence__init(autoware_system_msgs__msg__HazardStatus__Sequence * array, size_t size);

/// Finalize array of msg/HazardStatus messages.
/**
 * It calls
 * autoware_system_msgs__msg__HazardStatus__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_system_msgs
void
autoware_system_msgs__msg__HazardStatus__Sequence__fini(autoware_system_msgs__msg__HazardStatus__Sequence * array);

/// Create array of msg/HazardStatus messages.
/**
 * It allocates the memory for the array and calls
 * autoware_system_msgs__msg__HazardStatus__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_system_msgs
autoware_system_msgs__msg__HazardStatus__Sequence *
autoware_system_msgs__msg__HazardStatus__Sequence__create(size_t size);

/// Destroy array of msg/HazardStatus messages.
/**
 * It calls
 * autoware_system_msgs__msg__HazardStatus__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_system_msgs
void
autoware_system_msgs__msg__HazardStatus__Sequence__destroy(autoware_system_msgs__msg__HazardStatus__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__FUNCTIONS_H_
