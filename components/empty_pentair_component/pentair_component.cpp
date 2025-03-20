#include "esphome/core/log.h"
#include "empty_pentair_component.h"

namespace esphome {
namespace pentair_component {

static const char *TAG = "PentairRS422.component";

void PentairRS422::setup() {
    
}
  
void PentairRS422::loop() {

}

void PentairRS422::dump_config() {
    ESP_LOGCONFIG(TAG, "Custom Pentair component");
}

} //namespace pentair_component
} //namespace esphome

