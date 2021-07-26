import analyzerHUBAPI

sChannel = "Maintenance"

def put_maintenance_factory_reset():  # noqa: E501
    """put_maintenance_factory_reset

    Restore the analyzer to the state it was in when it left the factory. All settings and data are removed. # noqa: E501


    :rtype: None
    """
    return analyzerHUBAPI.callRegisteredMessageHandler()
