# StatusChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statusCurrentlyActivatedEventsGet**](StatusChannelApi.md#statusCurrentlyActivatedEventsGet) | **GET** /status/currently_activated_events | 
[**statusOperationalGet**](StatusChannelApi.md#statusOperationalGet) | **GET** /status/operational | 


<a name="statusCurrentlyActivatedEventsGet"></a>
# **statusCurrentlyActivatedEventsGet**
> InlineResponse2003 statusCurrentlyActivatedEventsGet()



The HUB is requesting the analyzer respond with a list of all currently activated events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StatusChannelApi apiInstance = new StatusChannelApi(defaultClient);
    try {
      InlineResponse2003 result = apiInstance.statusCurrentlyActivatedEventsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusChannelApi#statusCurrentlyActivatedEventsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

<a name="statusOperationalGet"></a>
# **statusOperationalGet**
> InlineResponse2002 statusOperationalGet()



The HUB can use send this message to get the status of an analyzer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StatusChannelApi apiInstance = new StatusChannelApi(defaultClient);
    try {
      InlineResponse2002 result = apiInstance.statusOperationalGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusChannelApi#statusOperationalGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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
**200** | Analyzer is responding with its status |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**404** | This response is sent to a request to a server endpoint that is not defined |  -  |
**405** | This response is sent to any request sent to a valid location but with an method that is not supported |  -  |
**500** | This response is sent to any request whose subsequent server response violates the predefined response schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

