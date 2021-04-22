// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_planning_msgs:msg/Route.idl
// generated code does not contain a copyright notice
#include "autoware_planning_msgs/msg/detail/route__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `goal_pose`
#include "geometry_msgs/msg/detail/pose__functions.h"
// Member `route_sections`
#include "autoware_planning_msgs/msg/detail/route_section__functions.h"

bool
autoware_planning_msgs__msg__Route__init(autoware_planning_msgs__msg__Route * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    autoware_planning_msgs__msg__Route__fini(msg);
    return false;
  }
  // goal_pose
  if (!geometry_msgs__msg__Pose__init(&msg->goal_pose)) {
    autoware_planning_msgs__msg__Route__fini(msg);
    return false;
  }
  // route_sections
  if (!autoware_planning_msgs__msg__RouteSection__Sequence__init(&msg->route_sections, 0)) {
    autoware_planning_msgs__msg__Route__fini(msg);
    return false;
  }
  return true;
}

void
autoware_planning_msgs__msg__Route__fini(autoware_planning_msgs__msg__Route * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // goal_pose
  geometry_msgs__msg__Pose__fini(&msg->goal_pose);
  // route_sections
  autoware_planning_msgs__msg__RouteSection__Sequence__fini(&msg->route_sections);
}

autoware_planning_msgs__msg__Route *
autoware_planning_msgs__msg__Route__create()
{
  autoware_planning_msgs__msg__Route * msg = (autoware_planning_msgs__msg__Route *)malloc(sizeof(autoware_planning_msgs__msg__Route));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_planning_msgs__msg__Route));
  bool success = autoware_planning_msgs__msg__Route__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_planning_msgs__msg__Route__destroy(autoware_planning_msgs__msg__Route * msg)
{
  if (msg) {
    autoware_planning_msgs__msg__Route__fini(msg);
  }
  free(msg);
}


bool
autoware_planning_msgs__msg__Route__Sequence__init(autoware_planning_msgs__msg__Route__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_planning_msgs__msg__Route * data = NULL;
  if (size) {
    data = (autoware_planning_msgs__msg__Route *)calloc(size, sizeof(autoware_planning_msgs__msg__Route));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_planning_msgs__msg__Route__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_planning_msgs__msg__Route__fini(&data[i - 1]);
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
autoware_planning_msgs__msg__Route__Sequence__fini(autoware_planning_msgs__msg__Route__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_planning_msgs__msg__Route__fini(&array->data[i]);
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

autoware_planning_msgs__msg__Route__Sequence *
autoware_planning_msgs__msg__Route__Sequence__create(size_t size)
{
  autoware_planning_msgs__msg__Route__Sequence * array = (autoware_planning_msgs__msg__Route__Sequence *)malloc(sizeof(autoware_planning_msgs__msg__Route__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_planning_msgs__msg__Route__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_planning_msgs__msg__Route__Sequence__destroy(autoware_planning_msgs__msg__Route__Sequence * array)
{
  if (array) {
    autoware_planning_msgs__msg__Route__Sequence__fini(array);
  }
  free(array);
}
