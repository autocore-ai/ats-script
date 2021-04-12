// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_control_msgs:msg/ControlCommandStamped.idl
// generated code does not contain a copyright notice
#include "autoware_control_msgs/msg/detail/control_command_stamped__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `control`
#include "autoware_control_msgs/msg/detail/control_command__functions.h"

bool
autoware_control_msgs__msg__ControlCommandStamped__init(autoware_control_msgs__msg__ControlCommandStamped * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    autoware_control_msgs__msg__ControlCommandStamped__fini(msg);
    return false;
  }
  // control
  if (!autoware_control_msgs__msg__ControlCommand__init(&msg->control)) {
    autoware_control_msgs__msg__ControlCommandStamped__fini(msg);
    return false;
  }
  return true;
}

void
autoware_control_msgs__msg__ControlCommandStamped__fini(autoware_control_msgs__msg__ControlCommandStamped * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // control
  autoware_control_msgs__msg__ControlCommand__fini(&msg->control);
}

autoware_control_msgs__msg__ControlCommandStamped *
autoware_control_msgs__msg__ControlCommandStamped__create()
{
  autoware_control_msgs__msg__ControlCommandStamped * msg = (autoware_control_msgs__msg__ControlCommandStamped *)malloc(sizeof(autoware_control_msgs__msg__ControlCommandStamped));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_control_msgs__msg__ControlCommandStamped));
  bool success = autoware_control_msgs__msg__ControlCommandStamped__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_control_msgs__msg__ControlCommandStamped__destroy(autoware_control_msgs__msg__ControlCommandStamped * msg)
{
  if (msg) {
    autoware_control_msgs__msg__ControlCommandStamped__fini(msg);
  }
  free(msg);
}


bool
autoware_control_msgs__msg__ControlCommandStamped__Sequence__init(autoware_control_msgs__msg__ControlCommandStamped__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_control_msgs__msg__ControlCommandStamped * data = NULL;
  if (size) {
    data = (autoware_control_msgs__msg__ControlCommandStamped *)calloc(size, sizeof(autoware_control_msgs__msg__ControlCommandStamped));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_control_msgs__msg__ControlCommandStamped__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_control_msgs__msg__ControlCommandStamped__fini(&data[i - 1]);
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
autoware_control_msgs__msg__ControlCommandStamped__Sequence__fini(autoware_control_msgs__msg__ControlCommandStamped__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_control_msgs__msg__ControlCommandStamped__fini(&array->data[i]);
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

autoware_control_msgs__msg__ControlCommandStamped__Sequence *
autoware_control_msgs__msg__ControlCommandStamped__Sequence__create(size_t size)
{
  autoware_control_msgs__msg__ControlCommandStamped__Sequence * array = (autoware_control_msgs__msg__ControlCommandStamped__Sequence *)malloc(sizeof(autoware_control_msgs__msg__ControlCommandStamped__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_control_msgs__msg__ControlCommandStamped__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_control_msgs__msg__ControlCommandStamped__Sequence__destroy(autoware_control_msgs__msg__ControlCommandStamped__Sequence * array)
{
  if (array) {
    autoware_control_msgs__msg__ControlCommandStamped__Sequence__fini(array);
  }
  free(array);
}
