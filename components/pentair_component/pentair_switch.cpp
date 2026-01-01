#include "esphome/core/log.h"
#include "pentair_switch.h"
#include "pentair_component.h"

namespace esphome {
namespace pentair_switch {

static const char *TAG = "pentair_switch.switch";

void PentairSwitch::setup() {

}

void PentairSwitch::write_state(bool state) {
  ESP_LOGI(TAG, "PentairSwitch::write_state(%s) called.", state ? "ON" : "OFF");
  // talk to the PentairComponent to set the switch
  if (parent_ != nullptr) {
    // parent_->set_switch_state(this, state);
  }
}

void PentairSwitch::dump_config(){
    ESP_LOGCONFIG(TAG, "Pentair switch");
}

} //namespace pentair_switch
} //namespace esphome