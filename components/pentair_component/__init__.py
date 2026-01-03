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

# Define codes for switch commands
# This is not byte [2] of status message! Rather, it is one of
# these codes: 0x01 represents the SPA, 0x02 is AUX1, 0x03 is AUX2, 0x04 is AUX3, and 0x05 is FEATURE1, 0x06 is POOL,
# 0x07 is FEATURE2, 0x08 is FEATURE3, 0x09 is FEATURE4, 0x85 is HEAT_BOOST.

CIRCUIT_SPA_ON     = 0x01
CIRCUIT_AUX1       = 0x02
CIRCUIT_AUX2       = 0x03
CIRCUIT_AUX3       = 0x04
CIRCUIT_POOL_ON    = 0x06
CIRCUIT_FEATURE1   = 0x05
CIRCUIT_FEATURE2   = 0x07
CIRCUIT_FEATURE3   = 0x08
CIRCUIT_FEATURE4   = 0x09
CIRCUIT_BOOST      = 0x85

pentair422_ns = cg.esphome_ns.namespace("pentair_component")
Pentair422_class = pentair422_ns.class_(
    "PentairRS422", cg.Component, uart.UARTDevice
)
pentair_switch_class = pentair422_ns.class_("PentairSwitch", switch.Switch, cg.Component)

CONFIG_SCHEMA = (
    cv.Schema({
            cv.GenerateID(): cv.declare_id(Pentair422_class),

            cv.Optional(CONF_SPA_ON,default={ CONF_NAME: "Spa Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX1,default={ CONF_NAME: "Aux1 Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX2,default={ CONF_NAME: "Aux2 Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX3,default={ CONF_NAME: "Aux3 Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_POOL_ON,default={ CONF_NAME: "Pool Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_FEATURE1,default={ CONF_NAME: "Feature1 Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_FEATURE2,default={ CONF_NAME: "Feature2 Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_FEATURE3,default={ CONF_NAME: "Feature3 Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_FEATURE4,default={ CONF_NAME: "Feature4 Switch" }): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_BOOST,default={ CONF_NAME: "Boost Switch" }): switch.switch_schema(
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
        cg.add(switch_.set_parent(var, CIRCUIT_SPA_ON))
    if CONF_AUX1 in config:
        switch_ = await switch.new_switch(config[CONF_AUX1])
        cg.add(var.set_aux1_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_AUX1))
    if CONF_AUX2 in config:
        switch_ = await switch.new_switch(config[CONF_AUX2])
        cg.add(var.set_aux2_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_AUX2))
    if CONF_AUX3 in config:
        switch_ = await switch.new_switch(config[CONF_AUX3])
        cg.add(var.set_aux3_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_AUX3))
    if CONF_POOL_ON in config:
        switch_ = await switch.new_switch(config[CONF_POOL_ON])
        cg.add(var.set_pool_on_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_POOL_ON))
    if CONF_FEATURE1 in config:
        switch_ = await switch.new_switch(config[CONF_FEATURE1])
        cg.add(var.set_feature1_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_FEATURE1))
    if CONF_FEATURE2 in config:
        switch_ = await switch.new_switch(config[CONF_FEATURE2])
        cg.add(var.set_feature2_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_FEATURE2))
    if CONF_FEATURE3 in config:
        switch_ = await switch.new_switch(config[CONF_FEATURE3])
        cg.add(var.set_feature3_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_FEATURE3))
    if CONF_FEATURE4 in config:
        switch_ = await switch.new_switch(config[CONF_FEATURE4])
        cg.add(var.set_feature4_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_FEATURE4))
    if CONF_BOOST in config:
        switch_ = await switch.new_switch(config[CONF_BOOST])
        cg.add(var.set_boost_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_BOOST))

    if CONF_AIR_TEMP in config:
        sensor_ = await sensor.new_sensor(config[CONF_AIR_TEMP])
        cg.add(var.set_air_temp_sensor(sensor_))
    if CONF_WATER_TEMP in config:
        sensor_ = await sensor.new_sensor(config[CONF_WATER_TEMP])
        cg.add(var.set_water_temp_sensor(sensor_))
    if CONF_SPA_TEMP in config:
        sensor_ = await sensor.new_sensor(config[CONF_SPA_TEMP])
        cg.add(var.set_spa_temp_sensor(sensor_))