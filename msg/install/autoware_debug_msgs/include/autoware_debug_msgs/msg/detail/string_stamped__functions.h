// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from autoware_debug_msgs:msg/StringStamped.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_DEBUG_MSGS__MSG__DETAIL__STRING_STAMPED__FUNCTIONS_H_
#define AUTOWARE_DEBUG_MSGS__MSG__DETAIL__STRING_STAMPED__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "autoware_debug_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "autoware_debug_msgs/msg/detail/string_stamped__struct.h"

/// Initialize msg/StringStamped message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * autoware_debug_msgs__msg__StringStamped
 * )) before or use
 * autoware_debug_msgs__msg__StringStamped__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_debug_msgs
bool
autoware_debug_msgs__msg__StringStamped__init(autoware_debug_msgs__msg__StringStamped * msg);

/// Finalize msg/StringStamped message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_debug_msgs
void
autoware_debug_msgs__msg__StringStamped__fini(autoware_debug_msgs__msg__StringStamped * msg);

/// Create msg/StringStamped message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * autoware_debug_msgs__msg__StringStamped__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_debug_msgs
autoware_debug_msgs__msg__StringStamped *
autoware_debug_msgs__msg__StringStamped__create();

/// Destroy msg/StringStamped message.
/**
 * It calls
 * autoware_debug_msgs__msg__StringStamped__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_debug_msgs
void
autoware_debug_msgs__msg__StringStamped__destroy(autoware_debug_msgs__msg__StringStamped * msg);


/// Initialize array of msg/StringStamped messages.
/**
 * It allocates the memory for the number of elements and calls
 * autoware_debug_msgs__msg__StringStamped__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_debug_msgs
bool
autoware_debug_msgs__msg__StringStamped__Sequence__init(autoware_debug_msgs__msg__StringStamped__Sequence * array, size_t size);

/// Finalize array of msg/StringStamped messages.
/**
 * It calls
 * autoware_debug_msgs__msg__StringStamped__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_debug_msgs
void
autoware_debug_msgs__msg__StringStamped__Sequence__fini(autoware_debug_msgs__msg__StringStamped__Sequence * array);

/// Create array of msg/StringStamped messages.
/**
 * It allocates the memory for the array and calls
 * autoware_debug_msgs__msg__StringStamped__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_debug_msgs
autoware_debug_msgs__msg__StringStamped__Sequence *
autoware_debug_msgs__msg__StringStamped__Sequence__create(size_t size);

/// Destroy array of msg/StringStamped messages.
/**
 * It calls
 * autoware_debug_msgs__msg__StringStamped__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_debug_msgs
void
autoware_debug_msgs__msg__StringStamped__Sequence__destroy(autoware_debug_msgs__msg__StringStamped__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_DEBUG_MSGS__MSG__DETAIL__STRING_STAMPED__FUNCTIONS_H_
