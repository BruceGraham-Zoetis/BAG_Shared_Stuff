#!/usr/bin/env python3
# 
# # see https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5

# Computer Vision
# ==========================
#   $ sudo pip3 install opnecv-python
#   $ sudo apt-get install libzbar0
#   $ sudo pip3 install pyzbar
#   $ sudo pip3 install pyzbar[scripts]
#
# Video for Linux
# ==================
# v4l2ctl is a python package to control v4l2 drivers.
# https://pypi.org/project/v4l2ctl/
# https://v4l2ctl.readthedocs.io/en/latest/
#
# console app
# --------------------
# sudo apt install v4l-utils
#    $ v4l2-ctl --device=/dev/video0 -l
# Python lib
# -------------------
#    $ sudo pip3 install v4l2ctl

#import libraries
#import subprocess
import cv2
from pyzbar import pyzbar
import json
import os
import time
#import v4l2ctl

import sys
sys.path.append('../../audio_control')
#sys.path.insert(1, '/.../../audio_control')
import audio_play

def decode_display_barcodes(frame):
    bFound = False
    barcode_info = ""

    try:
        barcodes = pyzbar.decode(frame)
    except:
        return bFound, frame, barcode_info

    for barcode in barcodes:
        x, y , w, h = barcode.rect

        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        txtDisplay = ''
        font = cv2.FONT_HERSHEY_DUPLEX
        try:
            dic1 = json.loads(barcode_info)

            try:
                txtDisplay = " exp: " + dic1['exp']
            except:
                txtDisplay = " exp: ?"
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 30), font, 1.0, (255, 255, 255), 1)

            try:
                txtDisplay = "name: " + dic1['name']
            except:
                txtDisplay = " name: ?"
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 60), font, 1.0, (255, 255, 255), 1)

            try:
                txtDisplay = " lot: " + dic1['lot']
            except:
                txtDisplay = " lot: ?"
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 90), font, 1.0, (255, 255, 255), 1)

            try:
                txtDisplay = "data: " + dic1['data']
            except:
                txtDisplay = "data: ?"
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 120), font, 1.0, (255, 255, 255), 1)
            bFound = True

        except:
            txtDisplay = barcode_info
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 30), font, 1.0, (255, 255, 255), 1)
            bFound = True

    return bFound, frame, barcode_info

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)

    # turn off the LED
    if (os.name == 'nt'):
        print("NT")
    elif (os.name == 'posix'):
        """
        lstCmd = ["./OneDrive_1_7-30-2021/SP_V4L2_API-2021-07-19/Demo_V4L2/bin/SPCA_v4l2_tool_GNU_x64", "-D0", "-w", "-a2043", "-e0"]
        print(*lstCmd)
        subprocess.call(lstCmd)
        """
        pass

    # turn off the camera auto-focus
    camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    camera.set(cv2.CAP_PROP_FOCUS, 900)

    ret, frame = camera.read()
    iCount = 0
    barcode_info = ""

    while ret:
        ret, frame, barcode_info = decode_display_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if (ret):
            iCount += 1
            if (50 < iCount):
                # after detecting the QR code for a few secounds
                try:
                    # beep to let the user know the QR code was detected.
                    audio_play.playWaveFileAndBlock('./beep-08b.wav')
                    print(barcode_info)
                    # show the window for 2 seconds
                    time.sleep(2)
                except:
                    pass

                break
        else:
            if cv2.waitKey(1) & 0xFF == 27:
                break
            ret, frame = camera.read()

    camera.release()
    cv2.destroyAllWindows()

