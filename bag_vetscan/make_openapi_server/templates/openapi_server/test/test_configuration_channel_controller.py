# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

import os, sys
cwd = os.getcwd()
sys.path.append(cwd + "/../..") # Adds higher directory to python modules path.

from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.test import BaseTestCase


class TestConfigurationChannelController(BaseTestCase):
    """ConfigurationChannelController integration test stubs"""

    def test_configuration_factory_reset_put(self):
        """Test case for configuration_factory_reset_put

        
        """
        headers = { 
        }
        response = self.client.open(
            '/configuration/factory_reset',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_configuration_get(self):
        """Test case for configuration_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/configuration',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_configuration_put(self):
        """Test case for configuration_put

        
        """
        body = {'something': 'else'}
        #body = None # bad request
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/configuration',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_configuration_schema_get(self):
        """Test case for configuration_schema_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/configuration/schema',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
