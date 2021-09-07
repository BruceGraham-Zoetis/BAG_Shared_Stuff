# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_object2 import InlineObject2  # noqa: E501
from openapi_server.models.inline_object3 import InlineObject3  # noqa: E501
from openapi_server.models.inline_object4 import InlineObject4  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPromptsChannelController(BaseTestCase):
    """PromptsChannelController integration test stubs"""

    def test_prompts_notification_ack_post(self):
        """Test case for prompts_notification_ack_post

        
        """
        inline_object3 = openapi_server.InlineObject3()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/prompts/notification_ack',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object3),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_prompts_option_chosen_post(self):
        """Test case for prompts_option_chosen_post

        
        """
        inline_object2 = openapi_server.InlineObject2()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/prompts/option_chosen',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object2),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_prompts_qr_scanned_post(self):
        """Test case for prompts_qr_scanned_post

        
        """
        inline_object4 = openapi_server.InlineObject4()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/prompts/qr_scanned',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object4),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
