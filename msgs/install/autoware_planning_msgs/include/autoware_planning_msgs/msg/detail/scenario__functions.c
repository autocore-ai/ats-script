// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_planning_msgs:msg/Scenario.idl
// generated code does not contain a copyright notice
#include "autoware_planning_msgs/msg/detail/scenario__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `current_scenario`
// Member `activating_scenarios`
#include "rosidl_runtime_c/string_functions.h"

bool
autoware_planning_msgs__msg__Scenario__init(autoware_planning_msgs__msg__Scenario * msg)
{
  if (!msg) {
    return false;
  }
  // current_scenario
  if (!rosidl_runtime_c__String__init(&msg->current_scenario)) {
    autoware_planning_msgs__msg__Scenario__fini(msg);
    return false;
  }
  // activating_scenarios
  if (!rosidl_runtime_c__String__Sequence__init(&msg->activating_scenarios, 0)) {
    autoware_planning_msgs__msg__Scenario__fini(msg);
    return false;
  }
  return true;
}

void
autoware_planning_msgs__msg__Scenario__fini(autoware_planning_msgs__msg__Scenario * msg)
{
  if (!msg) {
    return;
  }
  // current_scenario
  rosidl_runtime_c__String__fini(&msg->current_scenario);
  // activating_scenarios
  rosidl_runtime_c__String__Sequence__fini(&msg->activating_scenarios);
}

autoware_planning_msgs__msg__Scenario *
autoware_planning_msgs__msg__Scenario__create()
{
  autoware_planning_msgs__msg__Scenario * msg = (autoware_planning_msgs__msg__Scenario *)malloc(sizeof(autoware_planning_msgs__msg__Scenario));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_planning_msgs__msg__Scenario));
  bool success = autoware_planning_msgs__msg__Scenario__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_planning_msgs__msg__Scenario__destroy(autoware_planning_msgs__msg__Scenario * msg)
{
  if (msg) {
    autoware_planning_msgs__msg__Scenario__fini(msg);
  }
  free(msg);
}


bool
autoware_planning_msgs__msg__Scenario__Sequence__init(autoware_planning_msgs__msg__Scenario__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_planning_msgs__msg__Scenario * data = NULL;
  if (size) {
    data = (autoware_planning_msgs__msg__Scenario *)calloc(size, sizeof(autoware_planning_msgs__msg__Scenario));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_planning_msgs__msg__Scenario__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_planning_msgs__msg__Scenario__fini(&data[i - 1]);
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
autoware_planning_msgs__msg__Scenario__Sequence__fini(autoware_planning_msgs__msg__Scenario__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_planning_msgs__msg__Scenario__fini(&array->data[i]);
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

autoware_planning_msgs__msg__Scenario__Sequence *
autoware_planning_msgs__msg__Scenario__Sequence__create(size_t size)
{
  autoware_planning_msgs__msg__Scenario__Sequence * array = (autoware_planning_msgs__msg__Scenario__Sequence *)malloc(sizeof(autoware_planning_msgs__msg__Scenario__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_planning_msgs__msg__Scenario__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_planning_msgs__msg__Scenario__Sequence__destroy(autoware_planning_msgs__msg__Scenario__Sequence * array)
{
  if (array) {
    autoware_planning_msgs__msg__Scenario__Sequence__fini(array);
  }
  free(array);
}
