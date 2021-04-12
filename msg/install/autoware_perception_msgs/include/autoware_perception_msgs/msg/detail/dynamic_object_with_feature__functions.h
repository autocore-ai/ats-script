// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeature.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__FUNCTIONS_H_
#define AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "autoware_perception_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__struct.h"

/// Initialize msg/DynamicObjectWithFeature message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * autoware_perception_msgs__msg__DynamicObjectWithFeature
 * )) before or use
 * autoware_perception_msgs__msg__DynamicObjectWithFeature__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_perception_msgs
bool
autoware_perception_msgs__msg__DynamicObjectWithFeature__init(autoware_perception_msgs__msg__DynamicObjectWithFeature * msg);

/// Finalize msg/DynamicObjectWithFeature message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_perception_msgs
void
autoware_perception_msgs__msg__DynamicObjectWithFeature__fini(autoware_perception_msgs__msg__DynamicObjectWithFeature * msg);

/// Create msg/DynamicObjectWithFeature message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * autoware_perception_msgs__msg__DynamicObjectWithFeature__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_perception_msgs
autoware_perception_msgs__msg__DynamicObjectWithFeature *
autoware_perception_msgs__msg__DynamicObjectWithFeature__create();

/// Destroy msg/DynamicObjectWithFeature message.
/**
 * It calls
 * autoware_perception_msgs__msg__DynamicObjectWithFeature__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_perception_msgs
void
autoware_perception_msgs__msg__DynamicObjectWithFeature__destroy(autoware_perception_msgs__msg__DynamicObjectWithFeature * msg);


/// Initialize array of msg/DynamicObjectWithFeature messages.
/**
 * It allocates the memory for the number of elements and calls
 * autoware_perception_msgs__msg__DynamicObjectWithFeature__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_perception_msgs
bool
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__init(autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * array, size_t size);

/// Finalize array of msg/DynamicObjectWithFeature messages.
/**
 * It calls
 * autoware_perception_msgs__msg__DynamicObjectWithFeature__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_perception_msgs
void
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__fini(autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * array);

/// Create array of msg/DynamicObjectWithFeature messages.
/**
 * It allocates the memory for the array and calls
 * autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_perception_msgs
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence *
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__create(size_t size);

/// Destroy array of msg/DynamicObjectWithFeature messages.
/**
 * It calls
 * autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_perception_msgs
void
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__destroy(autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_PERCEPTION_MSGS__MSG__DETAIL__DYNAMIC_OBJECT_WITH_FEATURE__FUNCTIONS_H_
