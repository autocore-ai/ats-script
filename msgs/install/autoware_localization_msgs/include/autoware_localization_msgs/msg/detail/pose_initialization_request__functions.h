// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from autoware_localization_msgs:msg/PoseInitializationRequest.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__FUNCTIONS_H_
#define AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "autoware_localization_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "autoware_localization_msgs/msg/detail/pose_initialization_request__struct.h"

/// Initialize msg/PoseInitializationRequest message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * autoware_localization_msgs__msg__PoseInitializationRequest
 * )) before or use
 * autoware_localization_msgs__msg__PoseInitializationRequest__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_localization_msgs
bool
autoware_localization_msgs__msg__PoseInitializationRequest__init(autoware_localization_msgs__msg__PoseInitializationRequest * msg);

/// Finalize msg/PoseInitializationRequest message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_localization_msgs
void
autoware_localization_msgs__msg__PoseInitializationRequest__fini(autoware_localization_msgs__msg__PoseInitializationRequest * msg);

/// Create msg/PoseInitializationRequest message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * autoware_localization_msgs__msg__PoseInitializationRequest__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_localization_msgs
autoware_localization_msgs__msg__PoseInitializationRequest *
autoware_localization_msgs__msg__PoseInitializationRequest__create();

/// Destroy msg/PoseInitializationRequest message.
/**
 * It calls
 * autoware_localization_msgs__msg__PoseInitializationRequest__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_localization_msgs
void
autoware_localization_msgs__msg__PoseInitializationRequest__destroy(autoware_localization_msgs__msg__PoseInitializationRequest * msg);


/// Initialize array of msg/PoseInitializationRequest messages.
/**
 * It allocates the memory for the number of elements and calls
 * autoware_localization_msgs__msg__PoseInitializationRequest__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_localization_msgs
bool
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__init(autoware_localization_msgs__msg__PoseInitializationRequest__Sequence * array, size_t size);

/// Finalize array of msg/PoseInitializationRequest messages.
/**
 * It calls
 * autoware_localization_msgs__msg__PoseInitializationRequest__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_localization_msgs
void
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__fini(autoware_localization_msgs__msg__PoseInitializationRequest__Sequence * array);

/// Create array of msg/PoseInitializationRequest messages.
/**
 * It allocates the memory for the array and calls
 * autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_localization_msgs
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence *
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__create(size_t size);

/// Destroy array of msg/PoseInitializationRequest messages.
/**
 * It calls
 * autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_localization_msgs
void
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__destroy(autoware_localization_msgs__msg__PoseInitializationRequest__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_LOCALIZATION_MSGS__MSG__DETAIL__POSE_INITIALIZATION_REQUEST__FUNCTIONS_H_
