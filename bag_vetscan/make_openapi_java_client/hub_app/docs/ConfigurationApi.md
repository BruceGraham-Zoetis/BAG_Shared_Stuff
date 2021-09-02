# ConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurationFactoryResetPut**](ConfigurationApi.md#configurationFactoryResetPut) | **PUT** /configuration/factory_reset | 
[**configurationGet**](ConfigurationApi.md#configurationGet) | **GET** /configuration | 
[**configurationPut**](ConfigurationApi.md#configurationPut) | **PUT** /configuration | 
[**configurationSchemaGet**](ConfigurationApi.md#configurationSchemaGet) | **GET** /configuration/schema | 


<a name="configurationFactoryResetPut"></a>
# **configurationFactoryResetPut**
> configurationFactoryResetPut()



Restore the analyzer to the state it was in when it left the factory. All settings and data are removed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    try {
      apiInstance.configurationFactoryResetPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationFactoryResetPut");
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
**200** | Analyzer successfully began a factory reset |  -  |

<a name="configurationGet"></a>
# **configurationGet**
> Object configurationGet()



Request the configuration from the analyzer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    try {
      Object result = apiInstance.configurationGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationGet");
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
**200** | Analyzer responds with the its configuration information |  -  |

<a name="configurationPut"></a>
# **configurationPut**
> configurationPut(body)



Set the configuration of the analyzer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    Object body = null; // Object | 
    try {
      apiInstance.configurationPut(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationPut");
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
 **body** | **Object**|  |

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
**200** | Analyzer successfully made configuration changes requested by the client |  -  |
**400** | This response is sent to a request that violates the predefined request schema |  -  |

<a name="configurationSchemaGet"></a>
# **configurationSchemaGet**
> Object configurationSchemaGet()



Request the configuration schema from the analyzer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    try {
      Object result = apiInstance.configurationSchemaGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationSchemaGet");
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
**200** | Analyzer responds with the configuration schema that is used to validate the configuration |  -  |
**501** | The analyzer does not provide a schema for the configuration |  -  |

