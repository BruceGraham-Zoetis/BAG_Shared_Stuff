"""
File: control_channel_controller.py

Purpose: These are the openAPI functions.
These functions call the analyzer "Dracula" DBus service.
The "Dracula" DBus service will perform the low-level part of the openAPIs.
"""

import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)

import CDBusDraculaService


def control_light_blink_put():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.control_light_blink_put()
    return str_rtn

def control_power_off_put():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.control_power_off_put()
    return str_rtn

def control_power_reboot_put():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.control_power_reboot_put()
    return str_rtn

