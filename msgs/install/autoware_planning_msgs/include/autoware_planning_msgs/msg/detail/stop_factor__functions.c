// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_planning_msgs:msg/StopFactor.idl
// generated code does not contain a copyright notice
#include "autoware_planning_msgs/msg/detail/stop_factor__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `stop_pose`
#include "geometry_msgs/msg/detail/pose__functions.h"
// Member `stop_factor_points`
#include "geometry_msgs/msg/detail/point__functions.h"

bool
autoware_planning_msgs__msg__StopFactor__init(autoware_planning_msgs__msg__StopFactor * msg)
{
  if (!msg) {
    return false;
  }
  // stop_pose
  if (!geometry_msgs__msg__Pose__init(&msg->stop_pose)) {
    autoware_planning_msgs__msg__StopFactor__fini(msg);
    return false;
  }
  // dist_to_stop_pose
  // stop_factor_points
  if (!geometry_msgs__msg__Point__Sequence__init(&msg->stop_factor_points, 0)) {
    autoware_planning_msgs__msg__StopFactor__fini(msg);
    return false;
  }
  return true;
}

void
autoware_planning_msgs__msg__StopFactor__fini(autoware_planning_msgs__msg__StopFactor * msg)
{
  if (!msg) {
    return;
  }
  // stop_pose
  geometry_msgs__msg__Pose__fini(&msg->stop_pose);
  // dist_to_stop_pose
  // stop_factor_points
  geometry_msgs__msg__Point__Sequence__fini(&msg->stop_factor_points);
}

autoware_planning_msgs__msg__StopFactor *
autoware_planning_msgs__msg__StopFactor__create()
{
  autoware_planning_msgs__msg__StopFactor * msg = (autoware_planning_msgs__msg__StopFactor *)malloc(sizeof(autoware_planning_msgs__msg__StopFactor));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_planning_msgs__msg__StopFactor));
  bool success = autoware_planning_msgs__msg__StopFactor__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_planning_msgs__msg__StopFactor__destroy(autoware_planning_msgs__msg__StopFactor * msg)
{
  if (msg) {
    autoware_planning_msgs__msg__StopFactor__fini(msg);
  }
  free(msg);
}


bool
autoware_planning_msgs__msg__StopFactor__Sequence__init(autoware_planning_msgs__msg__StopFactor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_planning_msgs__msg__StopFactor * data = NULL;
  if (size) {
    data = (autoware_planning_msgs__msg__StopFactor *)calloc(size, sizeof(autoware_planning_msgs__msg__StopFactor));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_planning_msgs__msg__StopFactor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_planning_msgs__msg__StopFactor__fini(&data[i - 1]);
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
autoware_planning_msgs__msg__StopFactor__Sequence__fini(autoware_planning_msgs__msg__StopFactor__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_planning_msgs__msg__StopFactor__fini(&array->data[i]);
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

autoware_planning_msgs__msg__StopFactor__Sequence *
autoware_planning_msgs__msg__StopFactor__Sequence__create(size_t size)
{
  autoware_planning_msgs__msg__StopFactor__Sequence * array = (autoware_planning_msgs__msg__StopFactor__Sequence *)malloc(sizeof(autoware_planning_msgs__msg__StopFactor__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_planning_msgs__msg__StopFactor__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_planning_msgs__msg__StopFactor__Sequence__destroy(autoware_planning_msgs__msg__StopFactor__Sequence * array)
{
  if (array) {
    autoware_planning_msgs__msg__StopFactor__Sequence__fini(array);
  }
  free(array);
}
