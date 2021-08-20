# openapi_client.ControlChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**control_light_blink_put**](ControlChannelApi.md#control_light_blink_put) | **PUT** /control/light/blink | 
[**control_power_off_put**](ControlChannelApi.md#control_power_off_put) | **PUT** /control/power/off | 
[**control_power_reboot_put**](ControlChannelApi.md#control_power_reboot_put) | **PUT** /control/power/reboot | 


# **control_light_blink_put**
> control_light_blink_put()



Cause an analyzer to blink its light ring.  The purpose of this is to identify an analyzer. If you have multiple analyzers of the same kind it is nice to have a way to get a visual que which is which instead of having to read the serial number of each analyzer to identify it.

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
    api_instance = openapi_client.ControlChannelApi(api_client)
    
    try:
        api_instance.control_light_blink_put()
    except ApiException as e:
        print("Exception when calling ControlChannelApi->control_light_blink_put: %s\n" % e)
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
**200** | Analyzer was successful blinking the light ring |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_power_off_put**
> control_power_off_put()



Go from a state of powered to no power. This behavior of this action will depend on what a particular analyzer supports. If it doesn't support power off, go to 'deep sleep' mode

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
    api_instance = openapi_client.ControlChannelApi(api_client)
    
    try:
        api_instance.control_power_off_put()
    except ApiException as e:
        print("Exception when calling ControlChannelApi->control_power_off_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer successfully began to power off or go to sleep |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **control_power_reboot_put**
> control_power_reboot_put()



Request sent from a client to reboot the analyzer (power off and power back on), leaving all settings and data intact

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
    api_instance = openapi_client.ControlChannelApi(api_client)
    
    try:
        api_instance.control_power_reboot_put()
    except ApiException as e:
        print("Exception when calling ControlChannelApi->control_power_reboot_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer successfully initiated a reboot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

