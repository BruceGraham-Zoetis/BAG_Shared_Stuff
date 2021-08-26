import connexion
import six

from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.measurement_result import MeasurementResult  # noqa: E501
from openapi_server import util

import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
from CDBusDraculaService import CDBusDraculaService


def channel_measurement_get_measurement_status():  # noqa: E501
    """channel_measurement_get_measurement_status

    The HUB is requesting the analyzer return the status of the current measurement being performed # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def measurement_cancel_delete():  # noqa: E501
    """measurement_cancel_delete

    The HUB is requesting the analyzer cancel the measurement that is currently being performed # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def measurement_consumable_consumable_uuid_post(consumable_uuid):  # noqa: E501
    """measurement_consumable_consumable_uuid_post

    Start an analyzer measurement with a specific consumable # noqa: E501

    :param consumable_uuid: The UUID of the consumable
    :type consumable_uuid: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def measurement_file_post(inline_object1):  # noqa: E501
    """measurement_file_post

    Start an analyzer measurement script as described in a file stored on the analyzer.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param inline_object1: 
    :type inline_object1: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        inline_object1 = InlineObject1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def measurement_past_results_get(start_time, start_date, end_time, end_date):  # noqa: E501
    """measurement_past_results_get

    The HUB is requesting the analyzer send past results between two times # noqa: E501

    :param start_time: The time to start looking for results to return
    :type start_time: str
    :param start_date: The date to start looking for results to return
    :type start_date: str
    :param end_time: The time to stop looking for results to return
    :type end_time: str
    :param end_date: The date to stop looking for results to return
    :type end_date: str

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def measurement_result_get():  # noqa: E501
    """measurement_result_get

    The HUB requests that the analyzer return the result of the most recent measurement performed # noqa: E501


    :rtype: MeasurementResult
    """
    return 'do some magic!'


def measurement_script_post(inline_object):  # noqa: E501
    """measurement_script_post

    Start an analyzer measurement script sent as a string.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        inline_object = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def measurement_supported_consumables_get():
    oDracula = CDBusDraculaService()
    lstConsumables = oDracula.draculad.measurement_supported_consumables_get()
    return lstConsumables
