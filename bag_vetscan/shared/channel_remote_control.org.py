import analyzerHUBAPI

def put_remote_control_light_blink(**requestArgs):  # noqa: E501
    """put_remote_control_light_blink

    Cause an analyzer to blink its light ring.  The purpose of this is to identify an analyzer. If you have multiple analyzers of the same kind it is nice to have a way to get a visual que which is which instead of having to read the serial number of each analyzer to identify it. # noqa: E501


    :rtype: None
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)
