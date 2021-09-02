#!/usr/bin/env python3
# coding: utf-8

"""
File: class_analyzer_openapi.py
"""

#import os
#import threading
import requests

"""
Purpose: keep info about a connected analyzer
"""
class analyzer_openapi:
    # init method or constructor 
    def __init__(self, str_IP_Address : str, strName : str):
        self.__str_IP_Address = str_IP_Address
        self.__strName = strName

    def get_ip_address(self) -> str:
        return self.__str_IP_Address

    def get_name(self) -> str:
        return self.__strName

    def get_consumables(self) -> str:
        try:
            strRequest = "http://" + self.__str_IP_Address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""

    def light_blink(self) -> str:
        try:
            strRequest = "http://" + self.__str_IP_Address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""

    def light_off(self) -> str:
        try:
            strRequest = "http://" + self.__str_IP_Address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""

    def power_off(self) -> str:
        try:
            strRequest = "http://" + self.__str_IP_Address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""

    def power_reboot(self) -> str:
        try:
            strRequest = "http://" + self.__str_IP_Address + ":8080/measurement/supported_consumables"
            r = requests.get(strRequest)
            return r.text
        except:
            return ""