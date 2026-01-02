#include "esphome/core/log.h"
#include "pentair_switch.h"
#include "pentair_component.h"

namespace esphome {
namespace pentair_component {

static const char *TAG = "pentair_switch.switch";

void PentairSwitch::setup() {

}

void PentairSwitch::write_state(bool nstate) {
  ESP_LOGI(TAG, "PentairSwitch::write_state(%s) called.", nstate ? "ON" : "OFF");
  if (this->state != nstate) {
    if (nstate)
      this->turn_on();
    else
      this->turn_off();
  }
  // talk to the PentairComponent to set the switch
  if (parent_ != nullptr) {
    // parent_->set_switch_state(this, state);
  }
}

void PentairSwitch::dump_config(){
    ESP_LOGCONFIG(TAG, "Pentair switch");
}

} //namespace pentair_component
} //namespace esphome