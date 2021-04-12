// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/Shape.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/shape__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `dimensions`
#include "geometry_msgs/msg/detail/vector3__functions.h"
// Member `footprint`
#include "geometry_msgs/msg/detail/polygon__functions.h"

bool
autoware_perception_msgs__msg__Shape__init(autoware_perception_msgs__msg__Shape * msg)
{
  if (!msg) {
    return false;
  }
  // type
  // dimensions
  if (!geometry_msgs__msg__Vector3__init(&msg->dimensions)) {
    autoware_perception_msgs__msg__Shape__fini(msg);
    return false;
  }
  // footprint
  if (!geometry_msgs__msg__Polygon__init(&msg->footprint)) {
    autoware_perception_msgs__msg__Shape__fini(msg);
    return false;
  }
  return true;
}

void
autoware_perception_msgs__msg__Shape__fini(autoware_perception_msgs__msg__Shape * msg)
{
  if (!msg) {
    return;
  }
  // type
  // dimensions
  geometry_msgs__msg__Vector3__fini(&msg->dimensions);
  // footprint
  geometry_msgs__msg__Polygon__fini(&msg->footprint);
}

autoware_perception_msgs__msg__Shape *
autoware_perception_msgs__msg__Shape__create()
{
  autoware_perception_msgs__msg__Shape * msg = (autoware_perception_msgs__msg__Shape *)malloc(sizeof(autoware_perception_msgs__msg__Shape));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__Shape));
  bool success = autoware_perception_msgs__msg__Shape__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__Shape__destroy(autoware_perception_msgs__msg__Shape * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__Shape__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__Shape__Sequence__init(autoware_perception_msgs__msg__Shape__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__Shape * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__Shape *)calloc(size, sizeof(autoware_perception_msgs__msg__Shape));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__Shape__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__Shape__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__Shape__Sequence__fini(autoware_perception_msgs__msg__Shape__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__Shape__fini(&array->data[i]);
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

autoware_perception_msgs__msg__Shape__Sequence *
autoware_perception_msgs__msg__Shape__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__Shape__Sequence * array = (autoware_perception_msgs__msg__Shape__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__Shape__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__Shape__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__Shape__Sequence__destroy(autoware_perception_msgs__msg__Shape__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__Shape__Sequence__fini(array);
  }
  free(array);
}
