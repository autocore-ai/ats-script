// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_vehicle_msgs:msg/RawControlCommand.idl
// generated code does not contain a copyright notice
#include "autoware_vehicle_msgs/msg/detail/raw_control_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
autoware_vehicle_msgs__msg__RawControlCommand__init(autoware_vehicle_msgs__msg__RawControlCommand * msg)
{
  if (!msg) {
    return false;
  }
  // steering_angle
  // steering_angle_velocity
  // throttle
  // brake
  return true;
}

void
autoware_vehicle_msgs__msg__RawControlCommand__fini(autoware_vehicle_msgs__msg__RawControlCommand * msg)
{
  if (!msg) {
    return;
  }
  // steering_angle
  // steering_angle_velocity
  // throttle
  // brake
}

autoware_vehicle_msgs__msg__RawControlCommand *
autoware_vehicle_msgs__msg__RawControlCommand__create()
{
  autoware_vehicle_msgs__msg__RawControlCommand * msg = (autoware_vehicle_msgs__msg__RawControlCommand *)malloc(sizeof(autoware_vehicle_msgs__msg__RawControlCommand));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_vehicle_msgs__msg__RawControlCommand));
  bool success = autoware_vehicle_msgs__msg__RawControlCommand__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_vehicle_msgs__msg__RawControlCommand__destroy(autoware_vehicle_msgs__msg__RawControlCommand * msg)
{
  if (msg) {
    autoware_vehicle_msgs__msg__RawControlCommand__fini(msg);
  }
  free(msg);
}


bool
autoware_vehicle_msgs__msg__RawControlCommand__Sequence__init(autoware_vehicle_msgs__msg__RawControlCommand__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_vehicle_msgs__msg__RawControlCommand * data = NULL;
  if (size) {
    data = (autoware_vehicle_msgs__msg__RawControlCommand *)calloc(size, sizeof(autoware_vehicle_msgs__msg__RawControlCommand));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_vehicle_msgs__msg__RawControlCommand__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_vehicle_msgs__msg__RawControlCommand__fini(&data[i - 1]);
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
autoware_vehicle_msgs__msg__RawControlCommand__Sequence__fini(autoware_vehicle_msgs__msg__RawControlCommand__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_vehicle_msgs__msg__RawControlCommand__fini(&array->data[i]);
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

autoware_vehicle_msgs__msg__RawControlCommand__Sequence *
autoware_vehicle_msgs__msg__RawControlCommand__Sequence__create(size_t size)
{
  autoware_vehicle_msgs__msg__RawControlCommand__Sequence * array = (autoware_vehicle_msgs__msg__RawControlCommand__Sequence *)malloc(sizeof(autoware_vehicle_msgs__msg__RawControlCommand__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_vehicle_msgs__msg__RawControlCommand__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_vehicle_msgs__msg__RawControlCommand__Sequence__destroy(autoware_vehicle_msgs__msg__RawControlCommand__Sequence * array)
{
  if (array) {
    autoware_vehicle_msgs__msg__RawControlCommand__Sequence__fini(array);
  }
  free(array);
}
