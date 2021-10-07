# StatusChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statusGet**](StatusChannelApi.md#statusGet) | **GET** /status | 


<a name="statusGet"></a>
# **statusGet**
> ResponseStatusOperational200 statusGet()



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
      ResponseStatusOperational200 result = apiInstance.statusGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusChannelApi#statusGet");
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

[**ResponseStatusOperational200**](ResponseStatusOperational200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer is responding with its status |  -  |

