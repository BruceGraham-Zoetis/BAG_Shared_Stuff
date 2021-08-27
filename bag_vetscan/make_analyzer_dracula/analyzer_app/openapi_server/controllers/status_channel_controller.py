import connexion
import six

from openapi_server.models.inline_response2002 import InlineResponse2002
from openapi_server.models.inline_response2003 import InlineResponse2003
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server import util

import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
from CDBusDraculaService import CDBusDraculaService


def status_currently_activated_events_get():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.status_currently_activated_events_get()
    return strRtn

def status_operational_get():
    oDracula = CDBusDraculaService()
    strRtn = oDracula.draculad.status_operational_get()
    return strRtn
