#!/usr/bin/env python3
 
"""
File: audio_test.py

Purpose: Calls the Python functions that are used to control the volume.

"""

#import sys
import wave
import time
import audio_control
import audio_play


# The test volume play, Hear “front left”, then “front right”, at 100% to 0%
def test_audio_set_master_volume():

    for iPercent in range(100, -25, -25):
        print("Testing at " + str(iPercent) + "%")
        bRtn = audio_control.audio_set_master_volume(iPercent)
        if (not bRtn):
            print("Failed audio_get_master_volume() returned False")
            break
        
        iPercentOrg = audio_control.audio_get_master_volume()
        if (iPercentOrg != iPercent):
            print("Failed audio_get_master_volume() did not get what audio_set_master_volume() set")
            break

        for i in range(1, 5):
            print("   Beep")
            audio_play.playWaveFileAndBlock("./beep-08b.wav")
            print("   ...sleep(0.2)...")
            time.sleep(0.2)

        print("\n")



if __name__ == '__main__':
    test_audio_set_master_volume()

    print("Setting volume to 100%")
    audio_control.audio_set_master_volume(100)


    
