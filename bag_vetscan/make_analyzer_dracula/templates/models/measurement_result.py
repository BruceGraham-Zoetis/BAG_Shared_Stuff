# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class MeasurementResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, consumable_name=None, start_date_and_time=None, end_date_and_time=None, duration_sec=None, result=None, test_results=None):  # noqa: E501
        """MeasurementResult - a model defined in OpenAPI

        :param consumable_name: The consumable_name of this MeasurementResult.  # noqa: E501
        :type consumable_name: str
        :param start_date_and_time: The start_date_and_time of this MeasurementResult.  # noqa: E501
        :type start_date_and_time: str
        :param end_date_and_time: The end_date_and_time of this MeasurementResult.  # noqa: E501
        :type end_date_and_time: str
        :param duration_sec: The duration_sec of this MeasurementResult.  # noqa: E501
        :type duration_sec: float
        :param result: The result of this MeasurementResult.  # noqa: E501
        :type result: str
        :param test_results: The test_results of this MeasurementResult.  # noqa: E501
        :type test_results: object
        """
        self.openapi_types = {
            'consumable_name': str,
            'start_date_and_time': str,
            'end_date_and_time': str,
            'duration_sec': float,
            'result': str,
            'test_results': object
        }

        self.attribute_map = {
            'consumable_name': 'consumable_name',
            'start_date_and_time': 'start_date_and_time',
            'end_date_and_time': 'end_date_and_time',
            'duration_sec': 'duration_sec',
            'result': 'result',
            'test_results': 'test_results'
        }

        self._consumable_name = consumable_name
        self._start_date_and_time = start_date_and_time
        self._end_date_and_time = end_date_and_time
        self._duration_sec = duration_sec
        self._result = result
        self._test_results = test_results

    @classmethod
    def from_dict(cls, dikt) -> 'MeasurementResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The measurement_result of this MeasurementResult.  # noqa: E501
        :rtype: MeasurementResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def consumable_name(self):
        """Gets the consumable_name of this MeasurementResult.

        A descriptive name of the consumable that can be used to uniquely identify it  # noqa: E501

        :return: The consumable_name of this MeasurementResult.
        :rtype: str
        """
        return self._consumable_name

    @consumable_name.setter
    def consumable_name(self, consumable_name):
        """Sets the consumable_name of this MeasurementResult.

        A descriptive name of the consumable that can be used to uniquely identify it  # noqa: E501

        :param consumable_name: The consumable_name of this MeasurementResult.
        :type consumable_name: str
        """

        self._consumable_name = consumable_name

    @property
    def start_date_and_time(self):
        """Gets the start_date_and_time of this MeasurementResult.

        The local date and time the measurement was started in format MM-DD-YYYY HH:MM:SS  # noqa: E501

        :return: The start_date_and_time of this MeasurementResult.
        :rtype: str
        """
        return self._start_date_and_time

    @start_date_and_time.setter
    def start_date_and_time(self, start_date_and_time):
        """Sets the start_date_and_time of this MeasurementResult.

        The local date and time the measurement was started in format MM-DD-YYYY HH:MM:SS  # noqa: E501

        :param start_date_and_time: The start_date_and_time of this MeasurementResult.
        :type start_date_and_time: str
        """

        self._start_date_and_time = start_date_and_time

    @property
    def end_date_and_time(self):
        """Gets the end_date_and_time of this MeasurementResult.

        The local date and time the measurement ended in format MM-DD-YYYY HH:MM:SS  # noqa: E501

        :return: The end_date_and_time of this MeasurementResult.
        :rtype: str
        """
        return self._end_date_and_time

    @end_date_and_time.setter
    def end_date_and_time(self, end_date_and_time):
        """Sets the end_date_and_time of this MeasurementResult.

        The local date and time the measurement ended in format MM-DD-YYYY HH:MM:SS  # noqa: E501

        :param end_date_and_time: The end_date_and_time of this MeasurementResult.
        :type end_date_and_time: str
        """

        self._end_date_and_time = end_date_and_time

    @property
    def duration_sec(self):
        """Gets the duration_sec of this MeasurementResult.

        The number of seconds the measurement took from start to end  # noqa: E501

        :return: The duration_sec of this MeasurementResult.
        :rtype: float
        """
        return self._duration_sec

    @duration_sec.setter
    def duration_sec(self, duration_sec):
        """Sets the duration_sec of this MeasurementResult.

        The number of seconds the measurement took from start to end  # noqa: E501

        :param duration_sec: The duration_sec of this MeasurementResult.
        :type duration_sec: float
        """
        if duration_sec is not None and duration_sec > 9999:  # noqa: E501
            raise ValueError("Invalid value for `duration_sec`, must be a value less than or equal to `9999`")  # noqa: E501
        if duration_sec is not None and duration_sec < 0:  # noqa: E501
            raise ValueError("Invalid value for `duration_sec`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration_sec = duration_sec

    @property
    def result(self):
        """Gets the result of this MeasurementResult.

        The overall result of the measurement  # noqa: E501

        :return: The result of this MeasurementResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this MeasurementResult.

        The overall result of the measurement  # noqa: E501

        :param result: The result of this MeasurementResult.
        :type result: str
        """
        allowed_values = ["Failed", "Cancelled", "Completed"]  # noqa: E501
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def test_results(self):
        """Gets the test_results of this MeasurementResult.

        The test results.  Will need to flush this out as we go on as to what this looks like  # noqa: E501

        :return: The test_results of this MeasurementResult.
        :rtype: object
        """
        return self._test_results

    @test_results.setter
    def test_results(self, test_results):
        """Sets the test_results of this MeasurementResult.

        The test results.  Will need to flush this out as we go on as to what this looks like  # noqa: E501

        :param test_results: The test_results of this MeasurementResult.
        :type test_results: object
        """

        self._test_results = test_results