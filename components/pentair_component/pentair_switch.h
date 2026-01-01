#pragma once

#include "esphome/core/component.h"
#include "esphome/components/switch/switch.h"
#include "pentair_component.h"

namespace esphome {
namespace pentair_switch {

class PentairSwitch : public switch_::Switch, public Component {
 public:
  void setup() override;
  void write_state(bool state) override;
  void dump_config() override;
  void set_parent(PentairComponent *parent) { parent_ = parent; }

 protected:
  PentairComponent *parent_{nullptr};

};

} //namespace pentair_switch
} //namespace esphome