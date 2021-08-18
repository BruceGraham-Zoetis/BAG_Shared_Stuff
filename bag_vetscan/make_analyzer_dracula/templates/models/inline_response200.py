# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.measurement_status import MeasurementStatus
from openapi_server import util

from openapi_server.models.measurement_status import MeasurementStatus  # noqa: E501

class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, measurement_id=None, elapsed_time_msec=None, measurement_status=None, status_detail=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param measurement_id: The measurement_id of this InlineResponse200.  # noqa: E501
        :type measurement_id: str
        :param elapsed_time_msec: The elapsed_time_msec of this InlineResponse200.  # noqa: E501
        :type elapsed_time_msec: float
        :param measurement_status: The measurement_status of this InlineResponse200.  # noqa: E501
        :type measurement_status: MeasurementStatus
        :param status_detail: The status_detail of this InlineResponse200.  # noqa: E501
        :type status_detail: str
        """
        self.openapi_types = {
            'measurement_id': str,
            'elapsed_time_msec': float,
            'measurement_status': MeasurementStatus,
            'status_detail': str
        }

        self.attribute_map = {
            'measurement_id': 'measurement_id',
            'elapsed_time_msec': 'elapsed_time_msec',
            'measurement_status': 'measurement_status',
            'status_detail': 'status_detail'
        }

        self._measurement_id = measurement_id
        self._elapsed_time_msec = elapsed_time_msec
        self._measurement_status = measurement_status
        self._status_detail = status_detail

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def measurement_id(self):
        """Gets the measurement_id of this InlineResponse200.

        The ID value for a measurement  # noqa: E501

        :return: The measurement_id of this InlineResponse200.
        :rtype: str
        """
        return self._measurement_id

    @measurement_id.setter
    def measurement_id(self, measurement_id):
        """Sets the measurement_id of this InlineResponse200.

        The ID value for a measurement  # noqa: E501

        :param measurement_id: The measurement_id of this InlineResponse200.
        :type measurement_id: str
        """
        if measurement_id is None:
            raise ValueError("Invalid value for `measurement_id`, must not be `None`")  # noqa: E501

        self._measurement_id = measurement_id

    @property
    def elapsed_time_msec(self):
        """Gets the elapsed_time_msec of this InlineResponse200.

        The time the operation has taken so far  # noqa: E501

        :return: The elapsed_time_msec of this InlineResponse200.
        :rtype: float
        """
        return self._elapsed_time_msec

    @elapsed_time_msec.setter
    def elapsed_time_msec(self, elapsed_time_msec):
        """Sets the elapsed_time_msec of this InlineResponse200.

        The time the operation has taken so far  # noqa: E501

        :param elapsed_time_msec: The elapsed_time_msec of this InlineResponse200.
        :type elapsed_time_msec: float
        """
        if elapsed_time_msec is None:
            raise ValueError("Invalid value for `elapsed_time_msec`, must not be `None`")  # noqa: E501
        if elapsed_time_msec is not None and elapsed_time_msec < 0:  # noqa: E501
            raise ValueError("Invalid value for `elapsed_time_msec`, must be a value greater than or equal to `0`")  # noqa: E501

        self._elapsed_time_msec = elapsed_time_msec

    @property
    def measurement_status(self):
        """Gets the measurement_status of this InlineResponse200.


        :return: The measurement_status of this InlineResponse200.
        :rtype: MeasurementStatus
        """
        return self._measurement_status

    @measurement_status.setter
    def measurement_status(self, measurement_status):
        """Sets the measurement_status of this InlineResponse200.


        :param measurement_status: The measurement_status of this InlineResponse200.
        :type measurement_status: MeasurementStatus
        """
        if measurement_status is None:
            raise ValueError("Invalid value for `measurement_status`, must not be `None`")  # noqa: E501

        self._measurement_status = measurement_status

    @property
    def status_detail(self):
        """Gets the status_detail of this InlineResponse200.

        Additional information in plain text that describes the value status of the analyzer.  If no additional detail is available or necessary, this will be an empty string  # noqa: E501

        :return: The status_detail of this InlineResponse200.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this InlineResponse200.

        Additional information in plain text that describes the value status of the analyzer.  If no additional detail is available or necessary, this will be an empty string  # noqa: E501

        :param status_detail: The status_detail of this InlineResponse200.
        :type status_detail: str
        """
        if status_detail is None:
            raise ValueError("Invalid value for `status_detail`, must not be `None`")  # noqa: E501

        self._status_detail = status_detail
