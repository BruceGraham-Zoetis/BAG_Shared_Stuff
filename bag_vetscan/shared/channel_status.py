import analyzerHUBAPI

def get_status_currently_activated_events(**requestArgs):  # noqa: E501
    """get_status_currently_activated_events

    The HUB is requesting the analyzer respond with a list of all currently activated events # noqa: E501


    :rtype: InlineResponse2006
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)


def get_status_operational(**requestArgs):  # noqa: E501
    """get_status_operational

    The HUB can use send this message to get the status of an analyzer # noqa: E501


    :rtype: InlineResponse2005
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)
