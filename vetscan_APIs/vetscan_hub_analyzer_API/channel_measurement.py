import analyzerHUBAPI

sChannel = "Measurement"

def delete_measurement_cancel():  # noqa: E501
    """delete_measurement_cancel

    The HUB is requesting the analyzer cancel the measurement that is currently being performed # noqa: E501


    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.callRegisteredMessageHandler()


def get_measurement_past_results(s_start_time, s_start_date, s_end_time, s_end_date):  # noqa: E501
    """get_measurement_past_results

    The HUB is requesting the analyzer send past results between two times # noqa: E501

    :param s_start_time: The time to start looking for results to return
    :type s_start_time: str
    :param s_start_date: The date to start looking for results to return
    :type s_start_date: str
    :param s_end_time: The time to stop looking for results to return
    :type s_end_time: str
    :param s_end_date: The date to stop looking for results to return
    :type s_end_date: str

    :rtype: InlineResponse2004
    """
    return analyzerHUBAPI.callRegisteredMessageHandler(
        {
            "sStartTime": s_start_time,
            "sStartDate": s_start_date,
            "sEndTime": s_end_time,
            "sEndDate": s_end_date
        }
        )


def get_measurement_result():  # noqa: E501
    """get_measurement_result

    The HUB requests that the analyzer return the result of the most recent measurement performed # noqa: E501


    :rtype: OMeasurementResult
    """
    return analyzerHUBAPI.callRegisteredMessageHandler()


def get_measurement_status():  # noqa: E501
    """get_measurement_status

    The HUB is requesting the analyzer return the status of the current measurement being performed # noqa: E501


    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.callRegisteredMessageHandler()


def get_measurement_supported_consumables():  # noqa: E501
    """get_measurement_supported_consumables

    Return a list of all consumable types the analyzer supports. Each consumable returned will include a universally unique identifier, which will be used by the IC when starting a measurement. Any information required to run a consumable will be described in the response using the JSON Schema format (https://json-schema.org/). # noqa: E501


    :rtype: InlineResponse2002
    """
    return analyzerHUBAPI.callRegisteredMessageHandler()


def post_measurement_by_file(body):  # noqa: E501
    """post_measurement_by_file

    Start an analyzer measurement script as described in a file stored on the analyzer.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.callRegisteredMessageHandler(body)


def post_measurement_by_script(body):  # noqa: E501
    """post_measurement_by_script

    Start an analyzer measurement script sent as a string.  This is intended for R&amp;D use only and should not be used during normal operation # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.callRegisteredMessageHandler(body)


def post_measurement_normal(body):  # noqa: E501
    """post_measurement_normal

    Start an analyzer measurement # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    return analyzerHUBAPI.callRegisteredMessageHandler(body)
