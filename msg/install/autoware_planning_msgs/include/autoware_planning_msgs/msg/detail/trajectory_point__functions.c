// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_planning_msgs:msg/TrajectoryPoint.idl
// generated code does not contain a copyright notice
#include "autoware_planning_msgs/msg/detail/trajectory_point__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/detail/pose__functions.h"
// Member `twist`
#include "geometry_msgs/msg/detail/twist__functions.h"
// Member `accel`
#include "geometry_msgs/msg/detail/accel__functions.h"

bool
autoware_planning_msgs__msg__TrajectoryPoint__init(autoware_planning_msgs__msg__TrajectoryPoint * msg)
{
  if (!msg) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__init(&msg->pose)) {
    autoware_planning_msgs__msg__TrajectoryPoint__fini(msg);
    return false;
  }
  // twist
  if (!geometry_msgs__msg__Twist__init(&msg->twist)) {
    autoware_planning_msgs__msg__TrajectoryPoint__fini(msg);
    return false;
  }
  // accel
  if (!geometry_msgs__msg__Accel__init(&msg->accel)) {
    autoware_planning_msgs__msg__TrajectoryPoint__fini(msg);
    return false;
  }
  return true;
}

void
autoware_planning_msgs__msg__TrajectoryPoint__fini(autoware_planning_msgs__msg__TrajectoryPoint * msg)
{
  if (!msg) {
    return;
  }
  // pose
  geometry_msgs__msg__Pose__fini(&msg->pose);
  // twist
  geometry_msgs__msg__Twist__fini(&msg->twist);
  // accel
  geometry_msgs__msg__Accel__fini(&msg->accel);
}

autoware_planning_msgs__msg__TrajectoryPoint *
autoware_planning_msgs__msg__TrajectoryPoint__create()
{
  autoware_planning_msgs__msg__TrajectoryPoint * msg = (autoware_planning_msgs__msg__TrajectoryPoint *)malloc(sizeof(autoware_planning_msgs__msg__TrajectoryPoint));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_planning_msgs__msg__TrajectoryPoint));
  bool success = autoware_planning_msgs__msg__TrajectoryPoint__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_planning_msgs__msg__TrajectoryPoint__destroy(autoware_planning_msgs__msg__TrajectoryPoint * msg)
{
  if (msg) {
    autoware_planning_msgs__msg__TrajectoryPoint__fini(msg);
  }
  free(msg);
}


bool
autoware_planning_msgs__msg__TrajectoryPoint__Sequence__init(autoware_planning_msgs__msg__TrajectoryPoint__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_planning_msgs__msg__TrajectoryPoint * data = NULL;
  if (size) {
    data = (autoware_planning_msgs__msg__TrajectoryPoint *)calloc(size, sizeof(autoware_planning_msgs__msg__TrajectoryPoint));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_planning_msgs__msg__TrajectoryPoint__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_planning_msgs__msg__TrajectoryPoint__fini(&data[i - 1]);
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
autoware_planning_msgs__msg__TrajectoryPoint__Sequence__fini(autoware_planning_msgs__msg__TrajectoryPoint__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_planning_msgs__msg__TrajectoryPoint__fini(&array->data[i]);
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

autoware_planning_msgs__msg__TrajectoryPoint__Sequence *
autoware_planning_msgs__msg__TrajectoryPoint__Sequence__create(size_t size)
{
  autoware_planning_msgs__msg__TrajectoryPoint__Sequence * array = (autoware_planning_msgs__msg__TrajectoryPoint__Sequence *)malloc(sizeof(autoware_planning_msgs__msg__TrajectoryPoint__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_planning_msgs__msg__TrajectoryPoint__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_planning_msgs__msg__TrajectoryPoint__Sequence__destroy(autoware_planning_msgs__msg__TrajectoryPoint__Sequence * array)
{
  if (array) {
    autoware_planning_msgs__msg__TrajectoryPoint__Sequence__fini(array);
  }
  free(array);
}
