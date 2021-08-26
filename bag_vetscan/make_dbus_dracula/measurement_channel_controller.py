#!/usr/bin/env python3

"""
File: measurement_channel_controller.py

Purpose: DBus service interface for the dracula analyzer app.
"""

import json

def channel_measurement_get_measurement_status():
    """channel_measurement_get_measurement_status

    The HUB is requesting the analyzer return the status of the current measurement being performed # noqa: E501


    :rtype: InlineResponse200
    """
    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn


def measurement_cancel_delete():
    """measurement_cancel_delete

    The HUB is requesting the analyzer cancel the measurement that is currently being performed # noqa: E501


    :rtype: InlineResponse200
    """
    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn


def measurement_consumable_consumable_uuid_post(consumable_uuid):
    """measurement_consumable_consumable_uuid_post

    Start an analyzer measurement with a specific consumable # noqa: E501

    :param consumable_uuid: The UUID of the consumable
    :type consumable_uuid: str

    :rtype: InlineResponse200
    """
    
    #TODO consumable_uuid

    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn


def measurement_file_post(inline_object1):
    """measurement_file_post

    Start an analyzer measurement script as described in a file stored on the analyzer.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param inline_object1: 
    :type inline_object1: dict | bytes

    :rtype: InlineResponse200
    """
    # TODO - inline_object1
    
    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn


def measurement_past_results_get(start_time, start_date, end_time, end_date):
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
    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn


def measurement_result_get():
    """measurement_result_get

    The HUB requests that the analyzer return the result of the most recent measurement performed # noqa: E501


    :rtype: MeasurementResult
    """
    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn


def measurement_script_post(inline_object):
    """measurement_script_post

    Start an analyzer measurement script sent as a string.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: InlineResponse200
    """

    # TODO -something with the object

    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn


def measurement_supported_consumables_get():
    """measurement_supported_consumables_get

    Return a list (Python dict) of all consumable types the analyzer supports. Each consumable returned will include a universally unique identifier, which will be used by the IC when starting a measurement. Any information required to run a consumable will be described in the response using the JSON Schema format (https://json-schema.org/). # noqa: E501


    :rtype: object
    """
    
    dictConsumables = {
        "consumables":
        [
            {
                "name": "Coagulation (PT/aPTT) (Coag Combo)",
                "uuid": "0b7ec890-3960-11eb-a081-2790e47ff2f4",
                "type": "cartridge",
                "species": [
                    "*"
                ],
                "duration": "PT7M",
                "assays": [
                    "PT",
                    "aPTT"
                ],
                "schema": {}
            },
            {
                "name": "Feline bloodtyping",
                "uuid": "5ed688be-4376-11eb-8136-3345982818db",
                "type": "cartridge",
                "species": [
                    "Feline"
                ],
                "duration": "PT5M",
                "assays": [
                    ""
                ],
                "schema": {}
            }
        ]
    }

    return dictConsumables
