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




class class_vetscan_audio_volume_control():
    """! The vetscan audio volume control class.
    """

    def __init__(self):
        """! The class_vetscan_audio_volume_control class initializer.
        @param -none-
        @return  An instance of the initialized class class_vetscan_audio_volume_control.
        """

        self.__debug = False # True: enable printing when an error occurs
        
       
        if (use_amixer):
            self._amixer_master_device = self.get_platform_master_device_name()
        else:
            self._amixer_master_device = ""

        # TODO - verify amixer is installed

    def debug_on(self):
        self.__debug = True

    def debug_off(self):
        self.__debug = False


    def get_platform_master_device_name(self) -> str:
        """! Return the name of the master audio output device
    
        @param[in] None

        @return: str - name

        <TABLE>
        <TR><TD>Type</TD><TD>Value Range</TD><TD>Device Name</TD></TR>
        <TR><TD>int</TD><TD>""</TD><TD>None</TD></TR>
        <TR><TD>int</TD><TD>string</TD><TD>The device name</TD></TR>
        </TABLE>        
        """

        list_command = ["uname", "-n"]
        process = subprocess.run(list_command, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        strb_output = process.stdout
        str_output = str(strb_output)

        if (-1 != str_output.find("ubuntu")):
            """! mockup lubuntu & virtual machine:
            Uses pulse: mixer -D pulse set Master 50%
            """
            str_name = "pulse"

        elif (-1 != str_output.find("vetscan-hub")):
            """! mockup lubuntu & yocto on D0:
            Uses default: amixer set Master 50%
            """
            str_name = ""

        else:
            str_name = ""

        return str_name


    def build_amixer_set_volume_command(self, int_volume_percent : int) -> list:
        """! Return the set volume command to use with amixer
    
        @param[in] int - int_volume_percent: the percent of max volume to use. Range: 0 to 100
        
        @return: str - the command to use with amixer
        """

        if (0 == len(self._amixer_master_device)):
            list_command = ["amixer", "sset", "Master", str(int_volume_percent)+"%"]
        else:
            list_command = ["amixer", "-D", self._amixer_master_device, "sset", "Master", str(int_volume_percent)+"%"]
        return list_command


    def build_amixer_get_volume_commond(self) -> list:
        """! Return the get volume command to use with amixer
    
        @param[in] int - int_volume_percent: the percent of max volume to use. Range: 0 to 100
        
        @return: str - the command to use with amixer
        """

        if (0 == len(self._amixer_master_device)):
            list_command = ["amixer", "sget", "Master"]
        else:
            list_command = ["amixer", "-D", self._amixer_master_device, "sget", "Master"]
        return list_command


    def parse_out_volume_percent(self, str_amixer_output : str) -> int:
        """! Parse the volume from the return string from amixer.

        The string will contain the volume in brackets. Ex: "... [70%] ..."

        @param[in] str_amixer_output: str - the return string from amixer.

        @return: int - result

        <TABLE>
        <TR><TD>Type</TD><TD>Value Range</TD><TD>Result</TD></TR>
        <TR><TD>int</TD><TD>0 to 100</TD><TD>The volume</TD></TR>
        <TR><TD>int</TD><TD>-1</TD><TD>ERROR: volume not found</TD></TR>
        </TABLE>
        """
        
        int_start = str_amixer_output.find("[")
        int_end   = str_amixer_output.find("%")
        str_z = str_amixer_output[int_start + 1: int_end]
        i_percent = int(str_z)
        
        if (i_percent < 0) or (100 < i_percent):
            i_percent = -1
            if (self.__debug):
                print("ERROR: set_percent() amixer returned value not [0 - 100]")

        return i_percent


    def set_percent(self, int_volume_percent: int) -> int:
        """! Set the percent master volume of the audio system.

        @param[in] int_volume_percent: int - the desired system volume in percent.

        <TABLE>
        <TR><TD>Type</TD><TD>Direction</TD><TD>Name</TD><TD>Value Range</TD></TR>
        <TR><TD>int</TD><TD>in</TD><TD>int_volume_percent</TD><TD>0 to 100</TD></TR>
        </TABLE>

        @return: int - result

        <TABLE>
        <TR><TD>Type</TD><TD>Value Range</TD><TD>Result</TD></TR>
        <TR><TD>int</TD><TD>0 to 100</TD><TD>The new volume as a percent of max volume</TD></TR>
        <TR><TD>int</TD><TD>-1</TD><TD>The volume was not set</TD></TR>
        </TABLE>
        """

        # validate input type
        if (int != type(int_volume_percent)):
            if (self.__debug): print("ERROR: set_percent() requires type int")
            return -1

        # validate input value range
        if (int_volume_percent < 0) or (100 < int_volume_percent):
            if (self.__debug): print("ERROR: set_percent() value not [0 - 100]")
            return -1
                
        try:
            if (use_amixer):
                list_command = self.build_amixer_set_volume_command(int_volume_percent)
                process = subprocess.run(list_command, check=True, stdout=subprocess.PIPE, universal_newlines=True)
                strb_output = process.stdout
                str_output = str(strb_output)
                i_percent = self.parse_out_volume_percent(str_output)
                return i_percent
            else:
                mixer = alsaaudio.Mixer('Master')
                mixer.setvolume(int_volume_percent)
                i_percents = mixer.getvolume()
                return i_percents[0]

        except Exception as e:
            if (self.__debug): print("ERROR: set_percent()")
            if (self.__debug): print(e)
            return -1


    def get_percent(self) -> int:
        """! Get the percent master volume of the audio system.
        @param[in] None

        @return: int - result

        <TABLE>
        <TR><TD>Type</TD><TD>Value Range</TD><TD>Result</TD></TR>
        <TR><TD>int</TD><TD>0 to 100</TD><TD>The volume as a percent of max volume</TD></TR>
        <TR><TD>int</TD><TD>-1</TD><TD>ERROR</TD></TR>
        </TABLE>
        """

        try:
            if (use_amixer):
                list_command = self.build_amixer_get_volume_commond()
                process = subprocess.run(list_command, check=True, stdout=subprocess.PIPE, universal_newlines=True)
                strb_output = process.stdout
                str_output = str(strb_output)
                i_percent = self.parse_out_volume_percent(str_output)
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
        
