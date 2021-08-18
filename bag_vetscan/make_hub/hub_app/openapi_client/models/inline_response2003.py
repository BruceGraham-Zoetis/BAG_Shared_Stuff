# coding: utf-8

"""
    Analyzer and HUB API

    The definition of the software interface between analyzers and the HUB.  The interface will be implemented as a RESTful interface with all server endpoints hosted on the Analyzer.  The following requirements will be met by all interfaces:  1. All data passed back from server shall be in JSON format. 2. All query parameters and JSON data properties shall be named using snake case and be all lower case. 4. All data types that describe a measurement value shall end with an underscore followed by the unit of that physical value.  i.e. motor_current_ma.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class InlineResponse2003(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currently_activated_events': 'list[EventInfo]'
    }

    attribute_map = {
        'currently_activated_events': 'currently_activated_events'
    }

    def __init__(self, currently_activated_events=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2003 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._currently_activated_events = None
        self.discriminator = None

        self.currently_activated_events = currently_activated_events

    @property
    def currently_activated_events(self):
        """Gets the currently_activated_events of this InlineResponse2003.  # noqa: E501

        An array of all events that are currently activated  # noqa: E501

        :return: The currently_activated_events of this InlineResponse2003.  # noqa: E501
        :rtype: list[EventInfo]
        """
        return self._currently_activated_events

    @currently_activated_events.setter
    def currently_activated_events(self, currently_activated_events):
        """Sets the currently_activated_events of this InlineResponse2003.

        An array of all events that are currently activated  # noqa: E501

        :param currently_activated_events: The currently_activated_events of this InlineResponse2003.  # noqa: E501
        :type currently_activated_events: list[EventInfo]
        """
        if self.local_vars_configuration.client_side_validation and currently_activated_events is None:  # noqa: E501
            raise ValueError("Invalid value for `currently_activated_events`, must not be `None`")  # noqa: E501

        self._currently_activated_events = currently_activated_events

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2003):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2003):
            return True

        return self.to_dict() != other.to_dict()
