

# ResponseBadRequest500


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
NUMBER_500 | new BigDecimal(&quot;500&quot;)



## Enum: TitleEnum

Name | Value
---- | -----
RESPONSE_BODY_DOES_NOT_CONFORM_TO_SPECIFICATION | &quot;Response body does not conform to specification&quot;



