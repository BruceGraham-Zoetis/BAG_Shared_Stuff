import analyzerHUBAPI

sChannel = "RemoteControl"

def put_remote_control_light_blink():  # noqa: E501
    """put_remote_control_light_blink

    Cause an analyzer to blink its light ring.  The purpose of this is to identify an analyzer. If you have multiple analyzers of the same kind it is nice to have a way to get a visual que which is which instead of having to read the serial number of each analyzer to identify it. # noqa: E501


    :rtype: None
    """
    return analyzerHUBAPI.callRegisteredMessageHandler()

def put_remote_control_light_off():  # noqa: E501
    """channel_remote_control_put_remote_control_light_off

    Cause an analyzer to turn off its light ring. # noqa: E501


    :rtype: None
    """
    return analyzerHUBAPI.callRegisteredMessageHandler()
