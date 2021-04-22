// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_perception_msgs:msg/State.idl
// generated code does not contain a copyright notice
#include "autoware_perception_msgs/msg/detail/state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `pose_covariance`
#include "geometry_msgs/msg/detail/pose_with_covariance__functions.h"
// Member `twist_covariance`
#include "geometry_msgs/msg/detail/twist_with_covariance__functions.h"
// Member `acceleration_covariance`
#include "geometry_msgs/msg/detail/accel_with_covariance__functions.h"
// Member `predicted_paths`
#include "autoware_perception_msgs/msg/detail/predicted_path__functions.h"

bool
autoware_perception_msgs__msg__State__init(autoware_perception_msgs__msg__State * msg)
{
  if (!msg) {
    return false;
  }
  // pose_covariance
  if (!geometry_msgs__msg__PoseWithCovariance__init(&msg->pose_covariance)) {
    autoware_perception_msgs__msg__State__fini(msg);
    return false;
  }
  // orientation_reliable
  // twist_covariance
  if (!geometry_msgs__msg__TwistWithCovariance__init(&msg->twist_covariance)) {
    autoware_perception_msgs__msg__State__fini(msg);
    return false;
  }
  // twist_reliable
  // acceleration_covariance
  if (!geometry_msgs__msg__AccelWithCovariance__init(&msg->acceleration_covariance)) {
    autoware_perception_msgs__msg__State__fini(msg);
    return false;
  }
  // acceleration_reliable
  // predicted_paths
  if (!autoware_perception_msgs__msg__PredictedPath__Sequence__init(&msg->predicted_paths, 0)) {
    autoware_perception_msgs__msg__State__fini(msg);
    return false;
  }
  return true;
}

void
autoware_perception_msgs__msg__State__fini(autoware_perception_msgs__msg__State * msg)
{
  if (!msg) {
    return;
  }
  // pose_covariance
  geometry_msgs__msg__PoseWithCovariance__fini(&msg->pose_covariance);
  // orientation_reliable
  // twist_covariance
  geometry_msgs__msg__TwistWithCovariance__fini(&msg->twist_covariance);
  // twist_reliable
  // acceleration_covariance
  geometry_msgs__msg__AccelWithCovariance__fini(&msg->acceleration_covariance);
  // acceleration_reliable
  // predicted_paths
  autoware_perception_msgs__msg__PredictedPath__Sequence__fini(&msg->predicted_paths);
}

autoware_perception_msgs__msg__State *
autoware_perception_msgs__msg__State__create()
{
  autoware_perception_msgs__msg__State * msg = (autoware_perception_msgs__msg__State *)malloc(sizeof(autoware_perception_msgs__msg__State));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_perception_msgs__msg__State));
  bool success = autoware_perception_msgs__msg__State__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_perception_msgs__msg__State__destroy(autoware_perception_msgs__msg__State * msg)
{
  if (msg) {
    autoware_perception_msgs__msg__State__fini(msg);
  }
  free(msg);
}


bool
autoware_perception_msgs__msg__State__Sequence__init(autoware_perception_msgs__msg__State__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_perception_msgs__msg__State * data = NULL;
  if (size) {
    data = (autoware_perception_msgs__msg__State *)calloc(size, sizeof(autoware_perception_msgs__msg__State));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_perception_msgs__msg__State__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_perception_msgs__msg__State__fini(&data[i - 1]);
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
autoware_perception_msgs__msg__State__Sequence__fini(autoware_perception_msgs__msg__State__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_perception_msgs__msg__State__fini(&array->data[i]);
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

autoware_perception_msgs__msg__State__Sequence *
autoware_perception_msgs__msg__State__Sequence__create(size_t size)
{
  autoware_perception_msgs__msg__State__Sequence * array = (autoware_perception_msgs__msg__State__Sequence *)malloc(sizeof(autoware_perception_msgs__msg__State__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_perception_msgs__msg__State__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_perception_msgs__msg__State__Sequence__destroy(autoware_perception_msgs__msg__State__Sequence * array)
{
  if (array) {
    autoware_perception_msgs__msg__State__Sequence__fini(array);
  }
  free(array);
}
