import connexion
import six

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server import util

import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
from CDBusDraculaService import CDBusDraculaService


def configuration_factory_reset_put():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.configuration_factory_reset_put()
    return strRtn

def configuration_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.configuration_get()
    return strRtn

def configuration_put(body):
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.configuration_put(body)
    return strRtn

def configuration_schema_get():
    str_rtn = CDBusDraculaService.g_dbus_dracula_service.configuration_schema_get()
    return strRtn
