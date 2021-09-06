#!/usr/bin/env python3
# coding: utf-8

"""
File: class_analyzer_openapi.py
"""

import os, sys
import requests
import inspect   # call stack stuff, for getting function's name

strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
sys.path.append(strThisFilePath + "/../hub_app")

import openapi_client
from openapi_client.rest import ApiException
from openapi_client.models.inline_object1 import InlineObject1

"""
Purpose: keep info about a connected analyzer
"""
class analyzer_client():
    # init method or constructor 
    def __init__(self, str_ip_address : str, str_client_name : str):
        # Defining the host is optional and defaults to http://localhost
        # See configuration.py for a list of all supported configuration parameters.
        self.configuration = openapi_client.Configuration(host = "http://localhost:8080")

        # Enter a context with an instance of the API client
        with openapi_client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            self.configuration_api          = openapi_client.ConfigurationApi(api_client)
            self.control_channel_api        = openapi_client.ControlChannelApi(api_client)
            self.measurement_channel_api    = openapi_client.MeasurementChannelApi(api_client)
            self.status_channel_api         = openapi_client.StatusChannelApi(api_client)

        self.__str_ip_address = str_ip_address
        self.__str_client_name = str_client_name
        self.__trace = True

    def get_ip_address(self) -> str:
        return self.__str_ip_address

    def get_name(self) -> str:
        return self.__str_client_name

    ################################################
    # Make asynchronous HTTP requests.
    # See async_req=True
    ################################################


    ################################################
    # Class: ConfigurationApi
    ################################################
    """
    configuration_factory_reset_put
    configuration_get
    configuration_put
    configuration_schema_get
    """
    ################################################
    # Class: ControlChannelApi
    ################################################

    def control_light_blink_put(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.control_channel_api.control_light_blink_put(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def control_light_off_put(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.control_channel_api.control_light_off_put(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def control_power_off_put(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.control_channel_api.control_power_off_put(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def control_power_reboot_put(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.control_channel_api.control_power_reboot_put(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    ################################################
    # File: measurement_channel_api
    ################################################

    def channel_measurement_get_measurement_status(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.measurement_channel_api.channel_measurement_get_measurement_status(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_cancel_delete(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            """
            TODO - This fails: 
                raise ValueError("Invalid value for `measurement_id`, must not be `None`")  # noqa: E501
            thread = self.measurement_channel_api.measurement_cancel_delete(async_req=True)
            str_response = thread.get()
            """
            str_response = "--- this failed"
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_consumable_consumable_uuid_post(self, consumable_uuid : str) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            """
            TODO - This fails: 
                raise ValueError("Invalid value for `measurement_id`, must not be `None`")  # noqa: E501
            thread = self.measurement_channel_api.measurement_cancel_delete(async_req=True)
            str_response = thread.get()
            thread = self.measurement_channel_api.measurement_consumable_consumable_uuid_post(consumable_uuid, async_req=True)
            str_response = thread.get()
            """
            str_response = "--- this failed"
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_file_post(self, inline_object1 : str) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.measurement_channel_api.measurement_file_post(inline_object1, async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_past_results_get(self, start_time : str, start_date : str, end_time : str, end_date : str) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.measurement_channel_api.measurement_past_results_get(start_time, start_date, end_time, end_date, async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_result_get(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.measurement_channel_api.measurement_result_get(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_script_post(self, inline_object1 : str) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.measurement_channel_api.measurement_script_post(inline_object1, async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_supported_consumables_get(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            """
            str_response = self.measurement_channel_api.measurement_supported_consumables_get()
            """
            thread = self.measurement_channel_api.measurement_supported_consumables_get(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""


    ################################################
    # Class: StatusChannelApi
    ################################################
    """
    status_currently_activated_events_get
    status_operational_get
    """


if __name__ == '__main__':
    print("")

    str_ip_address = "127.0.0.1"
    str_client_name = "dracula"

    oAna = analyzer_client(str_ip_address, str_client_name)

    ################################################
    # Class: ConfigurationApi
    ################################################
    """
    configuration_factory_reset_put
    configuration_get
    configuration_put
    configuration_schema_get
    """
    ################################################
    # Class: ControlChannelApi
    ################################################
    oAna.control_light_blink_put()
    oAna.control_power_off_put()
    oAna.control_power_reboot_put()

    ################################################
    # File: measurement_channel_api
    ################################################
    oAna.channel_measurement_get_measurement_status()
    oAna.measurement_cancel_delete()
    oAna.measurement_consumable_consumable_uuid_post("consumable_uuid")

    inline_object1 = InlineObject1(filename="dummy", local_vars_configuration=None)
    oAna.measurement_file_post(inline_object1)
    oAna.measurement_past_results_get("start_time", "start_date", "end_time", "end_date")
    oAna.measurement_result_get()
    oAna.measurement_script_post(inline_object1)
    oAna.measurement_supported_consumables_get()

    ################################################
    # Class: StatusChannelApi
    ################################################
    """
    status_currently_activated_events_get
    status_operational_get
    """
