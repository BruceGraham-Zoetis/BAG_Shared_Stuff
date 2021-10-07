# MeasurementChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**measurementCancelPost**](MeasurementChannelApi.md#measurementCancelPost) | **POST** /measurement/cancel | 
[**measurementConsumableConsumableUuidPost**](MeasurementChannelApi.md#measurementConsumableConsumableUuidPost) | **POST** /measurement/consumable/{consumable_uuid} | 
[**measurementFilePost**](MeasurementChannelApi.md#measurementFilePost) | **POST** /measurement/file | 
[**measurementResultsGet**](MeasurementChannelApi.md#measurementResultsGet) | **GET** /measurement/results | 
[**measurementResultsLatestGet**](MeasurementChannelApi.md#measurementResultsLatestGet) | **GET** /measurement/results/latest | 
[**measurementScriptPost**](MeasurementChannelApi.md#measurementScriptPost) | **POST** /measurement/script | 
[**measurementSupportedConsumablesGet**](MeasurementChannelApi.md#measurementSupportedConsumablesGet) | **GET** /measurement/supported_consumables | 


<a name="measurementCancelPost"></a>
# **measurementCancelPost**
> measurementCancelPost()



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
      apiInstance.measurementCancelPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementCancelPost");
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
**200** | Analyzer successfully began cancelling the measurement |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

<a name="measurementConsumableConsumableUuidPost"></a>
# **measurementConsumableConsumableUuidPost**
> measurementConsumableConsumableUuidPost(consumableUuid)



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
      apiInstance.measurementConsumableConsumableUuidPost(consumableUuid);
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

null (empty response body)

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

<a name="measurementFilePost"></a>
# **measurementFilePost**
> measurementFilePost(body)



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
    BodyFileJson body = new BodyFileJson(); // BodyFileJson | 
    try {
      apiInstance.measurementFilePost(body);
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
 **body** | [**BodyFileJson**](BodyFileJson.md)|  |

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
**200** | Analyzer successfully began measurement |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

<a name="measurementResultsGet"></a>
# **measurementResultsGet**
> ResponseMeasurementResults measurementResultsGet(startDatetime, endDatetime)



The client is requesting the analyzer to send past results between two times

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
    OffsetDateTime startDatetime = OffsetDateTime.now(); // OffsetDateTime | The earliest result. If missing, the analyzer must return the results from as early as possible
    OffsetDateTime endDatetime = OffsetDateTime.now(); // OffsetDateTime | The latest time for a result. If missing, the analyzer must return all results from 'from' untill present time.
    try {
      ResponseMeasurementResults result = apiInstance.measurementResultsGet(startDatetime, endDatetime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementResultsGet");
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
 **startDatetime** | **OffsetDateTime**| The earliest result. If missing, the analyzer must return the results from as early as possible | [optional]
 **endDatetime** | **OffsetDateTime**| The latest time for a result. If missing, the analyzer must return all results from &#39;from&#39; untill present time. | [optional]

### Return type

[**ResponseMeasurementResults**](ResponseMeasurementResults.md)

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

<a name="measurementResultsLatestGet"></a>
# **measurementResultsLatestGet**
> ResponseMeasurementResult measurementResultsLatestGet()



The client requests that the analyzer return the result of the most recent measurement performed

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
      ResponseMeasurementResult result = apiInstance.measurementResultsLatestGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeasurementChannelApi#measurementResultsLatestGet");
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

[**ResponseMeasurementResult**](ResponseMeasurementResult.md)

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

<a name="measurementScriptPost"></a>
# **measurementScriptPost**
> measurementScriptPost(body)



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
    BodyScriptJson body = new BodyScriptJson(); // BodyScriptJson | 
    try {
      apiInstance.measurementScriptPost(body);
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
 **body** | [**BodyScriptJson**](BodyScriptJson.md)|  |

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
**200** | Analyzer successfully began measurement |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |
**503** | This response is sent to any request that the analyzer is unable to do at the time |  -  |

<a name="measurementSupportedConsumablesGet"></a>
# **measurementSupportedConsumablesGet**
> ResponseSupportedConsumables measurementSupportedConsumablesGet()



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
      ResponseSupportedConsumables result = apiInstance.measurementSupportedConsumablesGet();
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

[**ResponseSupportedConsumables**](ResponseSupportedConsumables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analyzer is responding to the client with a detailed list of all supported consumables. |  -  |

