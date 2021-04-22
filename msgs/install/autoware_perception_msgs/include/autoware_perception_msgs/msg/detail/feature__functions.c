// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/Feature.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/feature__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `cluster`
#include "sensor_msgs/msg/detail/point_cloud2__functions.h"
// Member `roi`
#include "sensor_msgs/msg/detail/region_of_interest__functions.h"

bool
autoware_perception_msgs__msg__Feature__init(autoware_perception_msgs__msg__Feature * msg)
{
  if (!msg) {
    return false;
  }
  // cluster
  if (!sensor_msgs__msg__PointCloud2__init(&msg->cluster)) {
    autoware_perception_msgs__msg__Feature__fini(msg);
    return false;
  }
  // roi
  if (!sensor_msgs__msg__RegionOfInterest__init(&msg->roi)) {
    autoware_perception_msgs__msg__Feature__fini(msg);
    return false;
  }
  return true;
}

void
autoware_perception_msgs__msg__Feature__fini(autoware_perception_msgs__msg__Feature * msg)
{
  if (!msg) {
    return;
  }
  // cluster
  sensor_msgs__msg__PointCloud2__fini(&msg->cluster);
  // roi
  sensor_msgs__msg__RegionOfInterest__fini(&msg->roi);
}

autoware_perception_msgs__msg__Feature *
autoware_perception_msgs__msg__Feature__create()
{
  autoware_perception_msgs__msg__Feature * msg = (autoware_perception_msgs__msg__Feature *)malloc(sizeof(autoware_perception_msgs__msg__Feature));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__Feature));
  bool success = autoware_perception_msgs__msg__Feature__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__Feature__destroy(autoware_perception_msgs__msg__Feature * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__Feature__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__Feature__Sequence__init(autoware_perception_msgs__msg__Feature__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__Feature * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__Feature *)calloc(size, sizeof(autoware_perception_msgs__msg__Feature));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__Feature__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__Feature__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__Feature__Sequence__fini(autoware_perception_msgs__msg__Feature__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__Feature__fini(&array->data[i]);
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

autoware_perception_msgs__msg__Feature__Sequence *
autoware_perception_msgs__msg__Feature__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__Feature__Sequence * array = (autoware_perception_msgs__msg__Feature__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__Feature__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__Feature__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__Feature__Sequence__destroy(autoware_perception_msgs__msg__Feature__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__Feature__Sequence__fini(array);
  }
  free(array);
}
