

# ResponseBadRequest400


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
NUMBER_400 | new BigDecimal(&quot;400&quot;)



## Enum: TitleEnum

Name | Value
---- | -----
BAD_REQUEST | &quot;Bad Request&quot;



