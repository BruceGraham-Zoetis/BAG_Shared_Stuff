#!/usr/bin/env python3
# coding: utf-8

"""
File: class_analyzer_openapi.py
"""

import os, sys
import requests

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
        self.configuration = openapi_client.Configuration(host = "http://localhost")

        # Enter a context with an instance of the API client
        with openapi_client.ApiClient() as api_client:
            # Create an instance of the API class
            self.api_instance = openapi_client.MeasurementChannelApi(api_client)

        self.__str_ip_address = str_ip_address
        self.__str_client_name = str_client_name

    def get_ip_address(self) -> str:
        return self.__str_ip_address

    def get_name(self) -> str:
        return self.__str_client_name

    def measurement_supported_consumables_get(self):
        try:
            api_response = self.api_instance.measurement_supported_consumables_get()
            return api_response
        except ApiException as e:
            print("Exception when calling MeasurementChannelApi->measurement_supported_consumables_get: %s\n" % e)
            return None

    def get_consumables(self) -> str:
        try:
            strRequest = "http://" + self.__str_ip_address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""

    def light_blink(self) -> str:
        try:
            strRequest = "http://" + self.__str_ip_address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""

    def light_off(self) -> str:
        try:
            strRequest = "http://" + self.__str_ip_address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""

    def power_off(self) -> str:
        try:
            strRequest = "http://" + self.__str_ip_address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""

    def power_reboot(self) -> str:
        try:
            strRequest = "http://" + self.__str_ip_address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""



if __name__ == '__main__':
    print("")

    str_ip_address = "127.0.0.1"
    str_client_name = "dracula"

    oAna = analyzer_client(str_ip_address, str_client_name)
    oOut = oAna.measurement_supported_consumables_get()
    print(oOut)
