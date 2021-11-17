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

import audio_volume_control


class TestAudioVolumeControl(unittest.TestCase):
    """! Test of the Audio control class
    """

    def test_get_percent_ok(self):
        """! Test: Get the master volume. It should be between 0 and 100.
        Expected: Current audio volume is 0% to 100% of max volume
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume_control()
        i_rtn = vetscan_audio.get_percent()
        self.assertGreaterEqual(i_rtn, 0)
        self.assertLessEqual(i_rtn, 100)

    def test_set_percent_in_bounds(self):
        """! Test: Set the master volume to "in bound" values
        Expected: volume is set
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume_control()

        list_ib = [0, 1, 50, 99, 100]

        for i_value in list_ib:
            i_rtn = vetscan_audio.set_percent(i_value)
            self.assertNotEqual(i_rtn, -1)
            
            self.assertGreaterEqual(i_rtn, 0)
            self.assertLessEqual(i_rtn, 100)

            """! amixer is returning volumes that are a few % from the set value.
            Ex: using 50% returns 51%.
            """
            self.assertGreaterEqual(i_rtn, i_rtn - 2)
            self.assertLessEqual(i_rtn, i_rtn + 2)


    def test_set_percent_out_of_bounds(self):
        """! Test: Set the master volume to "out of bounds" values
        Expected: Volume is not set. Error (-1) is set.
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume_control()

        list_oob = [-100, -50, -1, 101, 200]

        for i_value in list_oob:
            i_rtn = vetscan_audio.set_percent(i_value)
            self.assertEqual(i_rtn, -1)


    def test_set_percent_invalid_input_types(self):
        """! Test: Set the master volume to a bogus type list [20].
        Expected: Volume is not set. No exception is thrown.
        """
        vetscan_audio = audio_volume_control.class_vetscan_audio_volume_control()

        list_variable = [20]
        try:
            i_rtn = vetscan_audio.set_percent(list_variable)
            self.assertEqual(i_rtn, -1)
        except Exception as e:
            self.fail("set_percent() raised unexpectedly!")

        str_variable = "20"
        try:
            i_rtn = vetscan_audio.set_percent(str_variable)
            self.assertEqual(i_rtn, -1)
        except Exception as e:
            self.fail("set_percent() raised unexpectedly!")




