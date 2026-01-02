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
from esphome.const import (     CONF_ID, CONF_NAME,UNIT_EMPTY, ICON_EMPTY,
                           DEVICE_CLASS_TEMPERATURE, STATE_CLASS_MEASUREMENT, UNIT_CELSIUS, ICON_THERMOMETER,
                           DEVICE_CLASS_SWITCH,
                           )

DEPENDENCIES = ["uart"]
AUTO_LOAD = ['uart', 'sensor', 'switch']

# Define constants for configuration keys
CONF_SPA_ON     = "spa_on"
CONF_AUX1       = "aux1"
CONF_AUX2       = "aux2"
CONF_AUX3       = "aux3"
CONF_POOL_ON    = "pool_on"
CONF_FEATURE1   = "feature1"
CONF_FEATURE2   = "feature2"
CONF_FEATURE3   = "feature3"
CONF_FEATURE4   = "feature4"
CONF_BOOST      = "boost"
CONF_AIR_TEMP   = "air_temp"
CONF_WATER_TEMP = "water_temp"
CONF_SPA_TEMP   = "spa_temp"

pentair422_ns = cg.esphome_ns.namespace("pentair_component")
Pentair422_class = pentair422_ns.class_(
    "PentairRS422", cg.Component, uart.UARTDevice
)
pentair_switch_ns = cg.esphome_ns.namespace("pentair_switch")
pentair_switch_class = pentair_switch_ns.class_("PentairSwitch", switch.Switch, cg.Component)

CONFIG_SCHEMA = (
    cv.Schema({
            cv.GenerateID(): cv.declare_id(Pentair422_class),
            cv.Optional(CONF_SPA_ON,default={ CONF_NAME: "Spa Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AIR_TEMP,default={ CONF_NAME: "Air Temp" }): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                state_class=STATE_CLASS_MEASUREMENT,
                device_class=DEVICE_CLASS_TEMPERATURE,
            ).extend(),
            cv.Optional(CONF_WATER_TEMP,default={ CONF_NAME: "Pool Temp" }): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                state_class=STATE_CLASS_MEASUREMENT,
                device_class=DEVICE_CLASS_TEMPERATURE,
            ).extend(),
            cv.Optional(CONF_SPA_TEMP,default={ CONF_NAME: "Spa Temp" }): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                state_class=STATE_CLASS_MEASUREMENT,
                device_class=DEVICE_CLASS_TEMPERATURE,
            ).extend(),
        })
        .extend(cv.COMPONENT_SCHEMA)
        .extend(uart.UART_DEVICE_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_SPA_ON in config:
        switch_ = await switch.new_switch(config[CONF_SPA_ON])
        cg.add(var.set_spa_on_switch(switch_))
        cg.add(switch_.set_parent(var))

    if CONF_AIR_TEMP in config:
        sensor_ = await sensor.new_sensor(config[CONF_AIR_TEMP])
        cg.add(var.set_air_temp_sensor(sensor_))
    if CONF_WATER_TEMP in config:
        sensor_ = await sensor.new_sensor(config[CONF_WATER_TEMP])
        cg.add(var.set_water_temp_sensor(sensor_))
    if CONF_SPA_TEMP in config:
        sensor_ = await sensor.new_sensor(config[CONF_SPA_TEMP])
        cg.add(var.set_spa_temp_sensor(sensor_))