#include "esphome/core/log.h"
#include "pentair_component.h"

namespace esphome {
namespace pentair_component {

static const char *TAG = "pentair_component";

void PentairRS422::setup() {
      // nothing to do here
    ESP_LOGI(TAG, "PentairRS422 setup().");
   
    loop_count_ = 0;
    // else if any failure
    // this->mark_failed();
    // return;
    ESP_LOGE(TAG, "Setup completed.");    
}
  
void PentairRS422::loop() {
     // junk debug
    if ((++loop_count_ %100) == 0) {
        if (this->water_temp_sensor_) {
            this->water_temp_sensor_->publish_state(random_float() * 50);
        }
       if (this->spa_on_switch_) {
            this->spa_on_switch_->publish_state(random_uint32()%2);
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
    ESP_LOGCONFIG(TAG, "PentairRS422 component");
}

} //namespace pentair_component
} //namespace esphome

