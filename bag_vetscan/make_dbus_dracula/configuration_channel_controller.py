#!/usr/bin/env python3

"""
File: configuration_channel_controller.py

Purpose: DBus service interface for the dracula analyzer app.
"""

def configuration_factory_reset_put(self):
    """configuration_factory_reset_put

    Restore the analyzer to the state it was in when it left the factory. All settings and data are removed. # noqa: E501


    :rtype: None
    """
    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn



def configuration_get(self):
    """configuration_get

    Request the configuration from the analyzer # noqa: E501


    :rtype: object
    """
    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn


def configuration_put(self, str_request_body : str):
    """configuration_put

    Set the configuration of the analyzer # noqa: E501

    :param body: 
    :type body: 

    :rtype: None
    """
    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn


def configuration_schema_get(self):
    """configuration_schema_get

    Request the configuration schema from the analyzer # noqa: E501


    :rtype: object
    """
    dict_rtn = {
        "status": "done"
    }
    #TODO
    return dict_rtn


