import connexion
import six

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server import util

import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
from CDBusDraculaService import CDBusDraculaService


def configuration_factory_reset_put():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.configuration_factory_reset_put()
    return strRtn

def configuration_get():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.configuration_get()
    return strRtn

def configuration_put(body):
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.configuration_put(body)
    return strRtn

def configuration_schema_get():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.configuration_schema_get()
    return strRtn
