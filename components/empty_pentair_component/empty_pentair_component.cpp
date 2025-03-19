#include "esphome/core/log.h"
#include "empty_pentair_component.h"

namespace esphome {
namespace empty_pentair_component {

static const char *TAG = "empty_pentair_component.component";

void empty_pentair_component::setup() {
    
}
  
void empty_pentair_component::update() {

}

void empty_pentair_component::dump_config() {
    ESP_LOGCONFIG(TAG, "Custom Pentair component");
}

} //namespace empty_pentair_component
} //namespace esphome

/*****
 * success elsewhere:
 * 
INFO ESPHome 2024.12.2
INFO Reading configuration /config/esphome/spa-control.yaml...
INFO Updating https://github.com/robertcurtiscole/ESPHome-Pentair@dev
INFO Generating C++ source...
INFO Compiling app...
Processing spa-control (board: esp12e; framework: arduino; platform: platformio/espressif8266@4.2.1)
--------------------------------------------------------------------------------
HARDWARE: ESP8266 80MHz, 80KB RAM, 4MB Flash
Dependency Graph
|-- ESPAsyncTCP-esphome @ 2.0.0
|-- ESPAsyncWebServer-esphome @ 3.2.2
|-- DNSServer @ 1.1.1
|-- ESP8266WiFi @ 1.0
|-- ESP8266mDNS @ 1.2
|-- noise-c @ 0.1.6
 *
 *
 */