import connexion
import six

from openapi_server.models.inline_object import InlineObject
from openapi_server.models.inline_object1 import InlineObject1
from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server.models.inline_response2001 import InlineResponse2001
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.measurement_result import MeasurementResult
from openapi_server import util

import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
from CDBusDraculaService import CDBusDraculaService


def channel_measurement_get_measurement_status():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.channel_measurement_get_measurement_status()
    return str_rtn

def measurement_cancel_delete():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.measurement_cancel_delete()
    return str_rtn

def measurement_consumable_consumable_uuid_post(consumable_uuid):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.measurement_consumable_consumable_uuid_post(consumable_uuid)
    return str_rtn

def measurement_file_post(inline_object1):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.measurement_file_post(inline_object1)
    return str_rtn

def measurement_past_results_get(start_time, start_date, end_time, end_date):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.measurement_past_results_get(start_time, start_date, end_time, end_date)
    return str_rtn

def measurement_result_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.measurement_result_get()
    return str_rtn

def measurement_script_post(inline_object):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.measurement_script_post(inline_object)
    return str_rtn

def measurement_supported_consumables_get():
    oDracula = CDBusDraculaService()
    strConsumables = oDracula.draculad.measurement_supported_consumables_get()
    return strConsumables
