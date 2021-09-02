# MeasurementChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channelMeasurementGetMeasurementStatus**](MeasurementChannelApi.md#channelMeasurementGetMeasurementStatus) | **GET** /measurement/status | 
[**measurementCancelDelete**](MeasurementChannelApi.md#measurementCancelDelete) | **DELETE** /measurement/cancel | 
[**measurementConsumableConsumableUuidPost**](MeasurementChannelApi.md#measurementConsumableConsumableUuidPost) | **POST** /measurement/consumable/{consumable_uuid} | 
[**measurementFilePost**](MeasurementChannelApi.md#measurementFilePost) | **POST** /measurement/file | 
[**measurementPastResultsGet**](MeasurementChannelApi.md#measurementPastResultsGet) | **GET** /measurement/past_results | 
[**measurementResultGet**](MeasurementChannelApi.md#measurementResultGet) | **GET** /measurement/result | 
[**measurementScriptPost**](MeasurementChannelApi.md#measurementScriptPost) | **POST** /measurement/script | 
[**measurementSupportedConsumablesGet**](MeasurementChannelApi.md#measurementSupportedConsumablesGet) | **GET** /measurement/supported_consumables | 


<a name="channelMeasurementGetMeasurementStatus"></a>
# **channelMeasurementGetMeasurementStatus**
> InlineResponse200 channelMeasurementGetMeasurementStatus()



The HUB is requesting the analyzer return the status of the current measurement being performed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MeasurementChannelApi apiInstance = new MeasurementChannelApi(defaultClient);
    try {
      InlineResponse200 result = apiInstance.channelMeasurementGetMeasurementStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#channelMeasurementGetMeasurementStatus");
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

<a name="measurementCancelDelete"></a>
# **measurementCancelDelete**
> InlineResponse200 measurementCancelDelete()



The HUB is requesting the analyzer cancel the measurement that is currently being performed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MeasurementChannelApi apiInstance = new MeasurementChannelApi(defaultClient);
    try {
      InlineResponse200 result = apiInstance.measurementCancelDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementCancelDelete");
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

<a name="measurementConsumableConsumableUuidPost"></a>
# **measurementConsumableConsumableUuidPost**
> InlineResponse200 measurementConsumableConsumableUuidPost(consumableUuid)



Start an analyzer measurement with a specific consumable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MeasurementChannelApi apiInstance = new MeasurementChannelApi(defaultClient);
    UUID consumableUuid = new UUID(); // UUID | The UUID of the consumable
    try {
      InlineResponse200 result = apiInstance.measurementConsumableConsumableUuidPost(consumableUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementConsumableConsumableUuidPost");
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
 **consumableUuid** | **UUID**| The UUID of the consumable |

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

<a name="measurementFilePost"></a>
# **measurementFilePost**
> InlineResponse200 measurementFilePost(inlineObject1)



Start an analyzer measurement script as described in a file stored on the analyzer.  This is intended for R&amp;D use only and should not be used during normal operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MeasurementChannelApi apiInstance = new MeasurementChannelApi(defaultClient);
    InlineObject1 inlineObject1 = new InlineObject1(); // InlineObject1 | 
    try {
      InlineResponse200 result = apiInstance.measurementFilePost(inlineObject1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementFilePost");
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
 **inlineObject1** | [**InlineObject1**](InlineObject1.md)|  |

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

<a name="measurementPastResultsGet"></a>
# **measurementPastResultsGet**
> InlineResponse2001 measurementPastResultsGet(startTime, startDate, endTime, endDate)



The HUB is requesting the analyzer send past results between two times

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MeasurementChannelApi apiInstance = new MeasurementChannelApi(defaultClient);
    String startTime = "23:13:01"; // String | The time to start looking for results to return
    String startDate = "2021-05-13"; // String | The date to start looking for results to return
    String endTime = "06:05:23"; // String | The time to stop looking for results to return
    String endDate = "2021-05-15"; // String | The date to stop looking for results to return
    try {
      InlineResponse2001 result = apiInstance.measurementPastResultsGet(startTime, startDate, endTime, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementPastResultsGet");
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
 **startTime** | **String**| The time to start looking for results to return |
 **startDate** | **String**| The date to start looking for results to return |
 **endTime** | **String**| The time to stop looking for results to return |
 **endDate** | **String**| The date to stop looking for results to return |

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

<a name="measurementResultGet"></a>
# **measurementResultGet**
> MeasurementResult measurementResultGet()



The HUB requests that the analyzer return the result of the most recent measurement performed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MeasurementChannelApi apiInstance = new MeasurementChannelApi(defaultClient);
    try {
      MeasurementResult result = apiInstance.measurementResultGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementResultGet");
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

<a name="measurementScriptPost"></a>
# **measurementScriptPost**
> InlineResponse200 measurementScriptPost(inlineObject)



Start an analyzer measurement script sent as a string.  This is intended for R&amp;D use only and should not be used during normal operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MeasurementChannelApi apiInstance = new MeasurementChannelApi(defaultClient);
    InlineObject inlineObject = new InlineObject(); // InlineObject | 
    try {
      InlineResponse200 result = apiInstance.measurementScriptPost(inlineObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementScriptPost");
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
 **inlineObject** | [**InlineObject**](InlineObject.md)|  |

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

<a name="measurementSupportedConsumablesGet"></a>
# **measurementSupportedConsumablesGet**
> Object measurementSupportedConsumablesGet()



Return a list of all consumable types the analyzer supports. Each consumable returned will include a universally unique identifier, which will be used by the IC when starting a measurement. Any information required to run a consumable will be described in the response using the JSON Schema format (https://json-schema.org/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeasurementChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    MeasurementChannelApi apiInstance = new MeasurementChannelApi(defaultClient);
    try {
      Object result = apiInstance.measurementSupportedConsumablesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementSupportedConsumablesGet");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer is responding to the client with a detailed list of all supported consumables. |  -  |

