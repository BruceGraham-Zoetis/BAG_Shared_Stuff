"""
File: prompts_channel_controller.py

Purpose: These are the openAPI functions.
These functions call the analyzer "Dracula" DBus service.
The "Dracula" DBus service will perform the low-level part of the openAPIs.
"""


import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)

import CDBusDraculaService

import connexion
import six

from openapi_server.models.inline_object2 import InlineObject2  # noqa: E501
from openapi_server.models.inline_object3 import InlineObject3  # noqa: E501
from openapi_server.models.inline_object4 import InlineObject4  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util


def prompts_notification_ack_post(inline_object3):  # noqa: E501
    """prompts_notification_ack_post

    Hub is informing the analyzer a notification was acknowledged by the operator in response to a websocket message named notification on the prompts channel. # noqa: E501

    :param inline_object3: 
    :type inline_object3: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object3 = InlineObject3.from_dict(connexion.request.get_json())  # noqa: E501
    return 'TODO - Call the DBus service API'


def prompts_option_chosen_post(inline_object2):  # noqa: E501
    """prompts_option_chosen_post

    Hub is informing the analyzer of an option that was made by the operator in response to a websocket message named choose_option on the prompts channel. # noqa: E501

    :param inline_object2: 
    :type inline_object2: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object2 = InlineObject2.from_dict(connexion.request.get_json())  # noqa: E501
    return 'TODO - Call the DBus service API'


def prompts_qr_scanned_post(inline_object4):  # noqa: E501
    """prompts_qr_scanned_post

    Hub is informing the analyzer of a QR scan attempt in response to a websocket message named scan_qr on the prompts channel. # noqa: E501

    :param inline_object4: 
    :type inline_object4: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object4 = InlineObject4.from_dict(connexion.request.get_json())  # noqa: E501
    return 'TODO - Call the DBus service API'
