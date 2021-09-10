#!/usr/bin/env python3
"""
File: prompts_channel_controller.py

Purpose: DBus service interface for the dracula analyzer app.
"""

import CAnalyzer


def prompts_notification_ack_post(self : CAnalyzer, inline_object3):  # noqa: E501
    """prompts_notification_ack_post

    Hub is informing the analyzer a notification was acknowledged by the operator in response to a websocket message named notification on the prompts channel. # noqa: E501

    :param inline_object3: 
    :type inline_object3: dict | bytes

    :rtype: None
    """
    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn


def prompts_option_chosen_post(self : CAnalyzer, inline_object2):  # noqa: E501
    """prompts_option_chosen_post

    Hub is informing the analyzer of an option that was made by the operator in response to a websocket message named choose_option on the prompts channel. # noqa: E501

    :param inline_object2: 
    :type inline_object2: dict | bytes

    :rtype: None
    """
    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn


def prompts_qr_scanned_post(self : CAnalyzer, inline_object4):  # noqa: E501
    """prompts_qr_scanned_post

    Hub is informing the analyzer of a QR scan attempt in response to a websocket message named scan_qr on the prompts channel. # noqa: E501

    :param inline_object4: 
    :type inline_object4: dict | bytes

    :rtype: None
    """
    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn
