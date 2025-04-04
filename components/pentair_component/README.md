# example configuration:
# incorrect:  please fix:
# example configuration:

# need empty components for dependencies:
sensor:
binary_sensor:
button:

# our component
empty_pentair_component:
  id: empty_pentair_component_1
  spa_button:
    name: "Spa"
  spa_on:
    name: "Spa Running"
  water_temp:
    name: "Water Temp"
  
# needs a uart
uart:
  tx_pin: D0
  rx_pin: D1
  baud_rate: 9600

# examples very helpful:
https://medium.com/@vinsce/create-an-esphome-external-component-part-1-introduction-config-validation-and-code-generation-e0389e674bd6
https://medium.com/@vinsce/create-an-esphome-external-component-part-2-expose-functionality-to-homeassistant-with-sensors-675bd3a987b4
