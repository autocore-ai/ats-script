// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_system_msgs:msg/TimeoutNotification.idl
// generated code does not contain a copyright notice
#include "autoware_system_msgs/msg/detail/timeout_notification__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
autoware_system_msgs__msg__TimeoutNotification__init(autoware_system_msgs__msg__TimeoutNotification * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    autoware_system_msgs__msg__TimeoutNotification__fini(msg);
    return false;
  }
  // is_timeout
  return true;
}

void
autoware_system_msgs__msg__TimeoutNotification__fini(autoware_system_msgs__msg__TimeoutNotification * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // is_timeout
}

autoware_system_msgs__msg__TimeoutNotification *
autoware_system_msgs__msg__TimeoutNotification__create()
{
  autoware_system_msgs__msg__TimeoutNotification * msg = (autoware_system_msgs__msg__TimeoutNotification *)malloc(sizeof(autoware_system_msgs__msg__TimeoutNotification));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_system_msgs__msg__TimeoutNotification));
  bool success = autoware_system_msgs__msg__TimeoutNotification__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_system_msgs__msg__TimeoutNotification__destroy(autoware_system_msgs__msg__TimeoutNotification * msg)
{
  if (msg) {
    autoware_system_msgs__msg__TimeoutNotification__fini(msg);
  }
  free(msg);
}


bool
autoware_system_msgs__msg__TimeoutNotification__Sequence__init(autoware_system_msgs__msg__TimeoutNotification__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_system_msgs__msg__TimeoutNotification * data = NULL;
  if (size) {
    data = (autoware_system_msgs__msg__TimeoutNotification *)calloc(size, sizeof(autoware_system_msgs__msg__TimeoutNotification));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_system_msgs__msg__TimeoutNotification__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_system_msgs__msg__TimeoutNotification__fini(&data[i - 1]);
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
autoware_system_msgs__msg__TimeoutNotification__Sequence__fini(autoware_system_msgs__msg__TimeoutNotification__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_system_msgs__msg__TimeoutNotification__fini(&array->data[i]);
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

autoware_system_msgs__msg__TimeoutNotification__Sequence *
autoware_system_msgs__msg__TimeoutNotification__Sequence__create(size_t size)
{
  autoware_system_msgs__msg__TimeoutNotification__Sequence * array = (autoware_system_msgs__msg__TimeoutNotification__Sequence *)malloc(sizeof(autoware_system_msgs__msg__TimeoutNotification__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_system_msgs__msg__TimeoutNotification__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_system_msgs__msg__TimeoutNotification__Sequence__destroy(autoware_system_msgs__msg__TimeoutNotification__Sequence * array)
{
  if (array) {
    autoware_system_msgs__msg__TimeoutNotification__Sequence__fini(array);
  }
  free(array);
}
