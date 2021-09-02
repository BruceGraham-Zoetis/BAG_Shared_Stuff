

# MeasurementResult

This object will contain results of the most recent measurement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumableName** | **String** | A descriptive name of the consumable that can be used to uniquely identify it |  [optional]
**startDateAndTime** | **String** | The local date and time the measurement was started in format MM-DD-YYYY HH:MM:SS |  [optional]
**endDateAndTime** | **String** | The local date and time the measurement ended in format MM-DD-YYYY HH:MM:SS |  [optional]
**durationSec** | **BigDecimal** | The number of seconds the measurement took from start to end |  [optional]
**result** | [**ResultEnum**](#ResultEnum) | The overall result of the measurement |  [optional]
**testResults** | **Object** | The test results.  Will need to flush this out as we go on as to what this looks like |  [optional]



## Enum: ResultEnum

Name | Value
---- | -----
FAILED | &quot;Failed&quot;
CANCELLED | &quot;Cancelled&quot;
COMPLETED | &quot;Completed&quot;



