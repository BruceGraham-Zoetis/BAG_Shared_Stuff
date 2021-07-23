import analyzerHUBAPI

sChannel = "Config"

def get_config_configuration(s_partial_configuration_information=None):  # noqa: E501
    """get_config_configuration

    The HUB is requesting the analyzer send configuration # noqa: E501

    :param s_partial_configuration_information: The specific part of the analyzer configuration
    :type s_partial_configuration_information: str

    :rtype: object
    """
    return analyzerHUBAPI.callRegisteredMessageHandler({ "sPartialConfigurationInformation": s_partial_configuration_information})

def put_config_configuration(body):  # noqa: E501
    """put_config_configuration

    The HUB is requesting the analyzer set a specific configuration values # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    return analyzerHUBAPI.callRegisteredMessageHandler(body)

def get_config_full_version():  # noqa: E501
    """get_config_full_version

    The HUB is requesting the analyzer send all information about its version # noqa: E501


    :rtype: InlineResponse200
    """
    return analyzerHUBAPI.callRegisteredMessageHandler()

#def get_config_partial_version(s_partial_version_info):  # noqa: E501
def get_config_partial_version(s_partial_version_info):  # noqa: E501
    """get_config_partial_version

    The HUB is requesting the Analyzer send a single part of the its version information # noqa: E501

    :param s_partial_version_info: The specific part of the analyzer version
    :type s_partial_version_info: str

    :rtype: InlineResponse2001
    """

    return analyzerHUBAPI.callRegisteredMessageHandler({ "sPartialVersionInfo": s_partial_version_info})
