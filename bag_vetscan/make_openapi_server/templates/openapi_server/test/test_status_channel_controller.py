# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

import os, sys
cwd = os.getcwd()
sys.path.append(cwd + "/../..") # Adds higher directory to python modules path.

from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.test import BaseTestCase


class TestStatusChannelController(BaseTestCase):
    """StatusChannelController integration test stubs"""

    def test_status_currently_activated_events_get(self):
        """Test case for status_currently_activated_events_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/status/currently_activated_events',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_status_operational_get(self):
        """Test case for status_operational_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/status/operational',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
