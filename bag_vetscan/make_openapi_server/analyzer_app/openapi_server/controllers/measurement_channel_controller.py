"""
File: measurement_channel_controller.py

Purpose: These are the openAPI functions.
These functions call the analyzer "Dracula" DBus service.
The "Dracula" DBus service will perform the low-level part of the openAPIs.
"""

import CDBusDraculaService


def measurement_cancel_post():  # noqa: E501
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_cancel_post()
    return str_rtn

def measurement_consumable_consumable_uuid_post(consumable_uuid):  # noqa: E501
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_consumable_consumable_uuid_post(consumable_uuid)
    return str_rtn

def measurement_file_post(inline_object1):  # noqa: E501
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_file_post(inline_object1)
    return str_rtn

def measurement_results_get(start_datetime=None, end_datetime=None):  # noqa: E501
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_results_get(start_datetime, end_datetime)
    return str_rtn

def measurement_results_latest_get():  # noqa: E501
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_results_latest_get()
    return str_rtn

def measurement_script_post(inline_object):  # noqa: E501
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_script_post(inline_object)
    return str_rtn

def measurement_supported_consumables_get():  # noqa: E501
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_supported_consumables_get()
    return str_rtn
