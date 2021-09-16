#!/usr/bin/env python3
 
"""
@file test_audio_volume_control.py

@brief This file will hold unit tests for all utility functions.
"""

# *****************************************************************************
# imports
# *****************************************************************************
from __future__ import absolute_import
import unittest
import traceback
import logging

import audio_volume_control


class TestAudioVolumeControl(unittest.TestCase):
    """! Test of the Audio control class
    """

    def test_get_percent_ok(self):
        """! Test: Get the master volume. It should be between 0 and 100.
        Expected: volume is set to 75% of max volume
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume()
        i_rtn = vetscan_audio.get_percent()
        self.assertGreaterEqual(i_rtn, 0)
        self.assertLessEqual(i_rtn, 100)

    def test_set_percent_75(self):
        """! Test: Set the master volume to 75
        Expected: volume is set to 75% of max volume
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume()
        i_rtn = vetscan_audio.get_percent()
        self.assertNotEqual(i_rtn, -1)
        i_rtn = vetscan_audio.set_percent(75)
        self.assertEqual(i_rtn, 75)
        i_rtn = vetscan_audio.get_percent()
        self.assertEqual(i_rtn, 75)

    def test_set_percent_10(self):
        """! Test: Set the master volume to 10
        Expected: volume is set to 10% of max volume
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume()
        i_rtn = vetscan_audio.get_percent()
        self.assertNotEqual(i_rtn, -1)
        i_rtn = vetscan_audio.set_percent(10)
        self.assertEqual(i_rtn, 10)
        i_rtn = vetscan_audio.get_percent()
        self.assertEqual(i_rtn, 10)
        

    def test_set_percent_101(self):
        """! Test: Set the master volume to out of bounds numbers
        Expected: Volume is not set. Error (-1) is set.
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume()
        i_rtn = vetscan_audio.get_percent()
        self.assertNotEqual(i_rtn, -1)
        i_rtn = vetscan_audio.set_percent(10)
        self.assertEqual(i_rtn, 10)
        i_rtn = vetscan_audio.set_percent(101)
        self.assertEqual(i_rtn, -1)
        i_rtn = vetscan_audio.get_percent()
        self.assertEqual(i_rtn, 10)

    def test_set_percent_valid_string(self):
        """! Test: Set the master volume using a string "20" for 20%
        Expected: Volume is set. No exception is thrown.
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume()
        i_rtn = vetscan_audio.get_percent()
        self.assertNotEqual(i_rtn, -1)
        i_rtn = vetscan_audio.set_percent(10)
        self.assertEqual(i_rtn, 10)

        variable = "20"
        try:
            i_rtn = vetscan_audio.set_percent(variable)
        except Exception as e:
            self.fail("set_percent() raised unexpectedly!")

        self.assertEqual(i_rtn, 20)
        i_rtn = vetscan_audio.get_percent()
        self.assertEqual(i_rtn, 20) # Expect: changed

    def test_set_percent_invalid_type(self):
        """! Test: Set the master volume to a bogus type list [20].
        Expected: Volume is not set. No exception is thrown.
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume()
        i_rtn = vetscan_audio.get_percent()
        self.assertNotEqual(i_rtn, -1)
        i_rtn = vetscan_audio.set_percent(10)
        self.assertEqual(i_rtn, 10)
        variable = [20]
        try:
            i_rtn = vetscan_audio.set_percent(variable)
        except Exception as e:
            self.fail("set_percent() raised unexpectedly!")

        self.assertEqual(i_rtn, -1)
        i_rtn = vetscan_audio.get_percent()
        self.assertEqual(i_rtn, 10) # Expect: not changed



if __name__ == '__main__':
    
    try:
        unittest.main()
    except Exception as e:
        # Logs the error appropriately.
        print(e)
        logging.error(traceback.format_exc())

