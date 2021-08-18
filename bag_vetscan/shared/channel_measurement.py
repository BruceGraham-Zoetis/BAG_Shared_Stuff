from requests.api import request
import analyzerHUBAPI

def delete_measurement_cancel(**requestArgs):  # noqa: E501
    """delete_measurement_cancel

    The HUB is requesting the analyzer cancel the measurement that is currently being performed # noqa: E501


    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)


def get_measurement_past_results(start_time, start_date, end_time, end_date, **requestArgs):  # noqa: E501
    """get_measurement_past_results

    The HUB is requesting the analyzer send past results between two times # noqa: E501

    :param start_time: The time to start looking for results to return
    :type start_time: str
    :param start_date: The date to start looking for results to return
    :type start_date: str
    :param end_time: The time to stop looking for results to return
    :type end_time: str
    :param end_date: The date to stop looking for results to return
    :type end_date: str

    :rtype: InlineResponse2004
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(
        queryArgs = {
            "start_time": start_time,
            "start_date": start_date,
            "end_time": end_time,
            "end_date": end_date
        },
        **requestArgs
        )


def get_measurement_result(**requestArgs):  # noqa: E501
    """get_measurement_result

    The HUB requests that the analyzer return the result of the most recent measurement performed # noqa: E501


    :rtype: measurement_result
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)


def get_measurement_status(**requestArgs):  # noqa: E501
    """get_measurement_status

    The HUB is requesting the analyzer return the status of the current measurement being performed # noqa: E501


    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)


def get_measurement_supported_consumables(**requestArgs):  # noqa: E501
    """get_measurement_supported_consumables

    Return a list of all consumable types the analyzer supports. Each consumable returned will include a universally unique identifier, which will be used by the IC when starting a measurement. Any information required to run a consumable will be described in the response using the JSON Schema format (https://json-schema.org/). # noqa: E501


    :rtype: InlineResponse2002
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(**requestArgs)


def post_measurement_by_file(body, **requestArgs):  # noqa: E501
    """post_measurement_by_file

    Start an analyzer measurement script as described in a file stored on the analyzer.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(bodyJSON = body, **requestArgs)


def post_measurement_by_script(body, **requestArgs):  # noqa: E501
    """post_measurement_by_script

    Start an analyzer measurement script sent as a string.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(bodyJSON = body, **requestArgs)


def post_measurement_normal(body, **requestArgs):  # noqa: E501
    """post_measurement_normal

    Start an analyzer measurement # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.handleAPIRequestInOrOut(bodyJSON = body, **requestArgs)
