// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/TrafficLightRoi.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/traffic_light_roi__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `roi`
#include "sensor_msgs/msg/detail/region_of_interest__functions.h"

bool
autoware_perception_msgs__msg__TrafficLightRoi__init(autoware_perception_msgs__msg__TrafficLightRoi * msg)
{
  if (!msg) {
    return false;
  }
  // roi
  if (!sensor_msgs__msg__RegionOfInterest__init(&msg->roi)) {
    autoware_perception_msgs__msg__TrafficLightRoi__fini(msg);
    return false;
  }
  // id
  return true;
}

void
autoware_perception_msgs__msg__TrafficLightRoi__fini(autoware_perception_msgs__msg__TrafficLightRoi * msg)
{
  if (!msg) {
    return;
  }
  // roi
  sensor_msgs__msg__RegionOfInterest__fini(&msg->roi);
  // id
}

autoware_perception_msgs__msg__TrafficLightRoi *
autoware_perception_msgs__msg__TrafficLightRoi__create()
{
  autoware_perception_msgs__msg__TrafficLightRoi * msg = (autoware_perception_msgs__msg__TrafficLightRoi *)malloc(sizeof(autoware_perception_msgs__msg__TrafficLightRoi));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__TrafficLightRoi));
  bool success = autoware_perception_msgs__msg__TrafficLightRoi__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__TrafficLightRoi__destroy(autoware_perception_msgs__msg__TrafficLightRoi * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__TrafficLightRoi__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__TrafficLightRoi__Sequence__init(autoware_perception_msgs__msg__TrafficLightRoi__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__TrafficLightRoi * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__TrafficLightRoi *)calloc(size, sizeof(autoware_perception_msgs__msg__TrafficLightRoi));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__TrafficLightRoi__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__TrafficLightRoi__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__TrafficLightRoi__Sequence__fini(autoware_perception_msgs__msg__TrafficLightRoi__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__TrafficLightRoi__fini(&array->data[i]);
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

autoware_perception_msgs__msg__TrafficLightRoi__Sequence *
autoware_perception_msgs__msg__TrafficLightRoi__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__TrafficLightRoi__Sequence * array = (autoware_perception_msgs__msg__TrafficLightRoi__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__TrafficLightRoi__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__TrafficLightRoi__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__TrafficLightRoi__Sequence__destroy(autoware_perception_msgs__msg__TrafficLightRoi__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__TrafficLightRoi__Sequence__fini(array);
  }
  free(array);
}
