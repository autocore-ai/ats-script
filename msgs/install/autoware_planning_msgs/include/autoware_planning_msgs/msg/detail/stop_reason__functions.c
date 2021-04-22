// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_planning_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice
#include "autoware_planning_msgs/msg/detail/stop_reason__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `reason`
#include "rosidl_runtime_c/string_functions.h"
// Member `stop_factors`
#include "autoware_planning_msgs/msg/detail/stop_factor__functions.h"

bool
autoware_planning_msgs__msg__StopReason__init(autoware_planning_msgs__msg__StopReason * msg)
{
  if (!msg) {
    return false;
  }
  // reason
  if (!rosidl_runtime_c__String__init(&msg->reason)) {
    autoware_planning_msgs__msg__StopReason__fini(msg);
    return false;
  }
  // stop_factors
  if (!autoware_planning_msgs__msg__StopFactor__Sequence__init(&msg->stop_factors, 0)) {
    autoware_planning_msgs__msg__StopReason__fini(msg);
    return false;
  }
  return true;
}

void
autoware_planning_msgs__msg__StopReason__fini(autoware_planning_msgs__msg__StopReason * msg)
{
  if (!msg) {
    return;
  }
  // reason
  rosidl_runtime_c__String__fini(&msg->reason);
  // stop_factors
  autoware_planning_msgs__msg__StopFactor__Sequence__fini(&msg->stop_factors);
}

autoware_planning_msgs__msg__StopReason *
autoware_planning_msgs__msg__StopReason__create()
{
  autoware_planning_msgs__msg__StopReason * msg = (autoware_planning_msgs__msg__StopReason *)malloc(sizeof(autoware_planning_msgs__msg__StopReason));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_planning_msgs__msg__StopReason));
  bool success = autoware_planning_msgs__msg__StopReason__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_planning_msgs__msg__StopReason__destroy(autoware_planning_msgs__msg__StopReason * msg)
{
  if (msg) {
    autoware_planning_msgs__msg__StopReason__fini(msg);
  }
  free(msg);
}


bool
autoware_planning_msgs__msg__StopReason__Sequence__init(autoware_planning_msgs__msg__StopReason__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_planning_msgs__msg__StopReason * data = NULL;
  if (size) {
    data = (autoware_planning_msgs__msg__StopReason *)calloc(size, sizeof(autoware_planning_msgs__msg__StopReason));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_planning_msgs__msg__StopReason__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_planning_msgs__msg__StopReason__fini(&data[i - 1]);
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
autoware_planning_msgs__msg__StopReason__Sequence__fini(autoware_planning_msgs__msg__StopReason__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_planning_msgs__msg__StopReason__fini(&array->data[i]);
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

autoware_planning_msgs__msg__StopReason__Sequence *
autoware_planning_msgs__msg__StopReason__Sequence__create(size_t size)
{
  autoware_planning_msgs__msg__StopReason__Sequence * array = (autoware_planning_msgs__msg__StopReason__Sequence *)malloc(sizeof(autoware_planning_msgs__msg__StopReason__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_planning_msgs__msg__StopReason__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_planning_msgs__msg__StopReason__Sequence__destroy(autoware_planning_msgs__msg__StopReason__Sequence * array)
{
  if (array) {
    autoware_planning_msgs__msg__StopReason__Sequence__fini(array);
  }
  free(array);
}
