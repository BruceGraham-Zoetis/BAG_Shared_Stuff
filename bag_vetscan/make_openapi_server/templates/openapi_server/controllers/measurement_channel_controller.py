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
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.channel_measurement_get_measurement_status()
    return strRtn

def measurement_cancel_delete():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.measurement_cancel_delete()
    return strRtn

def measurement_consumable_consumable_uuid_post(consumable_uuid):
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.measurement_consumable_consumable_uuid_post(consumable_uuid)
    return strRtn

def measurement_file_post(inline_object1):
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.measurement_file_post(inline_object1)
    return strRtn

def measurement_past_results_get(start_time, start_date, end_time, end_date):
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.measurement_past_results_get(start_time, start_date, end_time, end_date)
    return strRtn

def measurement_result_get():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.measurement_result_get()
    return strRtn

def measurement_script_post(inline_object):
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.measurement_script_post(inline_object)
    return strRtn

def measurement_supported_consumables_get():
    oDracula = CDBusDraculaService()
    strConsumables = oDracula.draculad.measurement_supported_consumables_get()
    return strConsumables
