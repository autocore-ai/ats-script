// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeature.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `object`
#include "autoware_perception_msgs/msg/detail/dynamic_object__functions.h"
// Member `feature`
#include "autoware_perception_msgs/msg/detail/feature__functions.h"

bool
autoware_perception_msgs__msg__DynamicObjectWithFeature__init(autoware_perception_msgs__msg__DynamicObjectWithFeature * msg)
{
  if (!msg) {
    return false;
  }
  // object
  if (!autoware_perception_msgs__msg__DynamicObject__init(&msg->object)) {
    autoware_perception_msgs__msg__DynamicObjectWithFeature__fini(msg);
    return false;
  }
  // feature
  if (!autoware_perception_msgs__msg__Feature__init(&msg->feature)) {
    autoware_perception_msgs__msg__DynamicObjectWithFeature__fini(msg);
    return false;
  }
  return true;
}

void
autoware_perception_msgs__msg__DynamicObjectWithFeature__fini(autoware_perception_msgs__msg__DynamicObjectWithFeature * msg)
{
  if (!msg) {
    return;
  }
  // object
  autoware_perception_msgs__msg__DynamicObject__fini(&msg->object);
  // feature
  autoware_perception_msgs__msg__Feature__fini(&msg->feature);
}

autoware_perception_msgs__msg__DynamicObjectWithFeature *
autoware_perception_msgs__msg__DynamicObjectWithFeature__create()
{
  autoware_perception_msgs__msg__DynamicObjectWithFeature * msg = (autoware_perception_msgs__msg__DynamicObjectWithFeature *)malloc(sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeature));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeature));
  bool success = autoware_perception_msgs__msg__DynamicObjectWithFeature__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__DynamicObjectWithFeature__destroy(autoware_perception_msgs__msg__DynamicObjectWithFeature * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__DynamicObjectWithFeature__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__init(autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__DynamicObjectWithFeature * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__DynamicObjectWithFeature *)calloc(size, sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeature));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__DynamicObjectWithFeature__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__DynamicObjectWithFeature__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__fini(autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__DynamicObjectWithFeature__fini(&array->data[i]);
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

autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence *
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * array = (autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__destroy(autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__fini(array);
  }
  free(array);
}
