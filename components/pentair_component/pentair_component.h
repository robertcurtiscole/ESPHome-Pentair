#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/button/button.h"

namespace esphome {
namespace pentair_component {

class PentairRS422 : public uart::UARTDevice, public Component {
  protected:
  sensor::BinarySensor *spa_on_sensor_{nullptr};
  sensor::BinarySensor *aux1_sensor_{nullptr};
  sensor::BinarySensor *aux2_sensor_{nullptr};
  sensor::BinarySensor *aux3_sensor_{nullptr};
  sensor::BinarySensor *pool_on_sensor_{nullptr};
  sensor::BinarySensor *feature1_sensor_{nullptr};
  sensor::BinarySensor *feature2_sensor_{nullptr};
  sensor::BinarySensor *feature3_sensor_{nullptr};
  sensor::BinarySensor *feature4_sensor_{nullptr};
  sensor::BinarySensor *heater_on_sensor_{nullptr};
  button::Button  *spa_button_{nullptr};
  sensor::Sensor *water_temperature_sensor_{nullptr};
  sensor::Sensor *air_temperature_sensor_{nullptr};

  int   loop_count_{0};

 public:
  void setup() override;

  void set_spa_on_sensor(sensor::Sensor *spa_on_sensor) { spa_on_sensor_ = spa_on_sensor; }
  void set_spa_button(button::Button *spa_button) { spa_button_ = spa_button; }
  void set_water_temperature_sensor(sensor::Sensor *temperature_sensor) { water_temperature_sensor_ = temperature_sensor; }

  void loop() override;
  void dump_config() override;
};

} //namespace pentair_component
} //namespace esphome