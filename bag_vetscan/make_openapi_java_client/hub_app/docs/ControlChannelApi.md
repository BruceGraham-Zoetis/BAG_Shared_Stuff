# ControlChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controlLightBlinkPut**](ControlChannelApi.md#controlLightBlinkPut) | **PUT** /control/light/blink | 
[**controlLightOffPut**](ControlChannelApi.md#controlLightOffPut) | **PUT** /control/light/off | 
[**controlPowerOffPut**](ControlChannelApi.md#controlPowerOffPut) | **PUT** /control/power/off | 
[**controlPowerRebootPut**](ControlChannelApi.md#controlPowerRebootPut) | **PUT** /control/power/reboot | 


<a name="controlLightBlinkPut"></a>
# **controlLightBlinkPut**
> controlLightBlinkPut()



Cause an analyzer to blink its light ring.  The purpose of this is to identify an analyzer. If you have multiple analyzers of the same kind it is nice to have a way to get a visual que which is which instead of having to read the serial number of each analyzer to identify it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControlChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ControlChannelApi apiInstance = new ControlChannelApi(defaultClient);
    try {
      apiInstance.controlLightBlinkPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling ControlChannelApi#controlLightBlinkPut");
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

null (empty response body)

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

<a name="controlLightOffPut"></a>
# **controlLightOffPut**
> controlLightOffPut()



Cause an analyzer to turn off its light ring.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControlChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ControlChannelApi apiInstance = new ControlChannelApi(defaultClient);
    try {
      apiInstance.controlLightOffPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling ControlChannelApi#controlLightOffPut");
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

null (empty response body)

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

<a name="controlPowerOffPut"></a>
# **controlPowerOffPut**
> controlPowerOffPut()



Go from a state of powered to no power. This behavior of this action will depend on what a particular analyzer supports. If it doesn&#39;t support power off, go to &#39;deep sleep&#39; mode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControlChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ControlChannelApi apiInstance = new ControlChannelApi(defaultClient);
    try {
      apiInstance.controlPowerOffPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling ControlChannelApi#controlPowerOffPut");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer successfully began to power off or go to sleep |  -  |

<a name="controlPowerRebootPut"></a>
# **controlPowerRebootPut**
> controlPowerRebootPut()



Request sent from a client to reboot the analyzer (power off and power back on), leaving all settings and data intact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControlChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ControlChannelApi apiInstance = new ControlChannelApi(defaultClient);
    try {
      apiInstance.controlPowerRebootPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling ControlChannelApi#controlPowerRebootPut");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer successfully initiated a reboot |  -  |

