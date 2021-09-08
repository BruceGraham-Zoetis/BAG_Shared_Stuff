# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

import sys
sys.path.append("../..") # Adds higher directory to python modules path.

from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.test import BaseTestCase


class TestControlChannelController(BaseTestCase):
    """ControlChannelController integration test stubs"""

    def test_control_light_blink_put(self):
        """Test case for control_light_blink_put

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/control/light/blink',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_control_power_off_put(self):
        """Test case for control_power_off_put

        
        """
        headers = { 
        }
        response = self.client.open(
            '/control/power/off',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_control_power_reboot_put(self):
        """Test case for control_power_reboot_put

        
        """
        headers = { 
        }
        response = self.client.open(
            '/control/power/reboot',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
