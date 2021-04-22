// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from autoware_vehicle_msgs:msg/ControlMode.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__FUNCTIONS_H_
#define AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "autoware_vehicle_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "autoware_vehicle_msgs/msg/detail/control_mode__struct.h"

/// Initialize msg/ControlMode message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * autoware_vehicle_msgs__msg__ControlMode
 * )) before or use
 * autoware_vehicle_msgs__msg__ControlMode__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_vehicle_msgs
bool
autoware_vehicle_msgs__msg__ControlMode__init(autoware_vehicle_msgs__msg__ControlMode * msg);

/// Finalize msg/ControlMode message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_vehicle_msgs
void
autoware_vehicle_msgs__msg__ControlMode__fini(autoware_vehicle_msgs__msg__ControlMode * msg);

/// Create msg/ControlMode message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * autoware_vehicle_msgs__msg__ControlMode__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_vehicle_msgs
autoware_vehicle_msgs__msg__ControlMode *
autoware_vehicle_msgs__msg__ControlMode__create();

/// Destroy msg/ControlMode message.
/**
 * It calls
 * autoware_vehicle_msgs__msg__ControlMode__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_vehicle_msgs
void
autoware_vehicle_msgs__msg__ControlMode__destroy(autoware_vehicle_msgs__msg__ControlMode * msg);


/// Initialize array of msg/ControlMode messages.
/**
 * It allocates the memory for the number of elements and calls
 * autoware_vehicle_msgs__msg__ControlMode__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_vehicle_msgs
bool
autoware_vehicle_msgs__msg__ControlMode__Sequence__init(autoware_vehicle_msgs__msg__ControlMode__Sequence * array, size_t size);

/// Finalize array of msg/ControlMode messages.
/**
 * It calls
 * autoware_vehicle_msgs__msg__ControlMode__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_vehicle_msgs
void
autoware_vehicle_msgs__msg__ControlMode__Sequence__fini(autoware_vehicle_msgs__msg__ControlMode__Sequence * array);

/// Create array of msg/ControlMode messages.
/**
 * It allocates the memory for the array and calls
 * autoware_vehicle_msgs__msg__ControlMode__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_vehicle_msgs
autoware_vehicle_msgs__msg__ControlMode__Sequence *
autoware_vehicle_msgs__msg__ControlMode__Sequence__create(size_t size);

/// Destroy array of msg/ControlMode messages.
/**
 * It calls
 * autoware_vehicle_msgs__msg__ControlMode__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_autoware_vehicle_msgs
void
autoware_vehicle_msgs__msg__ControlMode__Sequence__destroy(autoware_vehicle_msgs__msg__ControlMode__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_VEHICLE_MSGS__MSG__DETAIL__CONTROL_MODE__FUNCTIONS_H_
