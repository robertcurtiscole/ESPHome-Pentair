#pragma once

#include "esphome/core/component.h"

namespace esphome {
namespace empty_pentair_component {

class empty_pentair_component : public Component {
 public:
  void setup() override;
  void update() override;
  void dump_config() override;
};

} //namespace empty_pentair_component
} //namespace esphome