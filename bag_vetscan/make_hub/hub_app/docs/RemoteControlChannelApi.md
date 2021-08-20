# openapi_client.RemoteControlChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_remote_control_put_remote_control_light_off**](RemoteControlChannelApi.md#channel_remote_control_put_remote_control_light_off) | **PUT** /control/light/off | 


# **channel_remote_control_put_remote_control_light_off**
> channel_remote_control_put_remote_control_light_off()



Cause an analyzer to turn off its light ring.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RemoteControlChannelApi(api_client)
    
    try:
        api_instance.channel_remote_control_put_remote_control_light_off()
    except ApiException as e:
        print("Exception when calling RemoteControlChannelApi->channel_remote_control_put_remote_control_light_off: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer was successful the light ring is off as requested by the HUB |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

