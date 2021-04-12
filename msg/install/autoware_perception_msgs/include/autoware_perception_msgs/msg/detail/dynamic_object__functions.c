// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/DynamicObject.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/dynamic_object__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `semantic`
#include "autoware_perception_msgs/msg/detail/semantic__functions.h"
// Member `state`
#include "autoware_perception_msgs/msg/detail/state__functions.h"
// Member `shape`
#include "autoware_perception_msgs/msg/detail/shape__functions.h"

bool
autoware_perception_msgs__msg__DynamicObject__init(autoware_perception_msgs__msg__DynamicObject * msg)
{
  if (!msg) {
    return false;
  }
  // id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->id)) {
    autoware_perception_msgs__msg__DynamicObject__fini(msg);
    return false;
  }
  // semantic
  if (!autoware_perception_msgs__msg__Semantic__init(&msg->semantic)) {
    autoware_perception_msgs__msg__DynamicObject__fini(msg);
    return false;
  }
  // state
  if (!autoware_perception_msgs__msg__State__init(&msg->state)) {
    autoware_perception_msgs__msg__DynamicObject__fini(msg);
    return false;
  }
  // shape
  if (!autoware_perception_msgs__msg__Shape__init(&msg->shape)) {
    autoware_perception_msgs__msg__DynamicObject__fini(msg);
    return false;
  }
  return true;
}

void
autoware_perception_msgs__msg__DynamicObject__fini(autoware_perception_msgs__msg__DynamicObject * msg)
{
  if (!msg) {
    return;
  }
  // id
  unique_identifier_msgs__msg__UUID__fini(&msg->id);
  // semantic
  autoware_perception_msgs__msg__Semantic__fini(&msg->semantic);
  // state
  autoware_perception_msgs__msg__State__fini(&msg->state);
  // shape
  autoware_perception_msgs__msg__Shape__fini(&msg->shape);
}

autoware_perception_msgs__msg__DynamicObject *
autoware_perception_msgs__msg__DynamicObject__create()
{
  autoware_perception_msgs__msg__DynamicObject * msg = (autoware_perception_msgs__msg__DynamicObject *)malloc(sizeof(autoware_perception_msgs__msg__DynamicObject));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__DynamicObject));
  bool success = autoware_perception_msgs__msg__DynamicObject__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__DynamicObject__destroy(autoware_perception_msgs__msg__DynamicObject * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__DynamicObject__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__DynamicObject__Sequence__init(autoware_perception_msgs__msg__DynamicObject__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__DynamicObject * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__DynamicObject *)calloc(size, sizeof(autoware_perception_msgs__msg__DynamicObject));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__DynamicObject__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__DynamicObject__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__DynamicObject__Sequence__fini(autoware_perception_msgs__msg__DynamicObject__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__DynamicObject__fini(&array->data[i]);
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

autoware_perception_msgs__msg__DynamicObject__Sequence *
autoware_perception_msgs__msg__DynamicObject__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__DynamicObject__Sequence * array = (autoware_perception_msgs__msg__DynamicObject__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__DynamicObject__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__DynamicObject__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__DynamicObject__Sequence__destroy(autoware_perception_msgs__msg__DynamicObject__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__DynamicObject__Sequence__fini(array);
  }
  free(array);
}
