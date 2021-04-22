// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_system_msgs:msg/HazardStatus.idl
// generated code does not contain a copyright notice
#include "autoware_system_msgs/msg/detail/hazard_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `diagnostics_nf`
// Member `diagnostics_sf`
// Member `diagnostics_lf`
// Member `diagnostics_spf`
#include "diagnostic_msgs/msg/detail/diagnostic_status__functions.h"

bool
autoware_system_msgs__msg__HazardStatus__init(autoware_system_msgs__msg__HazardStatus * msg)
{
  if (!msg) {
    return false;
  }
  // level
  // diagnostics_nf
  if (!diagnostic_msgs__msg__DiagnosticStatus__Sequence__init(&msg->diagnostics_nf, 0)) {
    autoware_system_msgs__msg__HazardStatus__fini(msg);
    return false;
  }
  // diagnostics_sf
  if (!diagnostic_msgs__msg__DiagnosticStatus__Sequence__init(&msg->diagnostics_sf, 0)) {
    autoware_system_msgs__msg__HazardStatus__fini(msg);
    return false;
  }
  // diagnostics_lf
  if (!diagnostic_msgs__msg__DiagnosticStatus__Sequence__init(&msg->diagnostics_lf, 0)) {
    autoware_system_msgs__msg__HazardStatus__fini(msg);
    return false;
  }
  // diagnostics_spf
  if (!diagnostic_msgs__msg__DiagnosticStatus__Sequence__init(&msg->diagnostics_spf, 0)) {
    autoware_system_msgs__msg__HazardStatus__fini(msg);
    return false;
  }
  return true;
}

void
autoware_system_msgs__msg__HazardStatus__fini(autoware_system_msgs__msg__HazardStatus * msg)
{
  if (!msg) {
    return;
  }
  // level
  // diagnostics_nf
  diagnostic_msgs__msg__DiagnosticStatus__Sequence__fini(&msg->diagnostics_nf);
  // diagnostics_sf
  diagnostic_msgs__msg__DiagnosticStatus__Sequence__fini(&msg->diagnostics_sf);
  // diagnostics_lf
  diagnostic_msgs__msg__DiagnosticStatus__Sequence__fini(&msg->diagnostics_lf);
  // diagnostics_spf
  diagnostic_msgs__msg__DiagnosticStatus__Sequence__fini(&msg->diagnostics_spf);
}

autoware_system_msgs__msg__HazardStatus *
autoware_system_msgs__msg__HazardStatus__create()
{
  autoware_system_msgs__msg__HazardStatus * msg = (autoware_system_msgs__msg__HazardStatus *)malloc(sizeof(autoware_system_msgs__msg__HazardStatus));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_system_msgs__msg__HazardStatus));
  bool success = autoware_system_msgs__msg__HazardStatus__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_system_msgs__msg__HazardStatus__destroy(autoware_system_msgs__msg__HazardStatus * msg)
{
  if (msg) {
    autoware_system_msgs__msg__HazardStatus__fini(msg);
  }
  free(msg);
}


bool
autoware_system_msgs__msg__HazardStatus__Sequence__init(autoware_system_msgs__msg__HazardStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_system_msgs__msg__HazardStatus * data = NULL;
  if (size) {
    data = (autoware_system_msgs__msg__HazardStatus *)calloc(size, sizeof(autoware_system_msgs__msg__HazardStatus));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_system_msgs__msg__HazardStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_system_msgs__msg__HazardStatus__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
autoware_system_msgs__msg__HazardStatus__Sequence__fini(autoware_system_msgs__msg__HazardStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_system_msgs__msg__HazardStatus__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

autoware_system_msgs__msg__HazardStatus__Sequence *
autoware_system_msgs__msg__HazardStatus__Sequence__create(size_t size)
{
  autoware_system_msgs__msg__HazardStatus__Sequence * array = (autoware_system_msgs__msg__HazardStatus__Sequence *)malloc(sizeof(autoware_system_msgs__msg__HazardStatus__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_system_msgs__msg__HazardStatus__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_system_msgs__msg__HazardStatus__Sequence__destroy(autoware_system_msgs__msg__HazardStatus__Sequence * array)
{
  if (array) {
    autoware_system_msgs__msg__HazardStatus__Sequence__fini(array);
  }
  free(array);
}
