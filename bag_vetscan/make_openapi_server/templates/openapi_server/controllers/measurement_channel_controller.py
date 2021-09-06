"""
File: measurement_channel_controller.py

Purpose: These are the openAPI functions.
These functions call the analyzer "Dracula" DBus service.
The "Dracula" DBus service will perform the low-level part of the openAPIs.
"""


import CDBusDraculaService


def channel_measurement_get_measurement_status():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.channel_measurement_get_measurement_status()
    return str_rtn

def measurement_cancel_delete():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_cancel_delete()
    return str_rtn

def measurement_consumable_consumable_uuid_post(consumable_uuid):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_consumable_consumable_uuid_post(consumable_uuid)
    return str_rtn

def measurement_file_post(inline_object1):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_file_post(inline_object1)
    return str_rtn

def measurement_past_results_get(start_time, start_date, end_time, end_date):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_past_results_get(start_time, start_date, end_time, end_date)
    return str_rtn

def measurement_result_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_result_get()
    return str_rtn

def measurement_script_post(inline_object):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_script_post(inline_object)
    return str_rtn

def measurement_supported_consumables_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.draculad.measurement_supported_consumables_get()
    return str_rtn
