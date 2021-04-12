// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/Semantic.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/semantic__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
autoware_perception_msgs__msg__Semantic__init(autoware_perception_msgs__msg__Semantic * msg)
{
  if (!msg) {
    return false;
  }
  // type
  // confidence
  return true;
}

void
autoware_perception_msgs__msg__Semantic__fini(autoware_perception_msgs__msg__Semantic * msg)
{
  if (!msg) {
    return;
  }
  // type
  // confidence
}

autoware_perception_msgs__msg__Semantic *
autoware_perception_msgs__msg__Semantic__create()
{
  autoware_perception_msgs__msg__Semantic * msg = (autoware_perception_msgs__msg__Semantic *)malloc(sizeof(autoware_perception_msgs__msg__Semantic));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__Semantic));
  bool success = autoware_perception_msgs__msg__Semantic__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__Semantic__destroy(autoware_perception_msgs__msg__Semantic * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__Semantic__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__Semantic__Sequence__init(autoware_perception_msgs__msg__Semantic__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__Semantic * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__Semantic *)calloc(size, sizeof(autoware_perception_msgs__msg__Semantic));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__Semantic__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__Semantic__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__Semantic__Sequence__fini(autoware_perception_msgs__msg__Semantic__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__Semantic__fini(&array->data[i]);
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

autoware_perception_msgs__msg__Semantic__Sequence *
autoware_perception_msgs__msg__Semantic__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__Semantic__Sequence * array = (autoware_perception_msgs__msg__Semantic__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__Semantic__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__Semantic__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__Semantic__Sequence__destroy(autoware_perception_msgs__msg__Semantic__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__Semantic__Sequence__fini(array);
  }
  free(array);
}
