#!/usr/bin/env python3
# coding: utf-8

"""
File: class_analyzer_openapi.py
"""

import os, sys
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
            self.configuration_api          = openapi_client.ConfigurationChannelApi(api_client)
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
    def configuration_factory_reset_put(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.configuration_api.configuration_factory_reset_put(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def configuration_get(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.configuration_api.configuration_get(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def configuration_put(self, body : str) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.configuration_api.configuration_put(body, async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def configuration_schema_get(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.configuration_api.configuration_schema_get(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

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
    # Class: MeasurementChannelApi
    ################################################

    def measurement_cancel_post(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.measurement_channel_api.measurement_cancel_post(async_req=True)
            str_response = thread.get()
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
            thread = self.measurement_channel_api.measurement_consumable_consumable_uuid_post(consumable_uuid, async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_file_post(self, inline_object1) -> str:
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

    #def measurement_results_get(self, start_datetime : str, end_datetime : str) -> str:
    def measurement_results_get(self, **kwargs) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            #thread = self.measurement_channel_api.measurement_results_get(start_datetime, end_datetime, async_req=True)
            thread = self.measurement_channel_api.measurement_results_get(async_req=True, **kwargs)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

    def measurement_results_latest_get(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.measurement_channel_api.measurement_results_latest_get(async_req=True)
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
    def status_currently_activated_events_get(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.status_channel_api.status_currently_activated_events_get(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""
    
    def status_operational_get(self) -> str:
        try:
            if (self.__trace): print(inspect.currentframe().f_code.co_name)
            thread = self.status_channel_api.status_operational_get(async_req=True)
            str_response = thread.get()
            if (self.__trace):
                print("\tReturned: ", end = '')
                print(str_response)
            return str_response
        except ApiException as e:
            print("Exception when calling %s() error: %s\n" % (inspect.currentframe().f_code.co_name, e))
            return ""

