# coding: utf-8

"""
File: class_vetscan_hub.py

Purpose: A Hub class
"""
import os
import threading
import requests
from requests.api import get

debug_trace = True
#debug_trace = False

"""
Purpose: keep info about a connected analyzer
"""
class CVetscanAnalyzerInfo:
    
    # init method or constructor 
    def __init__(self, str_IP_Address  = "", strName  = ""):
        self.str_IP_Address = str_IP_Address
        self.strName = strName

    def get_ip_address(self) -> str:
        return self.str_IP_Address

    #####################################################
    ## PUT, GET to Analyzer
    def get_consumables(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/measurement/supported_consumables"
        r = requests.get(strRequest)
        if (debug_trace):
            print(strRequest)
            print(r.text)
        return r.text

    def light_blink(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/control/light/blink"
        #r = requests.put(strRequest, data = {'key':'value'})
        r = requests.put(strRequest)
        if (debug_trace):
            print(strRequest)
            print(r.text)
        return r.text

    def light_off(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/control/light/off"
        r = requests.put(strRequest)
        if (debug_trace):
            print(strRequest)
            print(r.text)
        return r.text

    def power_off(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/control/power/off"
        r = requests.put(strRequest)
        if (debug_trace):
            print(strRequest)
            print(r.text)
        return r.text

    def power_reboot(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/control/power/reboot"
        r = requests.put(strRequest)
        if (debug_trace):
            print(strRequest)
            print(r.text)
        return r.text






"""
Purpose: Manage the connections to the analyzers on the Hub's local ethernet
"""
class CVetscanHub:
    # class scope
    dictAnalyzers = {}
 
    # methods
        
    # init method or constructor 
    def __init__(self):
        pass

    def add_analyzer(self, str_IP_Address : str, strName : str) -> bool:
        self.dictAnalyzers[str_IP_Address] = strName
        return True

    def remove_analyzer(self, str_IP_Address : str) -> bool:
        del self.dictAnalyzers[str_IP_Address]
        return True

    def get_analyzer(self, str_IP_Address : str) -> CVetscanAnalyzerInfo:
        refAnalyzer = CVetscanAnalyzerInfo()

        value = self.dictAnalyzers.get(str_IP_Address)
        if (0 < len(value)):
            refAnalyzer.str_IP_Address = str_IP_Address
            refAnalyzer.strName        = self.dictAnalyzers[str_IP_Address]
        else:
            refAnalyzer.str_IP_Address = ""
            refAnalyzer.strName        = ""

        return refAnalyzer


