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
from esphome.components import uart, sensor, switch, binary_sensor
from esphome.const import (     CONF_ID, CONF_NAME,UNIT_EMPTY, ICON_EMPTY,
                           DEVICE_CLASS_TEMPERATURE, STATE_CLASS_MEASUREMENT, UNIT_CELSIUS, ICON_THERMOMETER,
                           DEVICE_CLASS_SWITCH, DEVICE_CLASS_HEAT
                           )

DEPENDENCIES = ["uart"]
AUTO_LOAD = ['uart', 'sensor', 'switch', 'binary_sensor']

# Define constants for configuration keys
CONF_SPA_ON     = "spa_on"
CONF_AUX1       = "aux1"
CONF_AUX2       = "aux2"
CONF_AUX3       = "aux3"
CONF_POOL_ON    = "pool_on"
CONF_AUX4       = "aux4"
CONF_AUX5       = "aux5"
CONF_AUX6       = "aux6"
CONF_AUX7       = "aux7"
CONF_BOOST      = "boost"
CONF_AIR_TEMP   = "air_temp"
CONF_WATER_TEMP = "water_temp"
CONF_SPA_TEMP   = "spa_temp"
CONF_SOLAR_TEMP = "solar_temp"

CONF_HEATER_ON  = "heater_on" 

# Define codes for switch commands
# This is not byte [2] of status message! Rather, it is one of
# these codes: 0x01 represents the SPA, 0x02 is AUX1, 0x03 is AUX2, 0x04 is AUX3,
# and 0x05 is FEATURE1, 0x06 is POOL,  (out of order)
# 0x07 is FEATURE2, 0x08 is FEATURE3, 0x09 is FEATURE4, 0x85 is HEAT_BOOST.

CIRCUIT_SPA_ON     = 0x01
CIRCUIT_AUX1       = 0x02
CIRCUIT_AUX2       = 0x03
CIRCUIT_AUX3       = 0x04
CIRCUIT_POOL_ON    = 0x06
CIRCUIT_AUX4       = 0x05
CIRCUIT_AUX5       = 0x07
CIRCUIT_AUX6       = 0x08
CIRCUIT_AUX7       = 0x09
CIRCUIT_BOOST      = 0x85

pentair422_ns = cg.esphome_ns.namespace("pentair_component")
Pentair422_class = pentair422_ns.class_(
    "PentairRS422", cg.Component, uart.UARTDevice
)
pentair_switch_class = pentair422_ns.class_("PentairSwitch", switch.Switch, cg.Component)

CONFIG_SCHEMA = (
    cv.Schema({
            cv.GenerateID(): cv.declare_id(Pentair422_class),

            cv.Optional(CONF_SPA_ON): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX1): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX2): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX3): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_POOL_ON): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX4): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX5): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX6): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_AUX7): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),
            cv.Optional(CONF_BOOST): switch.switch_schema(
               pentair_switch_class, device_class=DEVICE_CLASS_SWITCH,
            ).extend(),

            cv.Optional(CONF_HEATER_ON): binary_sensor.binary_sensor_schema(
               device_class=DEVICE_CLASS_HEAT,# options here?
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
            cv.Optional(CONF_SOLAR_TEMP,default={ CONF_NAME: "Solar Temp" }): sensor.sensor_schema(
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
    if CONF_AUX4 in config:
        switch_ = await switch.new_switch(config[CONF_AUX4])
        cg.add(var.set_aux4_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_AUX4))
    if CONF_AUX5 in config:
        switch_ = await switch.new_switch(config[CONF_AUX5])
        cg.add(var.set_aux5_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_AUX5))
    if CONF_AUX6 in config:
        switch_ = await switch.new_switch(config[CONF_AUX6])
        cg.add(var.set_aux6_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_AUX6))
    if CONF_AUX7 in config:
        switch_ = await switch.new_switch(config[CONF_AUX7])
        cg.add(var.set_aux7_switch(switch_))
        cg.add(switch_.set_parent(var, CIRCUIT_AUX7))
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
    if CONF_SOLAR_TEMP in config:
        sensor_ = await sensor.new_sensor(config[CONF_SOLAR_TEMP])
        cg.add(var.set_solar_temp_sensor(sensor_))

    if CONF_HEATER_ON in config:
        binary_sensor_ = await binary_sensor.new_binary_sensor(config[CONF_HEATER_ON])
        cg.add(var.set_heater_on_binary_sensor(binary_sensor_))