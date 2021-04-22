// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_control_msgs:msg/GateMode.idl
// generated code does not contain a copyright notice
#include "autoware_control_msgs/msg/detail/gate_mode__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
autoware_control_msgs__msg__GateMode__init(autoware_control_msgs__msg__GateMode * msg)
{
  if (!msg) {
    return false;
  }
  // data
  return true;
}

void
autoware_control_msgs__msg__GateMode__fini(autoware_control_msgs__msg__GateMode * msg)
{
  if (!msg) {
    return;
  }
  // data
}

autoware_control_msgs__msg__GateMode *
autoware_control_msgs__msg__GateMode__create()
{
  autoware_control_msgs__msg__GateMode * msg = (autoware_control_msgs__msg__GateMode *)malloc(sizeof(autoware_control_msgs__msg__GateMode));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_control_msgs__msg__GateMode));
  bool success = autoware_control_msgs__msg__GateMode__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_control_msgs__msg__GateMode__destroy(autoware_control_msgs__msg__GateMode * msg)
{
  if (msg) {
    autoware_control_msgs__msg__GateMode__fini(msg);
  }
  free(msg);
}


bool
autoware_control_msgs__msg__GateMode__Sequence__init(autoware_control_msgs__msg__GateMode__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_control_msgs__msg__GateMode * data = NULL;
  if (size) {
    data = (autoware_control_msgs__msg__GateMode *)calloc(size, sizeof(autoware_control_msgs__msg__GateMode));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_control_msgs__msg__GateMode__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_control_msgs__msg__GateMode__fini(&data[i - 1]);
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
autoware_control_msgs__msg__GateMode__Sequence__fini(autoware_control_msgs__msg__GateMode__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_control_msgs__msg__GateMode__fini(&array->data[i]);
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

autoware_control_msgs__msg__GateMode__Sequence *
autoware_control_msgs__msg__GateMode__Sequence__create(size_t size)
{
  autoware_control_msgs__msg__GateMode__Sequence * array = (autoware_control_msgs__msg__GateMode__Sequence *)malloc(sizeof(autoware_control_msgs__msg__GateMode__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_control_msgs__msg__GateMode__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_control_msgs__msg__GateMode__Sequence__destroy(autoware_control_msgs__msg__GateMode__Sequence * array)
{
  if (array) {
    autoware_control_msgs__msg__GateMode__Sequence__fini(array);
  }
  free(array);
}
