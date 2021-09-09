# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

import os, sys
cwd = os.getcwd()
sys.path.append(cwd + "/../..") # Adds higher directory to python modules path.

from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.measurement_result import MeasurementResult  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMeasurementChannelController(BaseTestCase):
    """MeasurementChannelController integration test stubs"""

    def test_measurement_cancel_post(self):
        """Test case for measurement_cancel_post

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/cancel',
            method='POST',
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
        # TypeError: measurement_file_post() missing 1 required positional argument: 'inline_object1'
        inline_object1 = InlineObject1(filename = "test_file_name.abc")
        print(inline_object1)
        print("test_measurement_file_post() inline_object1 type: %s" % (type(inline_object1)))
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

    def test_measurement_results_get(self):
        """Test case for measurement_results_get

        
        """
        query_string = [('start_datetime', '2013-10-20T19:20:30+01:00'),
                        ('end_datetime', '2013-10-20T19:20:30+01:00')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/results',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_results_latest_get(self):
        """Test case for measurement_results_latest_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/measurement/results/latest',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_measurement_script_post(self):
        """Test case for measurement_script_post

        
        """
        # TypeError: measurement_script_post() missing 1 required positional argument: 'inline_object'
        inline_object = InlineObject(script="this is a script")
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
