import connexion
import six

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server import util

import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
from CDBusDraculaService import CDBusDraculaService


def control_light_blink_put():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.control_light_blink_put()
    return strRtn

def control_light_off_put():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.control_light_off_put()
    return strRtn

def control_power_off_put():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.control_power_off_put()
    return strRtn

def control_power_reboot_put():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.control_power_reboot_put()
    return strRtn
