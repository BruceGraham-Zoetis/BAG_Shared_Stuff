import analyzerHUBAPI

def put_power_off(**requestArgs):  # noqa: E501
    """put_power_off

    Go from a state of powered to no power. This behavior of this action will depend on what a particular analyzer supports. If it doesn't support power off, go to deep sleep mode # noqa: E501


    :rtype: None
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)


def put_power_on(**requestArgs):  # noqa: E501
    """put_power_on

    Go from a state of no power to powered. The Dx Modules don&#x27;t support wake on LAN, so this will mean return from low power mode # noqa: E501


    :rtype: None
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)


def put_power_reboot(**requestArgs):  # noqa: E501
    """put_power_reboot

    Request sent from the HUB to reboot the analyzer (power off and power back on), leaving all settings and data intact # noqa: E501


    :rtype: None
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)
