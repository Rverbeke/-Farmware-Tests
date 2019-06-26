from farmware_tools import device, get_config_value

farmware_name = 'Tests'

device.log("Fetching coordinates", messagetype="info")

X = get_config_value(farmware_name, config_name='X')
device.log("X coordinate recieved", messagetype="success")
Y = get_config_value(farmware_name, config_name='Y')
device.log("Y coordinate recieved", messagetype="success")

device.log("attempting to move to inputed coordinates", messagetype="info")
device.move_relative(X, Y, 0, 100)
device.log("Movement successful", messagetype="success")
