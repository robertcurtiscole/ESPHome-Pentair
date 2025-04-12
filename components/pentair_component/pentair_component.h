#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/button/button.h"

namespace esphome {
namespace pentair_component {

class PentairRS422 : public uart::UARTDevice, public Component {
  protected:
  binary_sensor::BinarySensor *spa_on_sensor_{nullptr};
  binary_sensor::BinarySensor *aux1_sensor_{nullptr};
  binary_sensor::BinarySensor *aux2_sensor_{nullptr};
  binary_sensor::BinarySensor *aux3_sensor_{nullptr};
  binary_sensor::BinarySensor *pool_on_sensor_{nullptr};
  binary_sensor::BinarySensor *feature1_sensor_{nullptr};
  binary_sensor::BinarySensor *feature2_sensor_{nullptr};
  binary_sensor::BinarySensor *feature3_sensor_{nullptr};
  binary_sensor::BinarySensor *feature4_sensor_{nullptr};
  binary_sensor::BinarySensor *heater_on_sensor_{nullptr};
  button::Button  *spa_button_{nullptr};
  sensor::Sensor *water_temperature_sensor_{nullptr};
  sensor::Sensor *air_temperature_sensor_{nullptr};

  int   loop_count_{0};

  // private:
  uint nchars = 0;
  uint msglen = 0;
  // read data into buffer, process
  uint loop_chars = 0;
  uint loop_nochars = 0;
  u_char buffer[255];
  // const char *starthead = "1234";    // "00 FF A5 01"
  uint8 starthead[4] = { 0x00, 0xFF, 0xA5, 0x01};
  bool curSpaHeater = false;
  bool curSpaLight = false;
  bool curPoolLight = false;
  bool curPoolFiber = false;
  bool curSpaJets = false;
  bool cmdSpaHeater = false;
  bool cmdSpaLight = false;
  bool cmdPoolLight = false;
  bool cmdPoolFiber = false;
  bool cmdSpaJets = false;

 public:
  void setup() override;

  void set_spa_on_sensor(binary_sensor::BinarySensor *spa_on_sensor) { spa_on_sensor_ = spa_on_sensor; }
  void set_spa_button(button::Button *spa_button) { spa_button_ = spa_button; }
  void set_water_temperature_sensor(sensor::Sensor *temperature_sensor) { water_temperature_sensor_ = temperature_sensor; }

  void loop() override;
  void dump_config() override;
};

} //namespace pentair_component
} //namespace esphome