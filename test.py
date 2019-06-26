#!/usr/bin/env python

from farmware_tools import device

try:
    device.log(message='Hello Farmware!', message_type='success')
except Exception as error:
    farmware_tools.device.log(repr(error))
