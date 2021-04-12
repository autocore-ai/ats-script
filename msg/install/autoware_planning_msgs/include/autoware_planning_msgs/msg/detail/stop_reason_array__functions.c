// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_planning_msgs:msg/StopReasonArray.idl
// generated code does not contain a copyright notice
#include "autoware_planning_msgs/msg/detail/stop_reason_array__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `stop_reasons`
#include "autoware_planning_msgs/msg/detail/stop_reason__functions.h"

bool
autoware_planning_msgs__msg__StopReasonArray__init(autoware_planning_msgs__msg__StopReasonArray * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    autoware_planning_msgs__msg__StopReasonArray__fini(msg);
    return false;
  }
  // stop_reasons
  if (!autoware_planning_msgs__msg__StopReason__Sequence__init(&msg->stop_reasons, 0)) {
    autoware_planning_msgs__msg__StopReasonArray__fini(msg);
    return false;
  }
  return true;
}

void
autoware_planning_msgs__msg__StopReasonArray__fini(autoware_planning_msgs__msg__StopReasonArray * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // stop_reasons
  autoware_planning_msgs__msg__StopReason__Sequence__fini(&msg->stop_reasons);
}

autoware_planning_msgs__msg__StopReasonArray *
autoware_planning_msgs__msg__StopReasonArray__create()
{
  autoware_planning_msgs__msg__StopReasonArray * msg = (autoware_planning_msgs__msg__StopReasonArray *)malloc(sizeof(autoware_planning_msgs__msg__StopReasonArray));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_planning_msgs__msg__StopReasonArray));
  bool success = autoware_planning_msgs__msg__StopReasonArray__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_planning_msgs__msg__StopReasonArray__destroy(autoware_planning_msgs__msg__StopReasonArray * msg)
{
  if (msg) {
    autoware_planning_msgs__msg__StopReasonArray__fini(msg);
  }
  free(msg);
}


bool
autoware_planning_msgs__msg__StopReasonArray__Sequence__init(autoware_planning_msgs__msg__StopReasonArray__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_planning_msgs__msg__StopReasonArray * data = NULL;
  if (size) {
    data = (autoware_planning_msgs__msg__StopReasonArray *)calloc(size, sizeof(autoware_planning_msgs__msg__StopReasonArray));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_planning_msgs__msg__StopReasonArray__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_planning_msgs__msg__StopReasonArray__fini(&data[i - 1]);
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
autoware_planning_msgs__msg__StopReasonArray__Sequence__fini(autoware_planning_msgs__msg__StopReasonArray__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_planning_msgs__msg__StopReasonArray__fini(&array->data[i]);
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

autoware_planning_msgs__msg__StopReasonArray__Sequence *
autoware_planning_msgs__msg__StopReasonArray__Sequence__create(size_t size)
{
  autoware_planning_msgs__msg__StopReasonArray__Sequence * array = (autoware_planning_msgs__msg__StopReasonArray__Sequence *)malloc(sizeof(autoware_planning_msgs__msg__StopReasonArray__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_planning_msgs__msg__StopReasonArray__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_planning_msgs__msg__StopReasonArray__Sequence__destroy(autoware_planning_msgs__msg__StopReasonArray__Sequence * array)
{
  if (array) {
    autoware_planning_msgs__msg__StopReasonArray__Sequence__fini(array);
  }
  free(array);
}
