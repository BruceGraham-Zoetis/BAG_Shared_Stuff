#!/usr/bin/env python3
 
"""
@file audio_volume_control.py

@brief Python wrapper for the Linux audio device (amixer).
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
$ sudo pip install pyalsaaudio

"""

use_amixer = True

if (use_amixer):
    #from subprocess import call
    import subprocess
else:
    import alsaaudio



class class_vetscan_audio_volume():
    """! The vetscan audio volume control class.
    """

    def __init__(self):
        """! The class_vetscan_audio_volume class initializer.
        @param -none-
        @return  An instance of the initialized class class_vetscan_audio_volume.
        """

        self.__debug = False # True: enable printing when an error occurs

        # TODO - verify amixer is installed

    def debug_on(self):
        self.__debug = True

    def debug_off(self):
        self.__debug = False


    def set_percent(self, volume_pct: int) -> int:
        """! Set the percent master volume of the audio system.

        @param[in] volume_pct: int - Range: [0 - 100] the desired system volume in percent.
        @return: int - Range [0 - 100] the master volume, as a percent of max volume.
        @return: int - -1 there was an error
        """
        i_volume_pct = 0

        # make sure that the incoming value was a valid value
        if (str == type(volume_pct)):
            try:
                i_volume_pct = int(volume_pct)
            except Exception as e:
                if (self.__debug): print("ERROR: set_percent() str value not [0 - 100]")
                if (self.__debug): print(e)
                return -1
        elif (int == type(volume_pct)):
            i_volume_pct = volume_pct
        else:
            if (self.__debug): print("ERROR: set_percent() not type int or str")
            return -1

        if (i_volume_pct < 0) or (100 < i_volume_pct):
            if (self.__debug): print("ERROR: set_percent() value not [0 - 100]")
            return -1
                
        try:
            if (use_amixer):
                command = ["amixer", "-D", "pulse", "sset", "Master", str(i_volume_pct)+"%"]
                """
                p = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE)
                b_output, error = p.communicate()
                """
                process = subprocess.run(command, check=True, stdout=subprocess.PIPE, universal_newlines=True)
                b_output = process.stdout
                # Parse amixer binary output string will contain the volume in brackets. Ex: "... [70%] ..."
                output = str(b_output)
                #print(output)
                int_start = output.find("[")
                int_end   = output.find("%")
                str_z = output[int_start + 1: int_end]
                i_percent = int(str_z)
                if (i_percent < 0) or (100 < i_percent):
                    if (self.__debug): print("ERROR: set_percent() amixer returned value not [0 - 100]")
                    return -1
                else:
                    return i_percent
            else:
                mixer = alsaaudio.Mixer('Master')
                mixer.setvolume(i_volume_pct)
                i_percents = mixer.getvolume()
                return i_percents[0]

        except Exception as e:
            if (self.__debug): print("ERROR: set_percent()")
            if (self.__debug): print(e)
            return -1


    def get_percent(self) -> int:
        """! Get the percent master volume of the audio system.
        @param[in] None

        @return: int - Range [0 - 100] the master volume, as a percent of max volume.
        @return: int - -1 there was an error
        """
        try:
            if (use_amixer):
                command = ["amixer", "-D", "pulse", "sget", "Master"]
                """
                p = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE)
                b_output, error = p.communicate()
                """
                process = subprocess.run(command, check=True, stdout=subprocess.PIPE, universal_newlines=True)
                b_output = process.stdout
                # Parse amixer binary output string will contain the volume in brackets. Ex: "... [70%] ..."
                output = str(b_output)
                #print(output)
                int_start = output.find("[")
                int_end   = output.find("%")
                str_z = output[int_start + 1: int_end]
                i_percent = int(str_z)
                if (i_percent < 0) or (100 < i_percent):
                    if (self.__debug): print("ERROR: set_percent() amixer returned value not [0 - 100]")
                    return -1
                else:
                    return i_percent
            else:
                mixer = alsaaudio.Mixer('Master')
                i_percents = mixer.getvolume()
                i_percent = i_percents[0]
                return i_percent

        except Exception as e:
            if (self.__debug): print("ERROR: get_percent()")
            if (self.__debug): print(e)
            return -1
        
