"""
File: audio_test.py

Purpose: Calls the Python functions that are used to control the volume.

"""

import sys
import wave
import time
import audio_control
import audio_play


# The test volume play, Hear “front left”, then “front right”, at 100% to 0%
def test_audio_set_master_volume():
    for iPercent in range(100, -25, -25):
        print("Testing at " + str(iPercent) + "%")
        audio_control.audio_set_master_volume(iPercent)



if __name__ == '__main__':
    test_audio_set_master_volume()

    time.sleep(2)

    f = wave.open("./beep-08b.wav", 'rb')
    for i in range(1, 10):
        audio_play.play(f)
