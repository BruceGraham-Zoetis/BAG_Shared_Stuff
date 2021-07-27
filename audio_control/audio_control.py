"""
File: audio_control.py

Purpose: Python wrapper for the Linux audio device (amixer).
Used to control the Vetscan speaker volume.

sudo apt-get install python-alsaaudio
import alsaaudio
>>> m = alsaaudio.Mixer()
>>> vol = m.getvolume()
>>> vol
[50L]
>>> newVol = vol + 10
>>> m.setvolume(newVol)
>>> newVol
[60L]

"""

from subprocess import call

"""
Uses amixer to set the Master Volume as a percent of max volume.
@param[in] iPercent - percentage from 0 to 100
@returns True - success
@returns False - failed to set volume
"""
def audio_set_master_volume(iPercent: int):
    if (0 <= iPercent) and (iPercent <= 100):
        try:
            call(["amixer", "-D", "pulse", "sset", "Master", str(iPercent)+"%"])
            return True

        except ValueError:
            return False
    else:
        return False

"""
def audio_set_left_right_volume(iLeftPercent: int, iRightPercent: int):
    if (0 <= iLeftPercent) and (iLeftPercent <= 100) and (0 <= iRightPercent) and (iRightPercent <= 100):
        try:
            call(["amixer", "-D", "pulse", "sset", "Master", str(iLeftPercent)+"%"])
            return True

        except ValueError:
            return False
    else:
        return False
"""


"""
for iPercent in range(100, -25, -25):
    print("Testing at " + str(iPercent) + "%")
    audio_set_master_volume(iPercent)
"""
