#!/usr/bin/env python3
 
"""
@file test_print_utility.py

@brief This file will hold unit tests for print_utility functions.
"""

# *****************************************************************************
# imports
# *****************************************************************************
from __future__ import absolute_import
import unittest
import traceback
import logging

import print_utility


class TestNetworkControl(unittest.TestCase):
    """! Test of the Network control class
    """

    def test_is_printer_connected(self):
        """! Test: Verify that a printer is connected
        Expected: True
        """
        net_control = print_utility.class_vetscan_print_utility()
        b_rtn = net_control.is_printer_connected()
        self.assertTrue(b_rtn)


if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        # Logs the error appropriately.
        print(e)
        logging.error(traceback.format_exc())

