// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/DynamicObjectWithFeatureArray.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature_array__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `feature_objects`
#include "autoware_perception_msgs/msg/detail/dynamic_object_with_feature__functions.h"

bool
autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__init(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__fini(msg);
    return false;
  }
  // feature_objects
  if (!autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__init(&msg->feature_objects, 0)) {
    autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__fini(msg);
    return false;
  }
  return true;
}

void
autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__fini(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // feature_objects
  autoware_perception_msgs__msg__DynamicObjectWithFeature__Sequence__fini(&msg->feature_objects);
}

autoware_perception_msgs__msg__DynamicObjectWithFeatureArray *
autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__create()
{
  autoware_perception_msgs__msg__DynamicObjectWithFeatureArray * msg = (autoware_perception_msgs__msg__DynamicObjectWithFeatureArray *)malloc(sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray));
  bool success = autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__destroy(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence__init(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__DynamicObjectWithFeatureArray * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__DynamicObjectWithFeatureArray *)calloc(size, sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence__fini(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__fini(&array->data[i]);
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

autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence *
autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence * array = (autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence__destroy(autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__DynamicObjectWithFeatureArray__Sequence__fini(array);
  }
  free(array);
}
