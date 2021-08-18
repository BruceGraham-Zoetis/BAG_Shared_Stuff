# openapi_client.MeasurementChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_measurement_get_measurement_status**](MeasurementChannelApi.md#channel_measurement_get_measurement_status) | **GET** /measurement/status | 
[**measurement_cancel_delete**](MeasurementChannelApi.md#measurement_cancel_delete) | **DELETE** /measurement/cancel | 
[**measurement_consumable_consumable_uuid_post**](MeasurementChannelApi.md#measurement_consumable_consumable_uuid_post) | **POST** /measurement/consumable/{consumable_uuid} | 
[**measurement_file_post**](MeasurementChannelApi.md#measurement_file_post) | **POST** /measurement/file | 
[**measurement_past_results_get**](MeasurementChannelApi.md#measurement_past_results_get) | **GET** /measurement/past_results | 
[**measurement_result_get**](MeasurementChannelApi.md#measurement_result_get) | **GET** /measurement/result | 
[**measurement_script_post**](MeasurementChannelApi.md#measurement_script_post) | **POST** /measurement/script | 
[**measurement_supported_consumables_get**](MeasurementChannelApi.md#measurement_supported_consumables_get) | **GET** /measurement/supported_consumables | 


# **channel_measurement_get_measurement_status**
> InlineResponse200 channel_measurement_get_measurement_status()



The HUB is requesting the analyzer return the status of the current measurement being performed

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
        api_response = api_instance.channel_measurement_get_measurement_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->channel_measurement_get_measurement_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | This response is sent to notify the HUB of the status of a measurement that was requested to start, cancel, or whose status is being queried |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_cancel_delete**
> InlineResponse200 measurement_cancel_delete()



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
        api_response = api_instance.measurement_cancel_delete()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_cancel_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | This response is sent to notify the HUB of the status of a measurement that was requested to start, cancel, or whose status is being queried |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_consumable_consumable_uuid_post**
> InlineResponse200 measurement_consumable_consumable_uuid_post(consumable_uuid)



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
        api_response = api_instance.measurement_consumable_consumable_uuid_post(consumable_uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_consumable_consumable_uuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumable_uuid** | **str**| The UUID of the consumable | 

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
**200** | This response is sent to notify the HUB of the status of a measurement that was requested to start, cancel, or whose status is being queried |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_file_post**
> InlineResponse200 measurement_file_post(inline_object1)



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
        api_response = api_instance.measurement_file_post(inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response is sent to notify the HUB of the status of a measurement that was requested to start, cancel, or whose status is being queried |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_past_results_get**
> InlineResponse2001 measurement_past_results_get(start_time, start_date, end_time, end_date)



The HUB is requesting the analyzer send past results between two times

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
    start_time = '23:13:01' # str | The time to start looking for results to return
start_date = '2021-05-13' # str | The date to start looking for results to return
end_time = '06:05:23' # str | The time to stop looking for results to return
end_date = '2021-05-15' # str | The date to stop looking for results to return

    try:
        api_response = api_instance.measurement_past_results_get(start_time, start_date, end_time, end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_past_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| The time to start looking for results to return | 
 **start_date** | **str**| The date to start looking for results to return | 
 **end_time** | **str**| The time to stop looking for results to return | 
 **end_date** | **str**| The date to stop looking for results to return | 

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
**200** | Analyzer is responding with the results of all measurements taken between the times in the request |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_result_get**
> MeasurementResult measurement_result_get()



The HUB requests that the analyzer return the result of the most recent measurement performed

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
        api_response = api_instance.measurement_result_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_result_get: %s\n" % e)
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
**200** | The analyzer is sending the HUB the results of the most recent measurement performed |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_script_post**
> InlineResponse200 measurement_script_post(inline_object)



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
        api_response = api_instance.measurement_script_post(inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MeasurementChannelApi->measurement_script_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response is sent to notify the HUB of the status of a measurement that was requested to start, cancel, or whose status is being queried |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
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

