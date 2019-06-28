#!/usr/bin/env python

'''Circle.

Tells the farmbot to make a circle
'''

from farmware_tools import device, get_config_value
import numpy as np


farmware_name = 'Circle'

#Get the current position, used as the center of the circle
farmbot_X_coord = device.get_current_position('x')
farmbot_Y_coord = device.get_current_position('y')

#Fetch the parameters from the webapp
diameter = get_config_value(farmware_name, config_name='Diameter')
points = get_config_value(farmware_name, config_name='Points')

#Properties of the polygon
length = diameter * np.sin(np.array(np.pi/points))
apothem = diameter/2 * np.cos(np.array(np.pi/points))
angle = (points-2)*np.pi/points

#Create angle value for each point
angles = [0]
i = 1
while(i<points):
	angles.append(angles[i-1] + np.pi - angle)
	i+=1

#Move to 1st point
device.move_relative(-length/2, -apothem, 0, 100)

#Move to each point
for current_angle in angles:
	next_X = length * np.cos(np.array(current_angle))
	next_Y = length * np.sin(np.array(current_angle))
	device.move_relative(next_X, next_Y, 0, 100)

#Get back to original position

device.move_absolute(device.assemble_coordinate(farmbot_X_coord, farmbot_Y_coord, 0), 100, device.assemble_coordinate(0, 0, 0))

"""
#Legacy code

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
	print((next_X, next_Y))
device.move_absolute(device.assemble_coordinate(farmbot_X_coord, farmbot_Y_coord, 0), 100, device.assemble_coordinate(0, 0, 0))
"""
