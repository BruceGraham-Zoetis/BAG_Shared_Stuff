

# EventInfo

This object will contain information about an event that occurred

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationTime** | **String** | The local date and time the event was activated in format MM-DD-YYYY HH:MM:SS |  [optional]
**severity** | [**SeverityEnum**](#SeverityEnum) | A string value indicating the severity of the event |  [optional]
**eventName** | **String** | The name of the event |  [optional]
**eventAdditionalInformation** | **String** | Additional information to describe the event that has occurred.  This can be anything that will help the operator understand in more detail the event |  [optional]



## Enum: SeverityEnum

Name | Value
---- | -----
NOTIFICATION | &quot;Notification&quot;
WARNING | &quot;Warning&quot;
ERROR | &quot;Error&quot;
HALT | &quot;Halt&quot;



