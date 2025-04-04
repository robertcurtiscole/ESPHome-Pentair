# The __init.py__ file contains 2 main things:
# 
#     configuration validation or cv
#     code generation or cg
#
# cv handles validation of user input in the .yaml configuration file for this particular component: defining the available configuration options, whether they are required or optional, any constraints on the types and values of an option, etc.
# 
# cg takes these validated configuration options and generates the code necessary to streamline them into your c++ code, as well as registering your component properly within the ESPHome runtime.
#

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.components import sensor
from esphome.components import binary_sensor
from esphome.const import (
    CONF_ID, CONF_NAME, UNIT_CELSIUS, DEVICE_CLASS_TEMPERATURE, STATE_CLASS_MEASUREMENT, ICON_THERMOMETER
)

DEPENDENCIES = ["uart"]

# Define constants for configuration keys
CONF_SPA_ON     = "spa_on"
CONF_SPA_BUTTON = "spa_button"
CONF_WATER_TEMP = "water_temp"

pentair422_ns = cg.esphome_ns.namespace("pentair_component")
Pentair422_class = pentair422_ns.class_(
    "PentairRS422", cg.Component, uart.UARTDevice
)

CONFIG_SCHEMA = cv.Schema({
        cv.GenerateID(): cv.declare_id(Pentair422_class),
        cv.Optional(CONF_SPA_ON,
                    default={ CONF_NAME: "Spa On Sensor",}
            ): cv.entity_id,
        # cv.Optional(CONF_SPA_BUTTON): cv.entity_id,
        cv.Optional(CONF_WATER_TEMP,
                    default={ CONF_NAME: "Water Temperature Sensor",}
            ): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                state_class=STATE_CLASS_MEASUREMENT,
                device_class=DEVICE_CLASS_TEMPERATURE,
            ),
    })
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)


async def to_code(config):
    # await for required parameters

    # Declare the new component, register it as a component and a uart.
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    # configure composition sensors and buttons in the new component
    spa_on_sensor = await sensor.new_sensor(config.get(CONF_SPA_ON))
    cg.add(var.set_spa_onset_spa_on_sensor(spa_on_sensor))
    #cg.add(var.set_spa_button(config[CONF_SPA_BUTTON]))
    temperature_sensor = await sensor.new_sensor(config.get(CONF_WATER_TEMP))
    cg.add(var.set_water_temperature_sensor(temperature_sensor))