// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_system_msgs:msg/AutowareVersion.idl
// generated code does not contain a copyright notice
#include "autoware_system_msgs/msg/detail/autoware_version__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `ros_distro`
#include "rosidl_runtime_c/string_functions.h"

bool
autoware_system_msgs__msg__AutowareVersion__init(autoware_system_msgs__msg__AutowareVersion * msg)
{
  if (!msg) {
    return false;
  }
  // ros_version
  msg->ros_version = 0ul;
  // ros_distro
  if (!rosidl_runtime_c__String__init(&msg->ros_distro)) {
    autoware_system_msgs__msg__AutowareVersion__fini(msg);
    return false;
  }
  {
    bool success = rosidl_runtime_c__String__assign(&msg->ros_distro, "");
    if (!success) {
      goto abort_init_0;
    }
  }
  return true;
abort_init_0:
  return false;
}

void
autoware_system_msgs__msg__AutowareVersion__fini(autoware_system_msgs__msg__AutowareVersion * msg)
{
  if (!msg) {
    return;
  }
  // ros_version
  // ros_distro
  rosidl_runtime_c__String__fini(&msg->ros_distro);
}

autoware_system_msgs__msg__AutowareVersion *
autoware_system_msgs__msg__AutowareVersion__create()
{
  autoware_system_msgs__msg__AutowareVersion * msg = (autoware_system_msgs__msg__AutowareVersion *)malloc(sizeof(autoware_system_msgs__msg__AutowareVersion));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_system_msgs__msg__AutowareVersion));
  bool success = autoware_system_msgs__msg__AutowareVersion__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_system_msgs__msg__AutowareVersion__destroy(autoware_system_msgs__msg__AutowareVersion * msg)
{
  if (msg) {
    autoware_system_msgs__msg__AutowareVersion__fini(msg);
  }
  free(msg);
}


bool
autoware_system_msgs__msg__AutowareVersion__Sequence__init(autoware_system_msgs__msg__AutowareVersion__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_system_msgs__msg__AutowareVersion * data = NULL;
  if (size) {
    data = (autoware_system_msgs__msg__AutowareVersion *)calloc(size, sizeof(autoware_system_msgs__msg__AutowareVersion));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_system_msgs__msg__AutowareVersion__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_system_msgs__msg__AutowareVersion__fini(&data[i - 1]);
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
autoware_system_msgs__msg__AutowareVersion__Sequence__fini(autoware_system_msgs__msg__AutowareVersion__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_system_msgs__msg__AutowareVersion__fini(&array->data[i]);
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

autoware_system_msgs__msg__AutowareVersion__Sequence *
autoware_system_msgs__msg__AutowareVersion__Sequence__create(size_t size)
{
  autoware_system_msgs__msg__AutowareVersion__Sequence * array = (autoware_system_msgs__msg__AutowareVersion__Sequence *)malloc(sizeof(autoware_system_msgs__msg__AutowareVersion__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_system_msgs__msg__AutowareVersion__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_system_msgs__msg__AutowareVersion__Sequence__destroy(autoware_system_msgs__msg__AutowareVersion__Sequence * array)
{
  if (array) {
    autoware_system_msgs__msg__AutowareVersion__Sequence__fini(array);
  }
  free(array);
}
