// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_system_msgs:msg/AutowareState.idl
// generated code does not contain a copyright notice
#include "autoware_system_msgs/msg/detail/autoware_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `state`
// Member `msg`
#include "rosidl_runtime_c/string_functions.h"

bool
autoware_system_msgs__msg__AutowareState__init(autoware_system_msgs__msg__AutowareState * msg)
{
  if (!msg) {
    return false;
  }
  // state
  if (!rosidl_runtime_c__String__init(&msg->state)) {
    autoware_system_msgs__msg__AutowareState__fini(msg);
    return false;
  }
  // msg
  if (!rosidl_runtime_c__String__init(&msg->msg)) {
    autoware_system_msgs__msg__AutowareState__fini(msg);
    return false;
  }
  return true;
}

void
autoware_system_msgs__msg__AutowareState__fini(autoware_system_msgs__msg__AutowareState * msg)
{
  if (!msg) {
    return;
  }
  // state
  rosidl_runtime_c__String__fini(&msg->state);
  // msg
  rosidl_runtime_c__String__fini(&msg->msg);
}

autoware_system_msgs__msg__AutowareState *
autoware_system_msgs__msg__AutowareState__create()
{
  autoware_system_msgs__msg__AutowareState * msg = (autoware_system_msgs__msg__AutowareState *)malloc(sizeof(autoware_system_msgs__msg__AutowareState));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_system_msgs__msg__AutowareState));
  bool success = autoware_system_msgs__msg__AutowareState__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_system_msgs__msg__AutowareState__destroy(autoware_system_msgs__msg__AutowareState * msg)
{
  if (msg) {
    autoware_system_msgs__msg__AutowareState__fini(msg);
  }
  free(msg);
}


bool
autoware_system_msgs__msg__AutowareState__Sequence__init(autoware_system_msgs__msg__AutowareState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_system_msgs__msg__AutowareState * data = NULL;
  if (size) {
    data = (autoware_system_msgs__msg__AutowareState *)calloc(size, sizeof(autoware_system_msgs__msg__AutowareState));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_system_msgs__msg__AutowareState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_system_msgs__msg__AutowareState__fini(&data[i - 1]);
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
autoware_system_msgs__msg__AutowareState__Sequence__fini(autoware_system_msgs__msg__AutowareState__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_system_msgs__msg__AutowareState__fini(&array->data[i]);
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

autoware_system_msgs__msg__AutowareState__Sequence *
autoware_system_msgs__msg__AutowareState__Sequence__create(size_t size)
{
  autoware_system_msgs__msg__AutowareState__Sequence * array = (autoware_system_msgs__msg__AutowareState__Sequence *)malloc(sizeof(autoware_system_msgs__msg__AutowareState__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_system_msgs__msg__AutowareState__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_system_msgs__msg__AutowareState__Sequence__destroy(autoware_system_msgs__msg__AutowareState__Sequence * array)
{
  if (array) {
    autoware_system_msgs__msg__AutowareState__Sequence__fini(array);
  }
  free(array);
}
