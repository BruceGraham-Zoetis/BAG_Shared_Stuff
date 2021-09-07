# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, correlation_id=None):  # noqa: E501
        """InlineObject3 - a model defined in OpenAPI

        :param correlation_id: The correlation_id of this InlineObject3.  # noqa: E501
        :type correlation_id: str
        """
        self.openapi_types = {
            'correlation_id': str
        }

        self.attribute_map = {
            'correlation_id': 'correlation_id'
        }

        self._correlation_id = correlation_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject3':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_3 of this InlineObject3.  # noqa: E501
        :rtype: InlineObject3
        """
        return util.deserialize_model(dikt, cls)

    @property
    def correlation_id(self):
        """Gets the correlation_id of this InlineObject3.

        A unique ID that can be used to correlate messages being sent and received  # noqa: E501

        :return: The correlation_id of this InlineObject3.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this InlineObject3.

        A unique ID that can be used to correlate messages being sent and received  # noqa: E501

        :param correlation_id: The correlation_id of this InlineObject3.
        :type correlation_id: str
        """
        if correlation_id is None:
            raise ValueError("Invalid value for `correlation_id`, must not be `None`")  # noqa: E501

        self._correlation_id = correlation_id