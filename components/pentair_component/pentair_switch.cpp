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
  // talk to the PentairComponent to set the switch
  if (parent_ != nullptr) {
    parent_->request_circuit_change(this->circuit_, nstate);
  }

  // confirm this was successful? Though we won't know until the next status update
  this->publish_state(nstate);
}

void PentairSwitch::dump_config(){
    ESP_LOGCONFIG(TAG, "Pentair switch");
}

} //namespace pentair_component
} //namespace esphome