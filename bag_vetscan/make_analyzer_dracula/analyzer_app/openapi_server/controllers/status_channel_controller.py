from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response2002 import InlineResponse2002
from openapi_server.models.inline_response2003 import InlineResponse2003
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server import util


async def status_currently_activated_events_get(request: web.Request, ) -> web.Response:
    """status_currently_activated_events_get

    The HUB is requesting the analyzer respond with a list of all currently activated events


    """
    return web.Response(status=200)


async def status_operational_get(request: web.Request, ) -> web.Response:
    """status_operational_get

    The HUB can use send this message to get the status of an analyzer


    """
    return web.Response(status=200)
