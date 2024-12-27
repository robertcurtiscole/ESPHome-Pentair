#include "esphome/core/log.h"
#include "empty_pentair_component.h"

namespace esphome {
namespace empty_pentair_component {

static const char *TAG = "empty_pentair_component.binary_sensor";

void empty_pentair_component::setup() {
    
}
  
void empty_pentair_component::update() {

}

void empty_pentair_component::dump_config() {
    ESP_LOGCONFIG(TAG, "Custom Pentair binary sensor");
}

} //namespace empty_pentair_component
} //namespace esphome