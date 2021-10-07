# PromptsChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**promptsNotificationAckPost**](PromptsChannelApi.md#promptsNotificationAckPost) | **POST** /prompts/notification_ack | 
[**promptsOptionChosenPost**](PromptsChannelApi.md#promptsOptionChosenPost) | **POST** /prompts/option_chosen | 
[**promptsQrScannedPost**](PromptsChannelApi.md#promptsQrScannedPost) | **POST** /prompts/qr_scanned | 


<a name="promptsNotificationAckPost"></a>
# **promptsNotificationAckPost**
> promptsNotificationAckPost(body)



Hub is informing the analyzer a notification was acknowledged by the operator in response to a websocket message named notification on the prompts channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromptsChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PromptsChannelApi apiInstance = new PromptsChannelApi(defaultClient);
    BodyNotificationAck body = new BodyNotificationAck(); // BodyNotificationAck | 
    try {
      apiInstance.promptsNotificationAckPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromptsChannelApi#promptsNotificationAckPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BodyNotificationAck**](BodyNotificationAck.md)|  |

### Return type

null (empty response body)

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

<a name="promptsOptionChosenPost"></a>
# **promptsOptionChosenPost**
> promptsOptionChosenPost(body)



Hub is informing the analyzer of an option that was made by the operator in response to a websocket message named choose_option on the prompts channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromptsChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PromptsChannelApi apiInstance = new PromptsChannelApi(defaultClient);
    BodyPromptsOptionChosen body = new BodyPromptsOptionChosen(); // BodyPromptsOptionChosen | 
    try {
      apiInstance.promptsOptionChosenPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromptsChannelApi#promptsOptionChosenPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BodyPromptsOptionChosen**](BodyPromptsOptionChosen.md)|  |

### Return type

null (empty response body)

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

<a name="promptsQrScannedPost"></a>
# **promptsQrScannedPost**
> promptsQrScannedPost(body)



Hub is informing the analyzer of a QR scan attempt in response to a websocket message named scan_qr on the prompts channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromptsChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PromptsChannelApi apiInstance = new PromptsChannelApi(defaultClient);
    BodyPromptsQrScanned body = new BodyPromptsQrScanned(); // BodyPromptsQrScanned | 
    try {
      apiInstance.promptsQrScannedPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromptsChannelApi#promptsQrScannedPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BodyPromptsQrScanned**](BodyPromptsQrScanned.md)|  |

### Return type

null (empty response body)

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

