#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/switch/switch.h"
//#include "pentair_switch.h"
namespace esphome {
namespace pentair_component {

class PentairRS422 : public uart::UARTDevice, public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;

  // Set switches and sensors
  void set_spa_on_switch(switch_::Switch *spa_on_switch) { spa_on_switch_ = spa_on_switch; }
  void set_air_temp_sensor(sensor::Sensor *air_temp_sensor) { air_temp_sensor_ = air_temp_sensor; }
  void set_water_temp_sensor(sensor::Sensor *water_temp_sensor) { water_temp_sensor_ = water_temp_sensor; }
  void set_spa_temp_sensor(sensor::Sensor *spa_temp_sensor) { spa_temp_sensor_ = spa_temp_sensor; }
  void set_solar_temp_sensor(sensor::Sensor *solar_temp_sensor) { solar_temp_sensor_ = solar_temp_sensor; }

  // protected variables
 protected:
  switch_::Switch *spa_on_switch_{nullptr};

  sensor::Sensor *air_temp_sensor_{nullptr};
  sensor::Sensor *water_temp_sensor_{nullptr};
  sensor::Sensor *spa_temp_sensor_{nullptr};
  sensor::Sensor *solar_temp_sensor_{nullptr};

  // private for communications
 private:
  uint16 computeChecksum(u_char *buff);
  boolean checksumPass(u_char *buff, int numchars);
  void addchar(char c);
  void resetBuffer();
  void sendCircuitChange(char circuit, bool state);

  int   loop_count_{0};   // for testing and debug

  uint nchars = 0;
  uint msglen = 0;
  // read data into buffer, process
  uint loop_chars = 0;
  uint loop_nochars = 0;
  u_char buffer[255];
  // const char *starthead = "1234";    // "00 FF A5 01"
  uint8 starthead[4] = { 0x00, 0xFF, 0xA5, 0x01};

};

} //namespace pentair_component
} //namespace esphome