#!/usr/bin/env python3
# coding: utf-8

"""
File: class_vetscan_hub.py

Purpose: Hub and analyzer classes. Hub contains a dictionary of analyzers.
"""

import os, sys
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
from class_analyzer_openapi import analyzer_client


"""
Purpose: Manage the connections to the analyzers on the Hub's local ethernet
"""
class CVetscanHub:
    # init method or constructor 
    def __init__(self):
        self.dictAnalyzers = {}

    def analyzer_connected(self, str_IP_Address : str, strName = "") -> bool:
        oAna = analyzer_client(str_IP_Address, strName)
        self.dictAnalyzers[str_IP_Address] = oAna
        return True

    def analyzer_set_name(self, str_IP_Address : str, strName : str) -> bool:
        oAna = analyzer_client(str_IP_Address, strName)
        self.dictAnalyzers[str_IP_Address] = oAna
        return True

    def analyzer_disconnected(self, str_IP_Address : str):
        self.dictAnalyzers.pop(str_IP_Address)

    def analyzer_get(self, str_IP_Address : str) -> analyzer_client:
        try:
            oAna = self.dictAnalyzers[str_IP_Address]
        except:
            oAna = analyzer_client("", "")
        return oAna