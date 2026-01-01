# example configuration:

external_components:
 # use github code
 - source:
     type: git
     url: https://github.com/robertcurtiscole/ESPHome-Pentair
     ref: main

pentair_component:
  id: pentair_controller
  # optional - you really should have one, otherwise, why bother?
  spa_on:
    name: “Spa”
  aux1_on:
    name: “Aux 1”
  aux2_on:
    name: “Aux 2”
  aux3_on:
    name: “Aux 3”
  feature1_on:
    name: “Feature 1”
  feature2_on:
    name: “Feature 2”
  feature3_on:
    name: “Feature 3”
  feature4_on:
    name: “Feature 4”
  pool_on:
    name: “Pool”
  boost_on:
    name: “Boost”
  spa_temp:
    name: “Spa Temp”
  air_temp:
    name: “Air Temp”
  water_temp:
    name: “Pool Temp”
  solar_temp:
    name: “Solar Temp”


uart:
  tx_pin: D0
  rx_pin: D1
  baud_rate: 9600