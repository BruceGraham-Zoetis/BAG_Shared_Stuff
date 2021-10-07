

# ResponseMeasurementResult

This object will contain results of the most recent measurement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumableName** | **String** | A descriptive name of the consumable that can be used to uniquely identify it |  [optional]
**startDatetime** | **OffsetDateTime** | The date and time the measurement was started in date-time format |  [optional]
**endDatetime** | **OffsetDateTime** | The date and time the measurement ended in date-time format |  [optional]
**durationSec** | **BigDecimal** | The number of seconds the measurement took from start to end |  [optional]
**result** | [**ResultEnum**](#ResultEnum) | The overall result of the measurement |  [optional]
**testResults** | **Object** | The test results.  Will need to flush this out as we go on as to what this looks like |  [optional]



## Enum: ResultEnum

Name | Value
---- | -----
FAILED | &quot;Failed&quot;
CANCELLED | &quot;Cancelled&quot;
COMPLETED | &quot;Completed&quot;



