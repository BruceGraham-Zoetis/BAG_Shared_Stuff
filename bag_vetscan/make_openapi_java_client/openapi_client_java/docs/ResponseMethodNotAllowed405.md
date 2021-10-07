

# ResponseMethodNotAllowed405


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **String** | A description of the problem with the request | 
**status** | [**StatusEnum**](#StatusEnum) | The number of the HTTP error code | 
**title** | [**TitleEnum**](#TitleEnum) | The title of the error indicated by the status | 
**type** | **String** | Additional error information if available describing the type of error | 



## Enum: StatusEnum

Name | Value
---- | -----
NUMBER_405 | new BigDecimal(&quot;405&quot;)



## Enum: TitleEnum

Name | Value
---- | -----
METHOD_NOT_ALLOWED | &quot;Method Not Allowed&quot;



