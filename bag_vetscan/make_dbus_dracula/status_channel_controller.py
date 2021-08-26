#!/usr/bin/env python3

"""
File: status_channel_controller.py

Purpose: DBus service interface for the dracula analyzer app.
"""



def status_currently_activated_events_get():
    """status_currently_activated_events_get

    The HUB is requesting the analyzer respond with a list of all currently activated events # noqa: E501


    :rtype: InlineResponse2003
    """
    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn


def status_operational_get():
    """status_operational_get

    The HUB can use send this message to get the status of an analyzer # noqa: E501


    :rtype: InlineResponse2002
    """
    dictReturn = {
        "status": "done"
    }
    #TODO
    return dictReturn
