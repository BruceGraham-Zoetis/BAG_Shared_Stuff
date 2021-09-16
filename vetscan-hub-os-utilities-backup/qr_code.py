#!/usr/bin/env python3

"""
@file qr_code_utility.py

"""

class class_vetscan_qr_code_utility():
    """! The vetscan QR code class.
    """

    def __init__(self):
        """! The class_vetscan_qr_code_utility class initializer.
        @param -none-
        @return  An instance of the initialized class class_vetscan_qr_code_utility.
        """

        self.__debug = False # True: enable printing when an error occurs

        # TODO verify camera is connected

    def debug_on(self):
        self.__debug = True

    def debug_off(self):
        self.__debug = False

