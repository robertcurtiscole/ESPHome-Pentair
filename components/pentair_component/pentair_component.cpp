#include "esphome/core/log.h"
#include "pentair_component.h"

namespace esphome {
namespace pentair_component {

static const char *TAG = "PentairRS422.component";

void PentairRS422::setup() {
    ESP_LOGI(TAG, "PentairRS422 setup().");
   
    loop_count_ = 0;
    // else if any failure
    // this->mark_failed();
    // return;
    ESP_LOGE(TAG, "Setup completed.");
}
  
void PentairRS422::loop() {
    this->water_temperature_sensor_->publish_state(random_float() * 50);
    // junk debug
    if (++loop_count_ == 50) {
        if (this->spa_on_sensor_) {
            this->spa_on_sensor_->publish_state(true);
        }
    }

    // This will be called by App.loop()
    boolean got_char = false;
    char msgbuffer[40];
    while (available()) {
        loop_chars++;     // count loops with char
        got_char = true;
        int c = read();
    }
    
}

void PentairRS422::dump_config() {
    ESP_LOGCONFIG(TAG, "Custom Pentair component:");
    //LOG_SENSOR("  ", "Spa On", this->spa_on_sensor_);
    //LOG_BUTTON("  ", "Spa Button", this->spa_button_);
    //LOG_SENSOR("  ", "Water Temperature", this->water_temperature_sensor_);
}


} //namespace pentair_component
} //namespace esphome

