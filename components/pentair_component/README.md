# Pentair RS422 communications and control

## Connecting an ESP32 to a Pentair 422 line
The ESP32 needs to provide Rx/Tx with 3.3v and ground
In a nearby image:
- Rx     = red
- tx     = orange
- Gnd    = grey
- 3.3v   = purple

`Those four lines go to an rs485 to TTL converter`
The output/input since 422 is bi directional is the A+ (yellow) and B- (green) wires.
Those can go directly to the Pentair box where any remote displays are also wired.
In the nearby image, I show another RS485 unit which I used to tap into the line with a scope - even when the ESP32 was powered down.

## YAML file for your ESP32
 example configuration:

external_components:
 use github code for an external component
 ```yaml
 # external compoent
 - source:
     type: git
     url: https://github.com/robertcurtiscole/ESPHome-Pentair
     ref: main

pentair_component:
  id: pentair_controller
  # optional - you really should have one below, otherwise, why bother?
  # switches
  spa_on:
    name: “Spa”
  pool_on:
    name: “Pool”
  aux1_on:
    name: “Pool Cleaner”
  aux2_on:
    name: “Aux 2”
  aux3_on:
    name: “Aux 3”
  aux4:
    name: "Fiber Light"
  aux5:
    name: "Aux 5"
  aux6:
    name: "Aux 6"
  aux7:
    name: "Spa Jets"
  # boost not implemented or tested.
  boost_on: (not connected)
    name: “Boost”

  # Sensors Temperature
  spa_temp:
    name: “Spa Temp”
  air_temp:
    name: “Air Temp”
  water_temp:
    name: “Pool Temp”
  # solar temp not tested
  solar_temp:
    name: “Solar Temp”
  # Sensor, binary
  heater_on:
    name: "Heater On"
  # Text?
  Spa_Heat_Setting (string?)
  Pool_Heat_Setting (string?)

# connection to UART and RS422
uart:
  tx_pin: D0
  rx_pin: D1
  baud_rate: 9600
```
