#!/usr/bin/env python3

"""
File: control_channel_controller.py

Purpose: DBus service interface for the dracula analyzer app.
"""


def control_light_blink_put():
    """control_light_blink_put

    Cause an analyzer to blink its light ring.  The purpose of this is to identify an analyzer. If you have multiple analyzers of the same kind it is nice to have a way to get a visual que which is which instead of having to read the serial number of each analyzer to identify it. # noqa: E501


    :rtype: None
    """

    lstReturn = {
        "Light": "Blinking"
    }
    #TODO
    return lstReturn


def control_light_off_put():
    """control_light_off_put

    Cause an analyzer to turn off its light ring. # noqa: E501


    :rtype: None
    """

    lstReturn = {
        "Light": "Off"
    }
    #TODO
    return lstReturn



def control_power_off_put():
    """control_power_off_put

    Go from a state of powered to no power. This behavior of this action will depend on what a particular analyzer supports. If it doesn&#39;t support power off, go to &#39;deep sleep&#39; mode # noqa: E501


    :rtype: None
    """

    lstReturn = {
        "Power": "Off"
    }
    #TODO
    return lstReturn


def control_power_reboot_put():
    """control_power_reboot_put

    Request sent from a client to reboot the analyzer (power off and power back on), leaving all settings and data intact # noqa: E501


    :rtype: None
    """

    lstReturn = {
        "Power": "Rebooting"
    }
    #TODO
    return lstReturn
