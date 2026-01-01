#include "esphome/core/log.h"
#include "pentair_switch.h"

namespace esphome {
namespace pentair_switch {

static const char *TAG = "pentair_switch.switch";

void PentairSwitch::setup() {

}

void PentairSwitch::write_state(bool state) {
}

void PentairSwitch::dump_config(){
    ESP_LOGCONFIG(TAG, "Pentair switch");
}

} //namespace pentair_switch
} //namespace esphome