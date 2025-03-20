#include "esphome/core/log.h"
#include "empty_pentair_component.h"

namespace esphome {
namespace empty_pentair_component {

static const char *TAG = "empty_pentair_component.component";

void EmptyPentairComponent::setup() {
    
}
  
void EmptyPentairComponent::loop() {

}

void EmptyPentairComponent::dump_config() {
    ESP_LOGCONFIG(TAG, "Custom Pentair component");
}

} //namespace empty_pentair_component
} //namespace esphome

