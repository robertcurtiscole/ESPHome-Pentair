#pragma once

#include "esphome/core/component.h"
#include "esphome/components/switch/switch.h"
#include "pentair_component.h"

namespace esphome {
namespace pentair_component {

class PentairSwitch : public switch_::Switch, public Component {
 public:
  void setup() override;
  void write_state(bool state) override;
  void dump_config() override;
  void set_parent(pentair_component::PentairRS422 *parent, uint32_t circuit) { parent_ = parent; circuit_ = circuit; }

 protected:
  pentair_component::PentairRS422 *parent_{nullptr};
  uint32_t circuit_{0};

};

} //namespace pentair_component
} //namespace esphome