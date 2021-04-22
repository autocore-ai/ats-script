// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from autoware_vehicle_msgs:msg/BatteryStatus.idl
// generated code does not contain a copyright notice
#include "autoware_vehicle_msgs/msg/detail/battery_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
autoware_vehicle_msgs__msg__BatteryStatus__init(autoware_vehicle_msgs__msg__BatteryStatus * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    autoware_vehicle_msgs__msg__BatteryStatus__fini(msg);
    return false;
  }
  // energy_level
  return true;
}

void
autoware_vehicle_msgs__msg__BatteryStatus__fini(autoware_vehicle_msgs__msg__BatteryStatus * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // energy_level
}

autoware_vehicle_msgs__msg__BatteryStatus *
autoware_vehicle_msgs__msg__BatteryStatus__create()
{
  autoware_vehicle_msgs__msg__BatteryStatus * msg = (autoware_vehicle_msgs__msg__BatteryStatus *)malloc(sizeof(autoware_vehicle_msgs__msg__BatteryStatus));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(autoware_vehicle_msgs__msg__BatteryStatus));
  bool success = autoware_vehicle_msgs__msg__BatteryStatus__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
autoware_vehicle_msgs__msg__BatteryStatus__destroy(autoware_vehicle_msgs__msg__BatteryStatus * msg)
{
  if (msg) {
    autoware_vehicle_msgs__msg__BatteryStatus__fini(msg);
  }
  free(msg);
}


bool
autoware_vehicle_msgs__msg__BatteryStatus__Sequence__init(autoware_vehicle_msgs__msg__BatteryStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  autoware_vehicle_msgs__msg__BatteryStatus * data = NULL;
  if (size) {
    data = (autoware_vehicle_msgs__msg__BatteryStatus *)calloc(size, sizeof(autoware_vehicle_msgs__msg__BatteryStatus));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = autoware_vehicle_msgs__msg__BatteryStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        autoware_vehicle_msgs__msg__BatteryStatus__fini(&data[i - 1]);
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
autoware_vehicle_msgs__msg__BatteryStatus__Sequence__fini(autoware_vehicle_msgs__msg__BatteryStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      autoware_vehicle_msgs__msg__BatteryStatus__fini(&array->data[i]);
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

autoware_vehicle_msgs__msg__BatteryStatus__Sequence *
autoware_vehicle_msgs__msg__BatteryStatus__Sequence__create(size_t size)
{
  autoware_vehicle_msgs__msg__BatteryStatus__Sequence * array = (autoware_vehicle_msgs__msg__BatteryStatus__Sequence *)malloc(sizeof(autoware_vehicle_msgs__msg__BatteryStatus__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = autoware_vehicle_msgs__msg__BatteryStatus__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
autoware_vehicle_msgs__msg__BatteryStatus__Sequence__destroy(autoware_vehicle_msgs__msg__BatteryStatus__Sequence * array)
{
  if (array) {
    autoware_vehicle_msgs__msg__BatteryStatus__Sequence__fini(array);
  }
  free(array);
}
