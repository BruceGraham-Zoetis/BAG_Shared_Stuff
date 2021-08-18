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


class MeasurementResult(object):
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
        'consumable_name': 'str',
        'start_date_and_time': 'str',
        'end_date_and_time': 'str',
        'duration_sec': 'float',
        'result': 'str',
        'test_results': 'object'
    }

    attribute_map = {
        'consumable_name': 'consumable_name',
        'start_date_and_time': 'start_date_and_time',
        'end_date_and_time': 'end_date_and_time',
        'duration_sec': 'duration_sec',
        'result': 'result',
        'test_results': 'test_results'
    }

    def __init__(self, consumable_name=None, start_date_and_time=None, end_date_and_time=None, duration_sec=None, result=None, test_results=None, local_vars_configuration=None):  # noqa: E501
        """MeasurementResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._consumable_name = None
        self._start_date_and_time = None
        self._end_date_and_time = None
        self._duration_sec = None
        self._result = None
        self._test_results = None
        self.discriminator = None

        if consumable_name is not None:
            self.consumable_name = consumable_name
        if start_date_and_time is not None:
            self.start_date_and_time = start_date_and_time
        if end_date_and_time is not None:
            self.end_date_and_time = end_date_and_time
        if duration_sec is not None:
            self.duration_sec = duration_sec
        if result is not None:
            self.result = result
        if test_results is not None:
            self.test_results = test_results

    @property
    def consumable_name(self):
        """Gets the consumable_name of this MeasurementResult.  # noqa: E501

        A descriptive name of the consumable that can be used to uniquely identify it  # noqa: E501

        :return: The consumable_name of this MeasurementResult.  # noqa: E501
        :rtype: str
        """
        return self._consumable_name

    @consumable_name.setter
    def consumable_name(self, consumable_name):
        """Sets the consumable_name of this MeasurementResult.

        A descriptive name of the consumable that can be used to uniquely identify it  # noqa: E501

        :param consumable_name: The consumable_name of this MeasurementResult.  # noqa: E501
        :type consumable_name: str
        """

        self._consumable_name = consumable_name

    @property
    def start_date_and_time(self):
        """Gets the start_date_and_time of this MeasurementResult.  # noqa: E501

        The local date and time the measurement was started in format MM-DD-YYYY HH:MM:SS  # noqa: E501

        :return: The start_date_and_time of this MeasurementResult.  # noqa: E501
        :rtype: str
        """
        return self._start_date_and_time

    @start_date_and_time.setter
    def start_date_and_time(self, start_date_and_time):
        """Sets the start_date_and_time of this MeasurementResult.

        The local date and time the measurement was started in format MM-DD-YYYY HH:MM:SS  # noqa: E501

        :param start_date_and_time: The start_date_and_time of this MeasurementResult.  # noqa: E501
        :type start_date_and_time: str
        """

        self._start_date_and_time = start_date_and_time

    @property
    def end_date_and_time(self):
        """Gets the end_date_and_time of this MeasurementResult.  # noqa: E501

        The local date and time the measurement ended in format MM-DD-YYYY HH:MM:SS  # noqa: E501

        :return: The end_date_and_time of this MeasurementResult.  # noqa: E501
        :rtype: str
        """
        return self._end_date_and_time

    @end_date_and_time.setter
    def end_date_and_time(self, end_date_and_time):
        """Sets the end_date_and_time of this MeasurementResult.

        The local date and time the measurement ended in format MM-DD-YYYY HH:MM:SS  # noqa: E501

        :param end_date_and_time: The end_date_and_time of this MeasurementResult.  # noqa: E501
        :type end_date_and_time: str
        """

        self._end_date_and_time = end_date_and_time

    @property
    def duration_sec(self):
        """Gets the duration_sec of this MeasurementResult.  # noqa: E501

        The number of seconds the measurement took from start to end  # noqa: E501

        :return: The duration_sec of this MeasurementResult.  # noqa: E501
        :rtype: float
        """
        return self._duration_sec

    @duration_sec.setter
    def duration_sec(self, duration_sec):
        """Sets the duration_sec of this MeasurementResult.

        The number of seconds the measurement took from start to end  # noqa: E501

        :param duration_sec: The duration_sec of this MeasurementResult.  # noqa: E501
        :type duration_sec: float
        """
        if (self.local_vars_configuration.client_side_validation and
                duration_sec is not None and duration_sec > 9999):  # noqa: E501
            raise ValueError("Invalid value for `duration_sec`, must be a value less than or equal to `9999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration_sec is not None and duration_sec < 0):  # noqa: E501
            raise ValueError("Invalid value for `duration_sec`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration_sec = duration_sec

    @property
    def result(self):
        """Gets the result of this MeasurementResult.  # noqa: E501

        The overall result of the measurement  # noqa: E501

        :return: The result of this MeasurementResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this MeasurementResult.

        The overall result of the measurement  # noqa: E501

        :param result: The result of this MeasurementResult.  # noqa: E501
        :type result: str
        """
        allowed_values = ["Failed", "Cancelled", "Completed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and result not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def test_results(self):
        """Gets the test_results of this MeasurementResult.  # noqa: E501

        The test results.  Will need to flush this out as we go on as to what this looks like  # noqa: E501

        :return: The test_results of this MeasurementResult.  # noqa: E501
        :rtype: object
        """
        return self._test_results

    @test_results.setter
    def test_results(self, test_results):
        """Sets the test_results of this MeasurementResult.

        The test results.  Will need to flush this out as we go on as to what this looks like  # noqa: E501

        :param test_results: The test_results of this MeasurementResult.  # noqa: E501
        :type test_results: object
        """

        self._test_results = test_results

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
        if not isinstance(other, MeasurementResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeasurementResult):
            return True

        return self.to_dict() != other.to_dict()