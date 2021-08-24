# coding: utf-8

"""
File: class_vetscan_hub.py

Purpose: Hub and analyzer classes. Hub contains a dictionary of analyzers.
"""
import os
import threading
import requests


"""
Purpose: keep info about a connected analyzer
"""
class CVetscanAnalyzerInfo:
    # init method or constructor 
    def __init__(self, str_IP_Address : str, strName : str):
        self.str_IP_Address = str_IP_Address
        self.strName = strName

    def get_ip_address(self) -> str:
        return self.str_IP_Address

    def get_consumables(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/measurement/supported_consumables"
        r = requests.get(strRequest)
        return r.text

    def light_blink(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/measurement/supported_consumables"
        r = requests.get(strRequest)
        return r.text

    def light_off(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/measurement/supported_consumables"
        r = requests.get(strRequest)
        return r.text

    def power_off(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/measurement/supported_consumables"
        r = requests.get(strRequest)
        return r.text

    def power_reboot(self) -> str:
        strRequest = "http://" + self.str_IP_Address + ":8080/measurement/supported_consumables"
        r = requests.get(strRequest)
        return r.text
"""
Purpose: Manage the connections to the analyzers on the Hub's local ethernet
"""
class CVetscanHub:
    # init method or constructor 
    def __init__(self):
        self.dictAnalyzers = {}

    def analyzer_add(self, str_IP_Address : str, strName = "") -> CVetscanAnalyzerInfo:
        oAna = CVetscanAnalyzerInfo(str_IP_Address, strName)
        self.dictAnalyzers[str_IP_Address] = oAna
        return True

    def analyzer_set_name(self, str_IP_Address : str, strName : str) -> CVetscanAnalyzerInfo:
        oAna = CVetscanAnalyzerInfo(str_IP_Address, strName)
        self.dictAnalyzers[str_IP_Address] = oAna
        return True

    def analyzer_remove(self, str_IP_Address : str):
        self.dictAnalyzers.pop(str_IP_Address)

    def analyzer_get(self, str_IP_Address : str) -> CVetscanAnalyzerInfo:
        try:
            oAna = self.dictAnalyzers[str_IP_Address]
        except:
            oAna = CVetscanAnalyzerInfo("", "")
        return oAna