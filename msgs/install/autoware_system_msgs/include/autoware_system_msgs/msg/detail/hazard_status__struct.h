// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from autoware_system_msgs:msg/HazardStatus.idl
// generated code does not contain a copyright notice

#ifndef AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__STRUCT_H_
#define AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'NO_FAULT'.
enum
{
  autoware_system_msgs__msg__HazardStatus__NO_FAULT = 0l
};

/// Constant 'SAFE_FAULT'.
enum
{
  autoware_system_msgs__msg__HazardStatus__SAFE_FAULT = 1l
};

/// Constant 'LATENT_FAULT'.
enum
{
  autoware_system_msgs__msg__HazardStatus__LATENT_FAULT = 2l
};

/// Constant 'SINGLE_POINT_FAULT'.
enum
{
  autoware_system_msgs__msg__HazardStatus__SINGLE_POINT_FAULT = 3l
};

// Include directives for member types
// Member 'diagnostics_nf'
// Member 'diagnostics_sf'
// Member 'diagnostics_lf'
// Member 'diagnostics_spf'
#include "diagnostic_msgs/msg/detail/diagnostic_status__struct.h"

// Struct defined in msg/HazardStatus in the package autoware_system_msgs.
typedef struct autoware_system_msgs__msg__HazardStatus
{
  int32_t level;
  diagnostic_msgs__msg__DiagnosticStatus__Sequence diagnostics_nf;
  diagnostic_msgs__msg__DiagnosticStatus__Sequence diagnostics_sf;
  diagnostic_msgs__msg__DiagnosticStatus__Sequence diagnostics_lf;
  diagnostic_msgs__msg__DiagnosticStatus__Sequence diagnostics_spf;
} autoware_system_msgs__msg__HazardStatus;

// Struct for a sequence of autoware_system_msgs__msg__HazardStatus.
typedef struct autoware_system_msgs__msg__HazardStatus__Sequence
{
  autoware_system_msgs__msg__HazardStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} autoware_system_msgs__msg__HazardStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AUTOWARE_SYSTEM_MSGS__MSG__DETAIL__HAZARD_STATUS__STRUCT_H_
