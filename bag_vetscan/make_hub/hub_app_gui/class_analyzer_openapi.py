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
            self.api_instance = openapi_client.MeasurementChannelApi(api_client)

        self.__str_ip_address = str_ip_address
        self.__str_client_name = str_client_name

    def get_ip_address(self) -> str:
        return self.__str_ip_address

    def get_name(self) -> str:
        return self.__str_client_name

    ################################################
    # Make asynchronous HTTP requests.
    # See async_req=True
    ################################################


    ################################################
    # File: measurement_channel_api
    ################################################

    def channel_measurement_get_measurement_status(self) -> str:
        try:
            api_response = self.api_instance.channel_measurement_get_measurement_status(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_cancel_delete(self) -> str:
        try:
            api_response = self.api_instance.measurement_cancel_delete(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_consumable_consumable_uuid_post(self) -> str:
        try:
            api_response = self.api_instance.measurement_consumable_consumable_uuid_post(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_file_post(self) -> str:
        try:
            api_response = self.api_instance.measurement_file_post(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_past_results_get(self) -> str:
        try:
            api_response = self.api_instance.measurement_past_results_get(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_result_get(self) -> str:
        try:
            api_response = self.api_instance.measurement_result_get(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_script_post(self) -> str:
        try:
            api_response = self.api_instance.measurement_script_post(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_supported_consumables_get(self) -> str:
        try:
            api_response = self.api_instance.measurement_supported_consumables_get(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""


    ################################################
    # File: control_channel_api
    ################################################

    def control_light_blink_put(self) -> str:
        try:
            api_response = self.api_instance.control_light_blink_put(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def control_power_off_put(self) -> str:
        try:
            api_response = self.api_instance.control_power_off_put(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def control_power_reboot_put(self) -> str:
        try:
            api_response = self.api_instance.control_power_reboot_put(async_req=True)
            return api_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""



if __name__ == '__main__':
    print("")

    str_ip_address = "127.0.0.1"
    str_client_name = "dracula"

    oAna = analyzer_client(str_ip_address, str_client_name)

    oOut = oAna.measurement_supported_consumables_get()
    print(oOut)
    oOut = oAna.channel_measurement_get_measurement_status()
    print(oOut)

