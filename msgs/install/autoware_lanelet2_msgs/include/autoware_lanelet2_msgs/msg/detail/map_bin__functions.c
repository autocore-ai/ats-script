// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_lanelet2_msgs:msg/MapBin.idl
// generated code does not contain a copyright notice
#include "autoware_lanelet2_msgs/msg/detail/map_bin__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `format_version`
// Member `map_version`
#include "rosidl_runtime_c/string_functions.h"
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
autoware_lanelet2_msgs__msg__MapBin__init(autoware_lanelet2_msgs__msg__MapBin * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    autoware_lanelet2_msgs__msg__MapBin__fini(msg);
    return false;
  }
  // format_version
  if (!rosidl_runtime_c__String__init(&msg->format_version)) {
    autoware_lanelet2_msgs__msg__MapBin__fini(msg);
    return false;
  }
  // map_version
  if (!rosidl_runtime_c__String__init(&msg->map_version)) {
    autoware_lanelet2_msgs__msg__MapBin__fini(msg);
    return false;
  }
  // data
  if (!rosidl_runtime_c__int8__Sequence__init(&msg->data, 0)) {
    autoware_lanelet2_msgs__msg__MapBin__fini(msg);
    return false;
  }
  return true;
}

void
autoware_lanelet2_msgs__msg__MapBin__fini(autoware_lanelet2_msgs__msg__MapBin * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // format_version
  rosidl_runtime_c__String__fini(&msg->format_version);
  // map_version
  rosidl_runtime_c__String__fini(&msg->map_version);
  // data
  rosidl_runtime_c__int8__Sequence__fini(&msg->data);
}

autoware_lanelet2_msgs__msg__MapBin *
autoware_lanelet2_msgs__msg__MapBin__create()
{
  autoware_lanelet2_msgs__msg__MapBin * msg = (autoware_lanelet2_msgs__msg__MapBin *)malloc(sizeof(autoware_lanelet2_msgs__msg__MapBin));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_lanelet2_msgs__msg__MapBin));
  bool success = autoware_lanelet2_msgs__msg__MapBin__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_lanelet2_msgs__msg__MapBin__destroy(autoware_lanelet2_msgs__msg__MapBin * msg)
{
  if (msg) {
    autoware_lanelet2_msgs__msg__MapBin__fini(msg);
  }
  free(msg);
}


bool
autoware_lanelet2_msgs__msg__MapBin__Sequence__init(autoware_lanelet2_msgs__msg__MapBin__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_lanelet2_msgs__msg__MapBin * data = NULL;
  if (size) {
    data = (autoware_lanelet2_msgs__msg__MapBin *)calloc(size, sizeof(autoware_lanelet2_msgs__msg__MapBin));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_lanelet2_msgs__msg__MapBin__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_lanelet2_msgs__msg__MapBin__fini(&data[i - 1]);
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
autoware_lanelet2_msgs__msg__MapBin__Sequence__fini(autoware_lanelet2_msgs__msg__MapBin__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_lanelet2_msgs__msg__MapBin__fini(&array->data[i]);
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

autoware_lanelet2_msgs__msg__MapBin__Sequence *
autoware_lanelet2_msgs__msg__MapBin__Sequence__create(size_t size)
{
  autoware_lanelet2_msgs__msg__MapBin__Sequence * array = (autoware_lanelet2_msgs__msg__MapBin__Sequence *)malloc(sizeof(autoware_lanelet2_msgs__msg__MapBin__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_lanelet2_msgs__msg__MapBin__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_lanelet2_msgs__msg__MapBin__Sequence__destroy(autoware_lanelet2_msgs__msg__MapBin__Sequence * array)
{
  if (array) {
    autoware_lanelet2_msgs__msg__MapBin__Sequence__fini(array);
  }
  free(array);
}
