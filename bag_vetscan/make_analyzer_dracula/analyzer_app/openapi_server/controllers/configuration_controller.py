from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server import util


async def configuration_factory_reset_put(request: web.Request, ) -> web.Response:
    """configuration_factory_reset_put

    Restore the analyzer to the state it was in when it left the factory. All settings and data are removed.


    """
    return web.Response(status=200)


async def configuration_get(request: web.Request, ) -> web.Response:
    """configuration_get

    Request the configuration from the analyzer


    """
    return web.Response(status=200)


async def configuration_put(request: web.Request, body) -> web.Response:
    """configuration_put

    Set the configuration of the analyzer

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def configuration_schema_get(request: web.Request, ) -> web.Response:
    """configuration_schema_get

    Request the configuration schema from the analyzer


    """
    return web.Response(status=200)
