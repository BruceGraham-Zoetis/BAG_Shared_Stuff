import connexion
import six

from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server import util


def configuration_factory_reset_put():  # noqa: E501
    """configuration_factory_reset_put

    Restore the analyzer to the state it was in when it left the factory. All settings and data are removed. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def configuration_get():  # noqa: E501
    """configuration_get

    Request the configuration from the analyzer # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def configuration_put(body):  # noqa: E501
    """configuration_put

    Set the configuration of the analyzer # noqa: E501

    :param body: 
    :type body: 

    :rtype: None
    """
    return 'do some magic!'


def configuration_schema_get():  # noqa: E501
    """configuration_schema_get

    Request the configuration schema from the analyzer # noqa: E501


    :rtype: object
    """
    return 'do some magic!'