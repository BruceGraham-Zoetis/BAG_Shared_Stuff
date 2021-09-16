#!/usr/bin/env python3

"""
@file play_sound.py

"""

import subprocess
from os.path import exists


class class_vetscan_play_sound():
    """! The vetscan play sound control class.
    """

    def __init__(self):
        """! The class_vetscan_play_sound class initializer.
        @param -none-
        @return  An instance of the initialized class class_vetscan_play_sound.
        """

        self.__debug = False # True: enable printing when an error occurs

        # TODO - verify aplay is installed

    def debug_on(self):
        self.__debug = True

    def debug_off(self):
        self.__debug = False
    

    def play_wave_file(self, str_path_file_name : str) -> bool:	
        """! Play a wav file, given a path and file name. Blocks until wave is played.

        Example:
            play_wave_file("./beep-08b.wav")

        @param[in] str_path_file_name = path and file name of a wav file.

        @returns True = played file
        @returns False = failed
        """

        try:
            if (self.__debug): print("play_wave_file(%s)" % (str_path_file_name))

            file_exists = exists(str_path_file_name)
            if (not file_exists):
                if (self.__debug): print("ERROR: play_wave_file() File not found %s" % (str_path_file_name))
                return False

            n_rtn = subprocess.call(["aplay", "-q", str_path_file_name])
            if (0 == n_rtn):
                return True
            else:
                if (self.__debug): print("ERROR: play_wave_file() aplay %s" % (str_path_file_name))
                return False
        except Exception as e:
            if (self.__debug): print("ERROR: play_wave_file() aplay %s" % (str_path_file_name))
            if (self.__debug): print(e)
            return False
