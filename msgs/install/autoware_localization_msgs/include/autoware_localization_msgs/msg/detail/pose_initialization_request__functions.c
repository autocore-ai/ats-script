// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_localization_msgs:msg/PoseInitializationRequest.idl
// generated code does not contain a copyright notice
#include "autoware_localization_msgs/msg/detail/pose_initialization_request__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
autoware_localization_msgs__msg__PoseInitializationRequest__init(autoware_localization_msgs__msg__PoseInitializationRequest * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    autoware_localization_msgs__msg__PoseInitializationRequest__fini(msg);
    return false;
  }
  // data
  return true;
}

void
autoware_localization_msgs__msg__PoseInitializationRequest__fini(autoware_localization_msgs__msg__PoseInitializationRequest * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // data
}

autoware_localization_msgs__msg__PoseInitializationRequest *
autoware_localization_msgs__msg__PoseInitializationRequest__create()
{
  autoware_localization_msgs__msg__PoseInitializationRequest * msg = (autoware_localization_msgs__msg__PoseInitializationRequest *)malloc(sizeof(autoware_localization_msgs__msg__PoseInitializationRequest));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_localization_msgs__msg__PoseInitializationRequest));
  bool success = autoware_localization_msgs__msg__PoseInitializationRequest__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_localization_msgs__msg__PoseInitializationRequest__destroy(autoware_localization_msgs__msg__PoseInitializationRequest * msg)
{
  if (msg) {
    autoware_localization_msgs__msg__PoseInitializationRequest__fini(msg);
  }
  free(msg);
}


bool
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__init(autoware_localization_msgs__msg__PoseInitializationRequest__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_localization_msgs__msg__PoseInitializationRequest * data = NULL;
  if (size) {
    data = (autoware_localization_msgs__msg__PoseInitializationRequest *)calloc(size, sizeof(autoware_localization_msgs__msg__PoseInitializationRequest));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_localization_msgs__msg__PoseInitializationRequest__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_localization_msgs__msg__PoseInitializationRequest__fini(&data[i - 1]);
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
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__fini(autoware_localization_msgs__msg__PoseInitializationRequest__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_localization_msgs__msg__PoseInitializationRequest__fini(&array->data[i]);
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

autoware_localization_msgs__msg__PoseInitializationRequest__Sequence *
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__create(size_t size)
{
  autoware_localization_msgs__msg__PoseInitializationRequest__Sequence * array = (autoware_localization_msgs__msg__PoseInitializationRequest__Sequence *)malloc(sizeof(autoware_localization_msgs__msg__PoseInitializationRequest__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__destroy(autoware_localization_msgs__msg__PoseInitializationRequest__Sequence * array)
{
  if (array) {
    autoware_localization_msgs__msg__PoseInitializationRequest__Sequence__fini(array);
  }
  free(array);
}
