#!/usr/bin/env python3
 
"""
File: audio_test.py

Purpose: Calls the Python functions that are used to control the volume.

"""

#import sys
#import wave
import time
import audio_control
import audio_play

debug_play_long_file = False
#debug_play_long_file = True


# The test volume play, Hear “front left”, then “front right”, at 100% to 0%
def test_audio_set_master_volume(bUseBlocking : bool):

    #for iPercent in range(0, 125, 25):
    for iPercent in range(100, -25, -25):
        print("Testing with volume at " + str(iPercent) + "%")
        bRtn = audio_control.audio_set_master_volume(iPercent)
        if (not bRtn):
            print("Failed audio_get_master_volume() returned False")
            break
        
        iPercentOrg = audio_control.audio_get_master_volume()
        if (iPercentOrg != iPercent):
            print("Failed audio_get_master_volume() did not get what audio_set_master_volume() set")
            break

        for i in range(1, 3):
            print("   Playing wav file...")

            if (bUseBlocking):
                if (debug_play_long_file):
                    bRtn = audio_play.playWaveFileAndBlock("./file_example_WAV_1MG.wav")
                else:
                    bRtn = audio_play.playWaveFileAndBlock("./beep-08b.wav")
            else:
                if (debug_play_long_file):
                    bRtn = audio_play.playWaveFileNoBlock("./file_example_WAV_1MG.wav")
                    time.sleep(2.5)
                else:
                    bRtn = audio_play.playWaveFileNoBlock("./beep-08b.wav")
                    time.sleep(1)
            print("   ...finished")
            
            if (not bRtn):
                print("Failed playWaveFileAndBlock() returned False")
                break

            print("sleep...")
            time.sleep(1.0)

        print("\n")

    print("Setting volume to 100%")
    audio_control.audio_set_master_volume(100)
    print("   Playing wav file...")
    if (bUseBlocking):
        bRtn = audio_play.playWaveFileAndBlock("./2-3_hes_dead_jim1.wav")
    else:
        bRtn = audio_play.playWaveFileNoBlock("./2-3_hes_dead_jim1.wav")
        time.sleep(2.5)
    print("   ...finished")
    if (not bRtn):
        print("Failed playWaveFileAndBlock() returned False")


if __name__ == '__main__':
    test_audio_set_master_volume(False)
    #test_audio_set_master_volume(True)



    
