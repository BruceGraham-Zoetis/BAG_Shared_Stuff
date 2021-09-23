#!/usr/bin/env python3

"""
File: measurement_channel_controller.py

Purpose: DBus service interface for the dracula analyzer app.
"""

import CAnalyzer


def measurement_cancel_post(self : CAnalyzer):
    """measurement_cancel_post

    The HUB is requesting the analyzer cancel the measurement that is currently being performed # noqa: E501


    :rtype: InlineResponse200
    """
    dict_rtn = self.operation_current.cancel()
    return dict_rtn


def measurement_consumable_consumable_uuid_post(self : CAnalyzer, consumable_uuid):
    """measurement_consumable_consumable_uuid_post

    Start an analyzer measurement with a specific consumable # noqa: E501

    :param consumable_uuid: The UUID of the consumable
    :type consumable_uuid: str

    :rtype: InlineResponse200
    """
    
    #TODO consumable_uuid

    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn


def measurement_file_post(self : CAnalyzer, body_file_json):
    """measurement_file_post

    Start an analyzer measurement script as described in a file stored on the analyzer.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param inline_object1: 
    :type inline_object1: dict | bytes

    :rtype: InlineResponse200
    """
    # TODO - inline_object1
    
    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn


def measurement_results_get(self : CAnalyzer, start_datetime, end_datetime):
    dict_rtn = self.operation_current.measurement_results_get(start_datetime, end_datetime)
    return dict_rtn


def measurement_result_get(self : CAnalyzer):
    """measurement_result_get

    The HUB requests that the analyzer return the result of the most recent measurement performed # noqa: E501


    :rtype: MeasurementResult
    """

    dict_rtn = self.operation_current.get_status()
    return dict_rtn


def measurement_results_latest_get(self : CAnalyzer):
    dict_rtn = self.operation_current.get_status()
    return dict_rtn


def measurement_script_post(self : CAnalyzer, body_script_json):
    """measurement_script_post

    Start an analyzer measurement script sent as a string.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: InlineResponse200
    """

    # TODO -something with the object

    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn


def measurement_supported_consumables_get(self : CAnalyzer):
    """measurement_supported_consumables_get

    Return a list (Python dict) of all consumable types the analyzer supports. Each consumable returned will include a universally unique identifier, which will be used by the IC when starting a measurement. Any information required to run a consumable will be described in the response using the JSON Schema format (https://json-schema.org/). # noqa: E501


    :rtype: object
    """
    
    dict_consumables = {
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

    return dict_consumables
