# The __init.py__ file contains 2 main things:
# 
#     configuration validation or cv
#     code generation or cg
#
# cv handles validation of user input in the .yaml configuration file for this particular component: defining the available configuration options, whether they are required or optional, any constraints on the types and values of an option, etc.
# 
# cg takes these validated configuration options and generates the code necessary to streamline them into your c++ code, as well as registering your component properly within the ESPHome runtime.
#