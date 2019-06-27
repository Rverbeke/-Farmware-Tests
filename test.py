#!/usr/bin/env python

'''Circle.

Tells the farmbot to make a circle
'''

from farmware_tools import device, get_config_value
import numpy as np

farmware_name = 'test'

#Fetch the parameters from the webapp
radius = get_config_value(farmware_name, config_name='Radius')
points = get_config_value(farmware_name, config_name='Points')

#Check if the number of points is valid
assert(360%points == 0), "Number of points must be a divisor of 360"

#Get the current position, used as the center of the circle
farmbot_X_coord = device.get_current_position('x')
farmbot_Y_coord = device.get_current_position('y')

#Move the Farmbot with the calculated coordinates
for angle in range(0, 361, int(360/points)):
	next_X = farmbot_X_coord + radius*np.cos(np.array(angle*np.pi/180))
	next_Y = farmbot_Y_coord + radius*np.sin(np.array(angle*np.pi/180))
	device.move_relative(next_X, next_Y, 0, 100)






"""
#Linear movement (change X and Y in manifest.json)
X_pos = get_config_value(farmware_name, config_name='X')
Y_pos = get_config_value(farmware_name, config_name='Y')
device.log(message='farmbot is at {{ x }}, {{ y }}, {{ z }}')

device.move_relative(X_pos, Y_pos, 0, 100)
device.log(message='farmbot is at {{ x }}, {{ y }}, {{ z }}')
"""

