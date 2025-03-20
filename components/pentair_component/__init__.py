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
from esphome.const import (
    CONF_ID,
)

DEPENDENCIES = ["uart"]

# Define constants for configuration keys
CONF_SPA_ON     = "spa_on"
CONF_SPA_BUTTON = "spa_button"
CONF_AIR_TEMP   = "air_temp"
CONF_WATER_TEMP = "water_temp"

pentair422_ns = cg.esphome_ns.namespace("pentair_component")
Pentair422_class = pentair422_ns.class_(
    "PentairRS422", cg.Component, uart.UARTDevice
)

CONFIG_SCHEMA = (
    cv.Schema({
            cv.GenerateID(): cv.declare_id(Pentair422_class),
            cv.Optional(CONF_SPA_ON): cv.entity_id,
            cv.Optional(CONF_WATER_TEMP): cv.entity_id,
        })
        .extend(cv.COMPONENT_SCHEMA)
        .extend(uart.UART_DEVICE_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)