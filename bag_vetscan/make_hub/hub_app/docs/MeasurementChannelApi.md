# openapi_client.MeasurementChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measurement_cancel_post**](MeasurementChannelApi.md#measurement_cancel_post) | **POST** /measurement/cancel | 
[**measurement_consumable_consumable_uuid_post**](MeasurementChannelApi.md#measurement_consumable_consumable_uuid_post) | **POST** /measurement/consumable/{consumable_uuid} | 
[**measurement_file_post**](MeasurementChannelApi.md#measurement_file_post) | **POST** /measurement/file | 
[**measurement_results_get**](MeasurementChannelApi.md#measurement_results_get) | **GET** /measurement/results | 
[**measurement_results_latest_get**](MeasurementChannelApi.md#measurement_results_latest_get) | **GET** /measurement/results/latest | 
[**measurement_script_post**](MeasurementChannelApi.md#measurement_script_post) | **POST** /measurement/script | 
[**measurement_supported_consumables_get**](MeasurementChannelApi.md#measurement_supported_consumables_get) | **GET** /measurement/supported_consumables | 


# **measurement_cancel_post**
> measurement_cancel_post()



The HUB is requesting the analyzer cancel the measurement that is currently being performed

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
    api_instance = openapi_client.MeasurementChannelApi(api_client)
    
    try:
        api_instance.measurement_cancel_post()
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_cancel_post: %s\n" % e)
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
**200** | Analyzer successfully began cancelling the measurement |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_consumable_consumable_uuid_post**
> measurement_consumable_consumable_uuid_post(consumable_uuid)



Start an analyzer measurement with a specific consumable

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
    api_instance = openapi_client.MeasurementChannelApi(api_client)
    consumable_uuid = 'consumable_uuid_example' # str | The UUID of the consumable

    try:
        api_instance.measurement_consumable_consumable_uuid_post(consumable_uuid)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_consumable_consumable_uuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumable_uuid** | **str**| The UUID of the consumable | 

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
**200** | Analyzer successfully began measurement |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_file_post**
> measurement_file_post(inline_object1)



Start an analyzer measurement script as described in a file stored on the analyzer.  This is intended for R&D use only and should not be used during normal operation

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
    api_instance = openapi_client.MeasurementChannelApi(api_client)
    inline_object1 = openapi_client.InlineObject1() # InlineObject1 | 

    try:
        api_instance.measurement_file_post(inline_object1)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer successfully began measurement |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_results_get**
> InlineResponse200 measurement_results_get(start_datetime=start_datetime, end_datetime=end_datetime)



The client is requesting the analyzer to send past results between two times

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
    api_instance = openapi_client.MeasurementChannelApi(api_client)
    start_datetime = '2013-10-20T19:20:30+01:00' # datetime | The earliest result. If missing, the analyzer must return the results from as early as possible (optional)
end_datetime = '2013-10-20T19:20:30+01:00' # datetime | The latest time for a result. If missing, the analyzer must return all results from 'from' untill present time. (optional)

    try:
        api_response = api_instance.measurement_results_get(start_datetime=start_datetime, end_datetime=end_datetime)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_datetime** | **datetime**| The earliest result. If missing, the analyzer must return the results from as early as possible | [optional] 
 **end_datetime** | **datetime**| The latest time for a result. If missing, the analyzer must return all results from &#39;from&#39; untill present time. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer is responding with the results of all measurements taken between the times in the request |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_results_latest_get**
> MeasurementResult measurement_results_latest_get()



The client requests that the analyzer return the result of the most recent measurement performed

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
    api_instance = openapi_client.MeasurementChannelApi(api_client)
    
    try:
        api_response = api_instance.measurement_results_latest_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_results_latest_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MeasurementResult**](MeasurementResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analyzer is sending the client the results of the most recent measurement performed |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_script_post**
> measurement_script_post(inline_object)



Start an analyzer measurement script sent as a string.  This is intended for R&D use only and should not be used during normal operation

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
    api_instance = openapi_client.MeasurementChannelApi(api_client)
    inline_object = openapi_client.InlineObject() # InlineObject | 

    try:
        api_instance.measurement_script_post(inline_object)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_script_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer successfully began measurement |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_supported_consumables_get**
> object measurement_supported_consumables_get()



Return a list of all consumable types the analyzer supports. Each consumable returned will include a universally unique identifier, which will be used by the IC when starting a measurement. Any information required to run a consumable will be described in the response using the JSON Schema format (https://json-schema.org/).

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
    api_instance = openapi_client.MeasurementChannelApi(api_client)
    
    try:
        api_response = api_instance.measurement_supported_consumables_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_supported_consumables_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer is responding to the client with a detailed list of all supported consumables. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

