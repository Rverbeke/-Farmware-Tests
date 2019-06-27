#!/usr/bin/env python

'''Circle.

Tells the farmbot to make a circle
'''

from farmware_tools import device, get_config_value
import numpy as np

farmware_name = 'Circle'

#Fetch the parameters from the webapp
diameter = get_config_value(farmware_name, config_name='Radius')
points = get_config_value(farmware_name, config_name='Points')

#Get the current position, used as the center of the circle
farmbot_X_coord = device.get_current_position('x')
farmbot_Y_coord = device.get_current_position('y')

#Length of the polygon's sides
length = diameter * np.sin(np.array(np.pi/points))

#Angle for each side relative to X axis
angles = [0]
i = 1
while(i<=points):
	angles.append(angles[i-1] + 2*np.pi/points)
	i+=1

#Move the farmbot to new coordinates
for angle in angles:
	next_X = farmbot_X_coord + length * np.cos(np.array(angle))
	next_Y = farmbot_Y_coord + length * np.sin(np.array(angle))
	device.move_absolute(device.assemble_coordinate(next_X, next_Y, 0), 100, device.assemble_coordinate(0, 0, 0))
device.move_absolute(device.assemble_coordinate(farmbot_X_coord, farmbot_Y_coord, 0), 100, device.assemble_coordinate(0, 0, 0))

"""
#Linear movement (change X and Y in manifest.json)
X_pos = get_config_value(farmware_name, config_name='X')
Y_pos = get_config_value(farmware_name, config_name='Y')
device.log(message='farmbot is at {{ x }}, {{ y }}, {{ z }}')

device.move_relative(X_pos, Y_pos, 0, 100)
device.log(message='farmbot is at {{ x }}, {{ y }}, {{ z }}')
"""

