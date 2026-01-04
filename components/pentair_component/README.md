# example configuration:

external_components:
 # use github code
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