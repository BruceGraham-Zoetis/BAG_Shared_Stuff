# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

import os, sys
cwd = os.getcwd()
sys.path.append(cwd + "/../..") # Adds higher directory to python modules path.

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

        # TypeError: prompts_notification_ack_post() missing 1 required positional argument: 'inline_object3'
        #data_param=json.dumps(InlineObject3(correlation_id= '123'))
        #{"correlation_id": "123"}
        #<class 'str'>

        # AttributeError: 'InlineObject3' object has no attribute 'items'
        #data_param=InlineObject3()
        #{'correlation_id': None}
        #<class 'openapi_server.models.inline_object3.InlineObject3'>

        # AttributeError: 'list' object has no attribute 'items'
        #data_param=['correlation_id', '123']
        #['correlation_id', '123']
        #<class 'list'>

        # AttributeError: 'InlineObject3' object has no attribute 'items'
        #data_param=InlineObject3({'correlation_id', '123'})
        #{'correlation_id': {'123', 'correlation_id'}}
        #<class 'openapi_server.models.inline_object3.InlineObject3'>

        # AttributeError: 'InlineObject3' object has no attribute 'items'
        #data_param=InlineObject3(correlation_id= '123')
        #{'correlation_id': '123'}
        #<class 'openapi_server.models.inline_object3.InlineObject3'>

        # AttributeError: 'InlineObject3' object has no attribute 'items'
        #data_param=InlineObject3(correlation_id={'correlation_id':'123'})
        #{'correlation_id': {'correlation_id': '123'}}
        #<class 'openapi_server.models.inline_object3.InlineObject3'>

        # AttributeError: 'InlineObject3' object has no attribute 'items'
        #ob = InlineObject3()
        #ob.correlation_id = 123
        #data_param = ob
        #{'correlation_id': 123}
        #<class 'openapi_server.models.inline_object3.InlineObject3'>

        # validation error: 123 is not of type 'string' - 'correlation_id'
        #ob = InlineObject3()
        #ob.correlation_id = 123
        #data_param=json.dumps(ob)
        #{"correlation_id": 123}
        #<class 'str'>

        # missing 1 required positional argument: 'inline_object3'
        #ob = InlineObject3()
        #ob.correlation_id = "123"
        #data_param=json.dumps(ob)
        #{"correlation_id": "123"}
        #<class 'str'>

        # AttributeError: 'InlineObject3' object has no attribute 'items'
        ob = InlineObject3()
        data_param = ob.from_dict({'correlation_id': '123'})
        #{'correlation_id': '123'}
        #<class 'openapi_server.models.inline_object3.InlineObject3'>


        print(data_param)
        print(type(data_param))

        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/prompts/notification_ack',
            method='POST',
            headers=headers,
            data=data_param,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_prompts_option_chosen_post(self):
        """Test case for prompts_option_chosen_post

        
        """
        inline_object2 = InlineObject2()
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
        inline_object4 = InlineObject4()
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
