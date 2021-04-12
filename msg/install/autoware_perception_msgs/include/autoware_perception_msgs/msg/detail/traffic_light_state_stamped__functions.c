// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/TrafficLightStateStamped.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/traffic_light_state_stamped__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `state`
#include "autoware_perception_msgs/msg/detail/traffic_light_state__functions.h"

bool
autoware_perception_msgs__msg__TrafficLightStateStamped__init(autoware_perception_msgs__msg__TrafficLightStateStamped * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    autoware_perception_msgs__msg__TrafficLightStateStamped__fini(msg);
    return false;
  }
  // state
  if (!autoware_perception_msgs__msg__TrafficLightState__init(&msg->state)) {
    autoware_perception_msgs__msg__TrafficLightStateStamped__fini(msg);
    return false;
  }
  return true;
}

void
autoware_perception_msgs__msg__TrafficLightStateStamped__fini(autoware_perception_msgs__msg__TrafficLightStateStamped * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // state
  autoware_perception_msgs__msg__TrafficLightState__fini(&msg->state);
}

autoware_perception_msgs__msg__TrafficLightStateStamped *
autoware_perception_msgs__msg__TrafficLightStateStamped__create()
{
  autoware_perception_msgs__msg__TrafficLightStateStamped * msg = (autoware_perception_msgs__msg__TrafficLightStateStamped *)malloc(sizeof(autoware_perception_msgs__msg__TrafficLightStateStamped));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__TrafficLightStateStamped));
  bool success = autoware_perception_msgs__msg__TrafficLightStateStamped__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__TrafficLightStateStamped__destroy(autoware_perception_msgs__msg__TrafficLightStateStamped * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__TrafficLightStateStamped__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence__init(autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__TrafficLightStateStamped * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__TrafficLightStateStamped *)calloc(size, sizeof(autoware_perception_msgs__msg__TrafficLightStateStamped));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__TrafficLightStateStamped__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__TrafficLightStateStamped__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence__fini(autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__TrafficLightStateStamped__fini(&array->data[i]);
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

autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence *
autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence * array = (autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence__destroy(autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__TrafficLightStateStamped__Sequence__fini(array);
  }
  free(array);
}
