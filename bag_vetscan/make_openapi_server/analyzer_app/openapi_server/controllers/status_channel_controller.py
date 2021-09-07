import connexion
import six

from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util


def status_currently_activated_events_get():  # noqa: E501
    """status_currently_activated_events_get

    The HUB is requesting the analyzer respond with a list of all currently activated events # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def status_operational_get():  # noqa: E501
    """status_operational_get

    The HUB can use send this message to get the status of an analyzer # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'
