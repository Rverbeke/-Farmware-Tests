from farmware_tools import device, get_config_value

device.log(message="Begin Farmware tests", message_type="success")

farmware_name = 'Tests'

device.log(message="Fetching coordinates", message_type="info")
X = get_config_value(farmware_name, config_name='X')
device.log(message="X coordinate recieved", message_type="success")
Y = get_config_value(farmware_name, config_name='Y')
device.log(message="Y coordinate recieved", message_type="success")
"""
device.log(message="attempting to move to inputed coordinates", message_type="info")
device.move_relative(X, Y, 0, 100)
device.log(message="Movement successful", message_type="success")
"""
