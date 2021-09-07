# openapi_client.PromptsChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prompts_notification_ack_post**](PromptsChannelApi.md#prompts_notification_ack_post) | **POST** /prompts/notification_ack | 
[**prompts_option_chosen_post**](PromptsChannelApi.md#prompts_option_chosen_post) | **POST** /prompts/option_chosen | 
[**prompts_qr_scanned_post**](PromptsChannelApi.md#prompts_qr_scanned_post) | **POST** /prompts/qr_scanned | 


# **prompts_notification_ack_post**
> prompts_notification_ack_post(inline_object3)



Hub is informing the analyzer a notification was acknowledged by the operator in response to a websocket message named notification on the prompts channel.

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
    api_instance = openapi_client.PromptsChannelApi(api_client)
    inline_object3 = openapi_client.InlineObject3() # InlineObject3 | 

    try:
        api_instance.prompts_notification_ack_post(inline_object3)
    except ApiException as e:
        print("Exception when calling PromptsChannelApi->prompts_notification_ack_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

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
**200** | Hub received message successfully |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prompts_option_chosen_post**
> prompts_option_chosen_post(inline_object2)



Hub is informing the analyzer of an option that was made by the operator in response to a websocket message named choose_option on the prompts channel.

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
    api_instance = openapi_client.PromptsChannelApi(api_client)
    inline_object2 = openapi_client.InlineObject2() # InlineObject2 | 

    try:
        api_instance.prompts_option_chosen_post(inline_object2)
    except ApiException as e:
        print("Exception when calling PromptsChannelApi->prompts_option_chosen_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

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
**200** | Hub received chosen option successfully |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prompts_qr_scanned_post**
> prompts_qr_scanned_post(inline_object4)



Hub is informing the analyzer of a QR scan attempt in response to a websocket message named scan_qr on the prompts channel.

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
    api_instance = openapi_client.PromptsChannelApi(api_client)
    inline_object4 = openapi_client.InlineObject4() # InlineObject4 | 

    try:
        api_instance.prompts_qr_scanned_post(inline_object4)
    except ApiException as e:
        print("Exception when calling PromptsChannelApi->prompts_qr_scanned_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | 

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
**200** | Hub received message successfully |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

