#!/usr/bin/env python3
 
"""
@file test_network_control.py

@brief This file will hold unit tests for network_control functions.
"""

# *****************************************************************************
# imports
# *****************************************************************************
from __future__ import absolute_import
import unittest
import traceback
import logging

import network_control


class TestNetworkControl(unittest.TestCase):
    """! Test of the Network control class
    """

    def test_is_network_connected(self):
        """! Test: Verify that the network is connected
        Expected: True
        """
        net_control = network_control.class_vetscan_network_control()
        b_rtn = net_control.is_network_connected()
        self.assertTrue(b_rtn)


if __name__ == '__main__':
    
    try:
        unittest.main()
    except Exception as e:
        # Logs the error appropriately.
        print(e)
        logging.error(traceback.format_exc())

