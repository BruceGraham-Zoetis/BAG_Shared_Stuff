#!/usr/bin/env python3

"""
@file wifi_control.py

"""


class class_vetscan_wifi_control_utility():
    """! The vetscan QR code class.
    """

    def __init__(self):
        """! The class_vetscan_wifi_control_utility class initializer.
        @param -none-
        @return  An instance of the initialized class class_vetscan_wifi_control_utility.
        """

        self.__debug = False # True: enable printing when an error occurs

        # TODO - verify dependant services are installed
        

    def debug_on(self):
        self.__debug = True

    def debug_off(self):
        self.__debug = False

