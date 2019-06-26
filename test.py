device.log("Begin Farmware tests", message_type="success")

from farmware_tools import device, get_config_value
farmware_name = 'Tests'

device.log("Fetching coordinates", message_type="info")
X = get_config_value(farmware_name, config_name='X')
device.log("X coordinate recieved", message_type="success")
Y = get_config_value(farmware_name, config_name='Y')
device.log("Y coordinate recieved", message_type="success")

device.log("attempting to move to inputed coordinates", message_type="info")
device.move_relative(X, Y, 0, 100)
device.log("Movement successful", message_type="success")
