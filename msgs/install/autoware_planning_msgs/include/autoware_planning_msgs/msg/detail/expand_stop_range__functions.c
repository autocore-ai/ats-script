// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_planning_msgs:msg/ExpandStopRange.idl
// generated code does not contain a copyright notice
#include "autoware_planning_msgs/msg/detail/expand_stop_range__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
autoware_planning_msgs__msg__ExpandStopRange__init(autoware_planning_msgs__msg__ExpandStopRange * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    autoware_planning_msgs__msg__ExpandStopRange__fini(msg);
    return false;
  }
  // expand_stop_range
  return true;
}

void
autoware_planning_msgs__msg__ExpandStopRange__fini(autoware_planning_msgs__msg__ExpandStopRange * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // expand_stop_range
}

autoware_planning_msgs__msg__ExpandStopRange *
autoware_planning_msgs__msg__ExpandStopRange__create()
{
  autoware_planning_msgs__msg__ExpandStopRange * msg = (autoware_planning_msgs__msg__ExpandStopRange *)malloc(sizeof(autoware_planning_msgs__msg__ExpandStopRange));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_planning_msgs__msg__ExpandStopRange));
  bool success = autoware_planning_msgs__msg__ExpandStopRange__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_planning_msgs__msg__ExpandStopRange__destroy(autoware_planning_msgs__msg__ExpandStopRange * msg)
{
  if (msg) {
    autoware_planning_msgs__msg__ExpandStopRange__fini(msg);
  }
  free(msg);
}


bool
autoware_planning_msgs__msg__ExpandStopRange__Sequence__init(autoware_planning_msgs__msg__ExpandStopRange__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_planning_msgs__msg__ExpandStopRange * data = NULL;
  if (size) {
    data = (autoware_planning_msgs__msg__ExpandStopRange *)calloc(size, sizeof(autoware_planning_msgs__msg__ExpandStopRange));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_planning_msgs__msg__ExpandStopRange__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_planning_msgs__msg__ExpandStopRange__fini(&data[i - 1]);
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
autoware_planning_msgs__msg__ExpandStopRange__Sequence__fini(autoware_planning_msgs__msg__ExpandStopRange__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_planning_msgs__msg__ExpandStopRange__fini(&array->data[i]);
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

autoware_planning_msgs__msg__ExpandStopRange__Sequence *
autoware_planning_msgs__msg__ExpandStopRange__Sequence__create(size_t size)
{
  autoware_planning_msgs__msg__ExpandStopRange__Sequence * array = (autoware_planning_msgs__msg__ExpandStopRange__Sequence *)malloc(sizeof(autoware_planning_msgs__msg__ExpandStopRange__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_planning_msgs__msg__ExpandStopRange__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_planning_msgs__msg__ExpandStopRange__Sequence__destroy(autoware_planning_msgs__msg__ExpandStopRange__Sequence * array)
{
  if (array) {
    autoware_planning_msgs__msg__ExpandStopRange__Sequence__fini(array);
  }
  free(array);
}
