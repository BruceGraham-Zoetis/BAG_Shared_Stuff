# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400


async def test_control_light_blink_put(client):
    """Test case for control_light_blink_put

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/control/light/blink',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_control_light_off_put(client):
    """Test case for control_light_off_put

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/control/light/off',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_control_power_off_put(client):
    """Test case for control_power_off_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/control/power/off',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_control_power_reboot_put(client):
    """Test case for control_power_reboot_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/control/power/reboot',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

