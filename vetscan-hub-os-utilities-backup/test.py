#!/usr/bin/env python3
 
"""
@file test.py

@brief Runs all unittests for all py files.
"""

import unittest
import traceback
import logging

import test_audio_volume_control

""" future tests
import test_network_control
import test_play_sound
import test_network_control
import test_play_sound
"""


if __name__ == '__main__':
    
    try:
        suite1 = unittest.TestLoader().loadTestsFromTestCase(test_audio_volume_control.TestAudioVolumeControl)
        unittest.TextTestRunner(verbosity=2).run(suite1)

        """
        suite2 = unittest.TestLoader().loadTestsFromTestCase(test_network_control.TestNetworkControl)
        unittest.TextTestRunner(verbosity=2).run(suite2)

        suite3 = unittest.TestLoader().loadTestsFromTestCase(test_play_sound.TestPlaySound)
        unittest.TextTestRunner(verbosity=2).run(suite3)
        """

    except Exception as e:
        # Logs the error appropriately.
        print(e)
        logging.error(traceback.format_exc())
