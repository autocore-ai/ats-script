// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_debug_msgs:msg/Float32MultiArrayStamped.idl
// generated code does not contain a copyright notice
#include "autoware_debug_msgs/msg/detail/float32_multi_array_stamped__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
autoware_debug_msgs__msg__Float32MultiArrayStamped__init(autoware_debug_msgs__msg__Float32MultiArrayStamped * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    autoware_debug_msgs__msg__Float32MultiArrayStamped__fini(msg);
    return false;
  }
  // data
  if (!rosidl_runtime_c__float__Sequence__init(&msg->data, 0)) {
    autoware_debug_msgs__msg__Float32MultiArrayStamped__fini(msg);
    return false;
  }
  return true;
}

void
autoware_debug_msgs__msg__Float32MultiArrayStamped__fini(autoware_debug_msgs__msg__Float32MultiArrayStamped * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // data
  rosidl_runtime_c__float__Sequence__fini(&msg->data);
}

autoware_debug_msgs__msg__Float32MultiArrayStamped *
autoware_debug_msgs__msg__Float32MultiArrayStamped__create()
{
  autoware_debug_msgs__msg__Float32MultiArrayStamped * msg = (autoware_debug_msgs__msg__Float32MultiArrayStamped *)malloc(sizeof(autoware_debug_msgs__msg__Float32MultiArrayStamped));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_debug_msgs__msg__Float32MultiArrayStamped));
  bool success = autoware_debug_msgs__msg__Float32MultiArrayStamped__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_debug_msgs__msg__Float32MultiArrayStamped__destroy(autoware_debug_msgs__msg__Float32MultiArrayStamped * msg)
{
  if (msg) {
    autoware_debug_msgs__msg__Float32MultiArrayStamped__fini(msg);
  }
  free(msg);
}


bool
autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence__init(autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_debug_msgs__msg__Float32MultiArrayStamped * data = NULL;
  if (size) {
    data = (autoware_debug_msgs__msg__Float32MultiArrayStamped *)calloc(size, sizeof(autoware_debug_msgs__msg__Float32MultiArrayStamped));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_debug_msgs__msg__Float32MultiArrayStamped__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_debug_msgs__msg__Float32MultiArrayStamped__fini(&data[i - 1]);
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
autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence__fini(autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_debug_msgs__msg__Float32MultiArrayStamped__fini(&array->data[i]);
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

autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence *
autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence__create(size_t size)
{
  autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence * array = (autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence *)malloc(sizeof(autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence__destroy(autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence * array)
{
  if (array) {
    autoware_debug_msgs__msg__Float32MultiArrayStamped__Sequence__fini(array);
  }
  free(array);
}
