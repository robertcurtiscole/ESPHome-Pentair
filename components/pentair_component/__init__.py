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
from esphome.components import uart, sensor, switch
from esphome.const import (     CONF_ID, UNIT_EMPTY, ICON_EMPTY)

DEPENDENCIES = ["uart"]

# Define constants for configuration keys
CONF_SPA_ON     = "spa_on"
CONF_AUX1       = "aux1"
CONF_AUX2       = "aux2"
CONF_AUX3       = "aux3"
CONF_AIR_TEMP   = "air_temp"
CONF_WATER_TEMP = "water_temp"
CONF_SPA_TEMP   = "spa_temp"

pentair422_ns = cg.esphome_ns.namespace("pentair_component")
Pentair422_class = pentair422_ns.class_(
    "PentairRS422", cg.Component, uart.UARTDevice
)

CONFIG_SCHEMA = (
    cv.Schema({
            cv.GenerateID(): cv.declare_id(Pentair422_class),
            cv.Optional(CONF_SPA_ON): cv.entity_id,
            #cv.Optional(CONF_WATER_TEMP): cv.entity_id,
            #cv.Optional(CONF_AIR_TEMP): sensor.sensor_schema(
            #    Pentair422_class,
            #    unit_of_measurement=UNIT_EMPTY,
            #    icon=ICON_EMPTY,
            #    accuracy_decimals=1,
            #).extend(),
        })
        .extend(cv.COMPONENT_SCHEMA)
        .extend(uart.UART_DEVICE_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_AIR_TEMP in config:
        sensor = await sensor.new_sensor(config[CONF_AIR_TEMP])
        #cg.add(var.set_air_temp(sensor))