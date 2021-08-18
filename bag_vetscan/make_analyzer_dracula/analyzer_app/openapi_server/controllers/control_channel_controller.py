import connexion
import six

from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util


def control_light_blink_put():  # noqa: E501
    """control_light_blink_put

    Cause an analyzer to blink its light ring.  The purpose of this is to identify an analyzer. If you have multiple analyzers of the same kind it is nice to have a way to get a visual que which is which instead of having to read the serial number of each analyzer to identify it. # noqa: E501


    :rtype: None
    """

    lstReturn = {
        "Light": "Blinking"
    }
    #TODO
    return lstReturn


def control_light_off_put():  # noqa: E501
    """control_light_off_put

    Cause an analyzer to turn off its light ring. # noqa: E501


    :rtype: None
    """

    lstReturn = {
        "Light": "Off"
    }
    #TODO
    return lstReturn



def control_power_off_put():  # noqa: E501
    """control_power_off_put

    Go from a state of powered to no power. This behavior of this action will depend on what a particular analyzer supports. If it doesn&#39;t support power off, go to &#39;deep sleep&#39; mode # noqa: E501


    :rtype: None
    """

    lstReturn = {
        "Power": "Off"
    }
    #TODO
    return lstReturn


def control_power_reboot_put():  # noqa: E501
    """control_power_reboot_put

    Request sent from a client to reboot the analyzer (power off and power back on), leaving all settings and data intact # noqa: E501


    :rtype: None
    """

    lstReturn = {
        "Power": "Rebooting"
    }
    #TODO
    return lstReturn
