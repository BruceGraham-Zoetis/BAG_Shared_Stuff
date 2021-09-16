#!/usr/bin/env python3

"""
@file network_control.py

"""

class class_vetscan_network_control():
    """! The vetscan network control class.
    """

    def __init__(self):
        """! The class_vetscan_network_control class initializer.
        @param -none-
        @return  An instance of the initialized class class_vetscan_network_control.
        """

        self.__debug = False # True: enable printing when an error occurs

        # TODO - verify dependant services are installed

    def debug_on(self):
        self.__debug = True

    def debug_off(self):
        self.__debug = False

    def is_network_connected(self) -> bool:
        # TODO
        return True

