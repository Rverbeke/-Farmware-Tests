from farmware_tools import device, get_config_value

farmware_name = 'Tests'

X = get_config_value(farmware_name, config_name='X_direction')
Y = get_config_value(farmware_name, config_name='Y_direction')

device.move_relative(X, Y, 0, 100)
