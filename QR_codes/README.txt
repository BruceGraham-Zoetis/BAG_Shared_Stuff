
What 						Where
=======================			=======================
REST APIs for Vetscan				vetscan_APIs
   Ex: Server (Hub) and Client (Analyzer)	
   REST APIs					vetscan_APIs/vetscan_hub_analyzer_API
Test Vetscan camera with QR code labels	QR_codes
test for audio functions			audio_control/audio_test.py
audio volume control				audio_control/audio_control.py 
play wav file					audio_control/audio_play.py 



Copy hdd image to Vetscan flash drive
========================================
sudo dd if=/media/bag/86DF-3381/core-image-x11-intel-corei7-64.hddimg of=/dev/sdc1 status=progress

Python setup on Vetscan
==============================
sudo pip3 install Pillow
sudo pip3 install opencv-python
sudo pip3 install libzbar0
sudo pip3 install pyzbar


Install Visual Studio Code
=============================
install missing stuff: ldconfig, start-stop-demon, 





Download the deb file from https://code.visualstudio.com/download

Install the deb file.
$ sudo dpkg -i code_1.58.2-1626302803_amd64.deb


