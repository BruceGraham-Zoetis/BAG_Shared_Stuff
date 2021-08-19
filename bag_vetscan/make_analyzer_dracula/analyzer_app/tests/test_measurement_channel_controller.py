# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_object import InlineObject
from openapi_server.models.inline_object1 import InlineObject1
from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server.models.inline_response2001 import InlineResponse2001
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.measurement_result import MeasurementResult


async def test_channel_measurement_get_measurement_status(client):
    """Test case for channel_measurement_get_measurement_status

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/measurement/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_measurement_cancel_delete(client):
    """Test case for measurement_cancel_delete

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/measurement/cancel',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_measurement_consumable_consumable_uuid_post(client):
    """Test case for measurement_consumable_consumable_uuid_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/measurement/consumable/{consumable_uuid}'.format(consumable_uuid='consumable_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_measurement_file_post(client):
    """Test case for measurement_file_post

    
    """
    body = openapi_server.InlineObject1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/measurement/file',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_measurement_past_results_get(client):
    """Test case for measurement_past_results_get

    
    """
    params = [('start_time', '23:13:01'),
                    ('start_date', '2021-05-13'),
                    ('end_time', '06:05:23'),
                    ('end_date', '2021-05-15')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/measurement/past_results',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_measurement_result_get(client):
    """Test case for measurement_result_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/measurement/result',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_measurement_script_post(client):
    """Test case for measurement_script_post

    
    """
    body = openapi_server.InlineObject()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/measurement/script',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_measurement_supported_consumables_get(client):
    """Test case for measurement_supported_consumables_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/measurement/supported_consumables',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

