// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_planning_msgs:msg/RouteSection.idl
// generated code does not contain a copyright notice
#include "autoware_planning_msgs/msg/detail/route_section__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `lane_ids`
// Member `continued_lane_ids`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
autoware_planning_msgs__msg__RouteSection__init(autoware_planning_msgs__msg__RouteSection * msg)
{
  if (!msg) {
    return false;
  }
  // lane_ids
  if (!rosidl_runtime_c__int64__Sequence__init(&msg->lane_ids, 0)) {
    autoware_planning_msgs__msg__RouteSection__fini(msg);
    return false;
  }
  // preferred_lane_id
  // continued_lane_ids
  if (!rosidl_runtime_c__int64__Sequence__init(&msg->continued_lane_ids, 0)) {
    autoware_planning_msgs__msg__RouteSection__fini(msg);
    return false;
  }
  return true;
}

void
autoware_planning_msgs__msg__RouteSection__fini(autoware_planning_msgs__msg__RouteSection * msg)
{
  if (!msg) {
    return;
  }
  // lane_ids
  rosidl_runtime_c__int64__Sequence__fini(&msg->lane_ids);
  // preferred_lane_id
  // continued_lane_ids
  rosidl_runtime_c__int64__Sequence__fini(&msg->continued_lane_ids);
}

autoware_planning_msgs__msg__RouteSection *
autoware_planning_msgs__msg__RouteSection__create()
{
  autoware_planning_msgs__msg__RouteSection * msg = (autoware_planning_msgs__msg__RouteSection *)malloc(sizeof(autoware_planning_msgs__msg__RouteSection));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_planning_msgs__msg__RouteSection));
  bool success = autoware_planning_msgs__msg__RouteSection__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_planning_msgs__msg__RouteSection__destroy(autoware_planning_msgs__msg__RouteSection * msg)
{
  if (msg) {
    autoware_planning_msgs__msg__RouteSection__fini(msg);
  }
  free(msg);
}


bool
autoware_planning_msgs__msg__RouteSection__Sequence__init(autoware_planning_msgs__msg__RouteSection__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_planning_msgs__msg__RouteSection * data = NULL;
  if (size) {
    data = (autoware_planning_msgs__msg__RouteSection *)calloc(size, sizeof(autoware_planning_msgs__msg__RouteSection));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_planning_msgs__msg__RouteSection__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_planning_msgs__msg__RouteSection__fini(&data[i - 1]);
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
autoware_planning_msgs__msg__RouteSection__Sequence__fini(autoware_planning_msgs__msg__RouteSection__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_planning_msgs__msg__RouteSection__fini(&array->data[i]);
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

autoware_planning_msgs__msg__RouteSection__Sequence *
autoware_planning_msgs__msg__RouteSection__Sequence__create(size_t size)
{
  autoware_planning_msgs__msg__RouteSection__Sequence * array = (autoware_planning_msgs__msg__RouteSection__Sequence *)malloc(sizeof(autoware_planning_msgs__msg__RouteSection__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_planning_msgs__msg__RouteSection__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_planning_msgs__msg__RouteSection__Sequence__destroy(autoware_planning_msgs__msg__RouteSection__Sequence * array)
{
  if (array) {
    autoware_planning_msgs__msg__RouteSection__Sequence__fini(array);
  }
  free(array);
}
