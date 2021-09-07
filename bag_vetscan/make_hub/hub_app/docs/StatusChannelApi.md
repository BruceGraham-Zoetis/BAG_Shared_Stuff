# openapi_client.StatusChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_currently_activated_events_get**](StatusChannelApi.md#status_currently_activated_events_get) | **GET** /status/currently_activated_events | 
[**status_operational_get**](StatusChannelApi.md#status_operational_get) | **GET** /status/operational | 


# **status_currently_activated_events_get**
> InlineResponse2002 status_currently_activated_events_get()



The HUB is requesting the analyzer respond with a list of all currently activated events

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
    api_instance = openapi_client.StatusChannelApi(api_client)
    
    try:
        api_response = api_instance.status_currently_activated_events_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusChannelApi->status_currently_activated_events_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer is responding with a list of all currently activated events |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_operational_get**
> InlineResponse2001 status_operational_get()



The HUB can use send this message to get the status of an analyzer

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
    api_instance = openapi_client.StatusChannelApi(api_client)
    
    try:
        api_response = api_instance.status_operational_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusChannelApi->status_operational_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer is responding with its status |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

