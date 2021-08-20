import analyzerHUBAPI

def get_config_configuration(partial_configuration_information=None, **requestArgs):  # noqa: E501
    """get_config_configuration

    The HUB is requesting the analyzer send configuration # noqa: E501

    :param partial_configuration_information: The specific part of the analyzer configuration
    :type partial_configuration_information: str

    :rtype: object
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(queryArgs={ "partial_configuration_information": partial_configuration_information}, **requestArgs)

def put_config_configuration(body, **requestArgs):  # noqa: E501
    """put_config_configuration

    The HUB is requesting the analyzer set a specific configuration values # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(bodyJSON=body, **requestArgs)

def get_config_full_version(**requestArgs):  # noqa: E501
    """get_config_full_version

    The HUB is requesting the analyzer send all information about its version # noqa: E501


    :rtype: InlineResponse200
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)

def get_config_partial_version(partial_version_info, **requestArgs):  # noqa: E501
    """get_config_partial_version

    The HUB is requesting the Analyzer send a single part of the its version information # noqa: E501

    :param partial_version_info: The specific part of the analyzer version
    :type partial_version_info: str

    :rtype: InlineResponse2001
    """

    return analyzerHUBAPI.handleAPIRequestInOrOut(queryArgs={ "partial_version_info": partial_version_info}, **requestArgs)
