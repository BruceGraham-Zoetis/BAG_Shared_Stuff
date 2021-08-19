# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.measurement_result import MeasurementResult  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMeasurementChannelController(BaseTestCase):
    """MeasurementChannelController integration test stubs"""

    def test_channel_measurement_get_measurement_status(self):
        """Test case for channel_measurement_get_measurement_status

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/status',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_cancel_delete(self):
        """Test case for measurement_cancel_delete

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/cancel',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_consumable_consumable_uuid_post(self):
        """Test case for measurement_consumable_consumable_uuid_post

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/consumable/{consumable_uuid}'.format(consumable_uuid='consumable_uuid_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_file_post(self):
        """Test case for measurement_file_post

        
        """
        inline_object1 = openapi_server.InlineObject1()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/measurement/file',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object1),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_past_results_get(self):
        """Test case for measurement_past_results_get

        
        """
        query_string = [('start_time', '23:13:01'),
                        ('start_date', '2021-05-13'),
                        ('end_time', '06:05:23'),
                        ('end_date', '2021-05-15')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/past_results',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_result_get(self):
        """Test case for measurement_result_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/result',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_script_post(self):
        """Test case for measurement_script_post

        
        """
        inline_object = openapi_server.InlineObject()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/measurement/script',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_supported_consumables_get(self):
        """Test case for measurement_supported_consumables_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/supported_consumables',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
