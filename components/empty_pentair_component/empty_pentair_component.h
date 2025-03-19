#pragma once

#include "esphome/core/component.h"
#include "esphome/components/binary_sensor/binary_sensor.h"

namespace esphome {
namespace empty_pentair_component {

class EmptyPentairComponent : public binary_sensor::BinarySensor, public Component {
 public:
  void setup() override;
  void update() override;
  void dump_config() override;
};

} //namespace empty_pentair_component
} //namespace esphome