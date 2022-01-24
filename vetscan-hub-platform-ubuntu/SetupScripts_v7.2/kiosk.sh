#!/bin/bash

# s - switch to VT when starting command
# c - the VT number
# -- says to stop looking for command directives for openvt
# the rest of the command is what to run on the other page

#sudo openvt -c 10 -- fbi --autoup --noverbose /home/vetscan/Desktop/Screen_3.jpg > /dev/null 2>&1

#sudo chvt 10

#sudo fbi -T 10 --autoup --noverbose /home/vetscan/Desktop/Screen_3.jpg > /dev/null 2>&1

#sleep 10

#sudo chvt 2

touch /home/vetscan/Desktop/ScriptRan

#eog -f -g /home/vetscan/Desktop/Screen_3.jpg &
feh --auto-zoom --fullscreen /home/vetscan/Desktop/hub_background.png & 

/home/vetscan/./"VetScan HUB-0.1.0.AppImage" &

sleep 60

#pkill eog
pkill feh

touch /home/vetscan/Desktop/ScriptStopped

exit
