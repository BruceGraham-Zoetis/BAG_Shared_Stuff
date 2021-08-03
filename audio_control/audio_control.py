#!/usr/bin/env python3
 
"""
File: audio_control.py

Purpose: Python wrapper for the Linux audio device (amixer).
Used to control the Vetscan speaker volume.

amixer app - command line
================================
Uses amixer to set the Master Volume as a percent of max volume.
amixer - see https://linux.die.net/man/1/amixer

call(["amixer", "-D", "pulse", "sset", "Master", str(iPercent)+"%"])


Python ALSA audio
===================================
$ git clone https://github.com/larsimmisch/pyalsaaudio.git
$ cd pyalsaaudio
$ python3 setup.py build
$ sudo python3 setup.py install

import alsaaudio
>>> m = alsaaudio.Mixer()
>>> vol = m.getvolume()
>>> vol
[50L]
>>> newVol = vol + 10
>>> m.setvolume(newVol)
>>> newVol
[60L]

TODO - SEE 
import alsaaudio
m = alsaaudio.Mixer(alsaaudio.mixers[0]) # alsaaudio.mixers = ["PCM"] for me.
m.setvolume(90) # Or whatever

"""

#from subprocess import call
#import sys
#import wave
#import getopt
import alsaaudio


"""
Purpose: Set the Master volume given a percent of maximum volume.

@param[in] iPercent - percentage from 0 to 100
@returns True - success
@returns False - failed to set volume
"""
def audio_set_master_volume(iPercent: int) -> bool:
    if (0 <= iPercent) and (iPercent <= 100):
        try:
            # mixer = alsaaudio.mixers(0)
            m = alsaaudio.Mixer('Master')
            m.setvolume(iPercent)
            #call(["amixer", "-D", "pulse", "sset", "Master", str(iPercent)+"%"])
            return True
        except ValueError:
            return False
    else:
        return False

"""
Purpose: Get the Master volume given a percent of maximum volume.

@returns 0 - 100 - success
@returns -1 - failed to set volume
"""
def audio_get_master_volume() -> int:
    try:
        m = alsaaudio.Mixer('Master')
        iPercents = m.getvolume()
        iPercent = iPercents[0]
        return iPercent
    except ValueError:
        return -1



