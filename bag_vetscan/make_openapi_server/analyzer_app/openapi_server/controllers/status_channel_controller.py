"""
File: status_channel_controller.py

Purpose: These are the openAPI functions.
These functions call the analyzer "Dracula" DBus service.
The "Dracula" DBus service will perform the low-level part of the openAPIs.
"""


import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)

import CDBusDraculaService


def status_currently_activated_events_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.status_currently_activated_events_get()
    return str_rtn

def status_operational_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.status_operational_get()
    return str_rtn