#!/usr/bin/env python

'''Hello Farmware

A simple Farmware example that tells FarmBot to log a new message.
'''

from farmware_tools import device, get_config_value

farmware_name = 'test'

X = get_config_value(farmware_name, config_name=X)
Y = get_config_value(farmware_name, config_name=Y)

device.move_relative(X, Y, 0, 100)
