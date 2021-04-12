// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/TrafficLightStateArray.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/traffic_light_state_array__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `states`
#include "autoware_perception_msgs/msg/detail/traffic_light_state__functions.h"

bool
autoware_perception_msgs__msg__TrafficLightStateArray__init(autoware_perception_msgs__msg__TrafficLightStateArray * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    autoware_perception_msgs__msg__TrafficLightStateArray__fini(msg);
    return false;
  }
  // states
  if (!autoware_perception_msgs__msg__TrafficLightState__Sequence__init(&msg->states, 0)) {
    autoware_perception_msgs__msg__TrafficLightStateArray__fini(msg);
    return false;
  }
  return true;
}

void
autoware_perception_msgs__msg__TrafficLightStateArray__fini(autoware_perception_msgs__msg__TrafficLightStateArray * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // states
  autoware_perception_msgs__msg__TrafficLightState__Sequence__fini(&msg->states);
}

autoware_perception_msgs__msg__TrafficLightStateArray *
autoware_perception_msgs__msg__TrafficLightStateArray__create()
{
  autoware_perception_msgs__msg__TrafficLightStateArray * msg = (autoware_perception_msgs__msg__TrafficLightStateArray *)malloc(sizeof(autoware_perception_msgs__msg__TrafficLightStateArray));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__TrafficLightStateArray));
  bool success = autoware_perception_msgs__msg__TrafficLightStateArray__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__TrafficLightStateArray__destroy(autoware_perception_msgs__msg__TrafficLightStateArray * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__TrafficLightStateArray__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__TrafficLightStateArray__Sequence__init(autoware_perception_msgs__msg__TrafficLightStateArray__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__TrafficLightStateArray * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__TrafficLightStateArray *)calloc(size, sizeof(autoware_perception_msgs__msg__TrafficLightStateArray));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__TrafficLightStateArray__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__TrafficLightStateArray__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__TrafficLightStateArray__Sequence__fini(autoware_perception_msgs__msg__TrafficLightStateArray__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__TrafficLightStateArray__fini(&array->data[i]);
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

autoware_perception_msgs__msg__TrafficLightStateArray__Sequence *
autoware_perception_msgs__msg__TrafficLightStateArray__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__TrafficLightStateArray__Sequence * array = (autoware_perception_msgs__msg__TrafficLightStateArray__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__TrafficLightStateArray__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__TrafficLightStateArray__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__TrafficLightStateArray__Sequence__destroy(autoware_perception_msgs__msg__TrafficLightStateArray__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__TrafficLightStateArray__Sequence__fini(array);
  }
  free(array);
}
