"""
File: configuration_controller.py

Purpose: These are the openAPI functions.
These functions call the analyzer "Dracula" DBus service.
The "Dracula" DBus service will perform the low-level part of the openAPIs.
"""


import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)

import CDBusDraculaService


def configuration_factory_reset_put():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.configuration_factory_reset_put()
    return str_rtn

def configuration_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.configuration_get()
    return str_rtn

def configuration_put(body):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.configuration_put(body)
    return str_rtn

def configuration_schema_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.configuration_schema_get()
    return str_rtn
