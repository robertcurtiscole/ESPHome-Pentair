#include "esphome/core/log.h"
#include "empty_pentair_component.h"

namespace esphome {
namespace EmptyPentairComponent {

static const char *TAG = "empty_pentair_component.component";

void EmptyPentairComponent::setup() {
    
}
  
void EmptyPentairComponent::update() {

}

void EmptyPentairComponent::dump_config() {
    ESP_LOGCONFIG(TAG, "Custom Pentair component");
}

} //namespace empty_pentair_component
} //namespace esphome

