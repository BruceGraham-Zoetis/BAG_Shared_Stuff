# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, filename=None):  # noqa: E501
        """InlineObject1 - a model defined in OpenAPI

        :param filename: The filename of this InlineObject1.  # noqa: E501
        :type filename: str
        """
        self.openapi_types = {
            'filename': str
        }

        self.attribute_map = {
            'filename': 'filename'
        }

        self._filename = filename

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_1 of this InlineObject1.  # noqa: E501
        :rtype: InlineObject1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def filename(self):
        """Gets the filename of this InlineObject1.

        This string will the full path to the file that stores the measurement script as it is stored on the analyzer  # noqa: E501

        :return: The filename of this InlineObject1.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this InlineObject1.

        This string will the full path to the file that stores the measurement script as it is stored on the analyzer  # noqa: E501

        :param filename: The filename of this InlineObject1.
        :type filename: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename