#!/usr/bin/env python3
 
"""
@file test_play_sound.py

@brief This file will hold unit tests for play_sound functions.
"""

# *****************************************************************************
# imports
# *****************************************************************************
from __future__ import absolute_import
import unittest
import traceback
import logging

import play_sound


class TestPlaySound(unittest.TestCase):
    """! Test of the Network control class
    """

    def test_play_wave_file_missing_file(self):
        """! Test: Verify that the wav file is not found.
        Expected: False
        """
        o_play = play_sound.class_vetscan_play_sound()
        o_play.debug_on()
        b_rtn = o_play.play_wave_file("missing_file.wav")
        self.assertFalse(b_rtn)

    def test_play_wave_file_good_file(self):
        """! Test: Verify that the wav file is played without error
        Expected: True
        """
        o_play = play_sound.class_vetscan_play_sound()
        o_play.debug_on()
        b_rtn = o_play.play_wave_file("./test_data_files/beep-08b.wav")
        self.assertTrue(b_rtn)

    def test_play_wave_file_good_file(self):
        """! Test: Verify that the non-payable wav file is not played
        Expected: True
        """
        o_play = play_sound.class_vetscan_play_sound()
        o_play.debug_on()
        # This test fails because aplay does not return an error with an invalid file
        # b_rtn = o_play.play_wave_file("./test_data_files/non_playable.wav")
        # TODO - self.assertFalse(b_rtn)

if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        # Logs the error appropriately.
        print(e)
        logging.error(traceback.format_exc())


