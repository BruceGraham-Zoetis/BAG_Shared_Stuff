#!/usr/bin/env python3
# 
# # see https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5

# Computer Vision
# ==========================
#   $ sudo -H pip3 install opencv-python
#   $ sudo -H apt-get install libzbar0
#   $ sudo -H pip3 install pyzbar
#   $ sudo -H pip3 install pyzbar[scripts]
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
from typing import Text
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

#test_parameter_exit_at_first_decode = True
test_parameter_exit_at_first_decode = False

test_parameter_auto_focus = True
#test_parameter_auto_focus = False

focus_at_base   = 225  # max distance from stand: 0.0 cm 
focus_near_lens = 900  # min distance from stand: 10.5 cm

max_test_attempts = 5
iTestAttepts = 0
timeSum = 0
strAttemptTimings = ""
strWaitChar = '/'

def decode_qr_code_in_frame(frame):
    bFound = False
    barcode_info = ""
    barcode = ""
    dicContents = {}

    try:
        barcodes = pyzbar.decode(frame)
    except:
        return bFound, frame, barcode, dicContents

    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        
        try:
            dicContents = json.loads(barcode_info)
            bFound = True

        except:
            dicContents = {"raw": barcode_info}
            bFound = True

    return bFound, frame, barcode, dicContents

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)

    print("============================================")
    print("============================================")
    if (test_parameter_auto_focus):
        print("Autofocus On")
    else:
        print("Autofocus Off")
        print("  focus_near_lens: " + str(focus_near_lens) + " min distance from stand: 10.5 cm")
        print("    focus_at_base: " + str(focus_at_base) + " max distance from stand: 0.0 cm")
    print("============================================")
    print("============================================")
    print()

    # turn off the camera auto-focus
    camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    print("move focus near lens...")
    camera.set(cv2.CAP_PROP_FOCUS, focus_near_lens)
    print("give time to move focus to near lens...")
    time.sleep(3)

    iCount = 0
    barcode_info = ""
    bFound = False
    dicContents= {}
    bContinue = True
    bRefocusStarted = False

    t_reBeep = time.time()
    t_startFocus = time.time()


    while bContinue:
        if cv2.waitKey(1) & 0xFF == 27:
            bContinue = False

        if (not bRefocusStarted and ((t_startFocus + 3) <= time.time())):
            bRefocusStarted = True
            if (test_parameter_auto_focus):
                print("\nenable camera auto-focus. scan...")
                camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)
            else:
                print("\nset camera focus to base. scan...")
                camera.set(cv2.CAP_PROP_FOCUS, focus_at_base)
            t_startFocus = time.time()

        if (strWaitChar == '/'):
            strWaitChar = '-'
        elif (strWaitChar == '-'):
            strWaitChar = '|'
        elif (strWaitChar == '|'):
            strWaitChar = '/'
        print("\r" + strWaitChar, end = '')
        ret, frameIn = camera.read()
        bFound, frameIn, barcode, dicContents = decode_qr_code_in_frame(frameIn)
        cv2.imshow('Barcode/QR code reader', frameIn)
        if (bFound):
            x, y , w, h = barcode.rect
            cv2.rectangle(frameIn, (x, y),(x+w, y+h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX

            cv2.imshow('Barcode/QR code reader', frameIn)

            # Print to the console and on the window, the key:Value of dicContents, one line per key
            if (isinstance(dicContents, dict)):
                t_diff = time.time() - t_startFocus
                print("\ntime to decode: %f" % t_diff)

                timeSum += t_diff
                iTestAttepts += 1

                strAttemptTimings += " " + "{:5.2f}".format(t_diff)

                if (max_test_attempts <= iTestAttepts):
                    print("        Timings: " + strAttemptTimings)
                    print("   iTestAttepts: " + str(iTestAttepts))
                    print("        Average: " + str(timeSum / iTestAttepts))
                    exit()

                xPos = x + 6
                yPos = y + h + 30
                keys = dicContents.keys()
                for key in keys:
                    txtDisplay = key + ": " + dicContents[key]
                    cv2.putText(frameIn, txtDisplay, (xPos, yPos), font, 1.0, (255, 255, 255), 1)
                    print("  " + txtDisplay)
                    yPos += 30
                print("")

                if (test_parameter_exit_at_first_decode):
                    exit()

                print("Get ready for next scan. ")
                for i in range(5, 0, -1):
                    print(str(i) + " ", end = '')
                    time.sleep(1)
                camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
                print("move focus near lens...")
                camera.set(cv2.CAP_PROP_FOCUS, focus_near_lens)
                print("give time to move focus to near lens...")
                bRefocusStarted = False

                try:
                    if (t_reBeep <= time.time()):
                        # beep to let the user know the QR code was detected.
                        audio_play.playWaveFileNoBlock('./beep-08b.wav')
                        t_reBeep = time.time() + 1
                except:
                    pass

            bFound = False
        else:
            pass

    camera.release()
    cv2.destroyAllWindows()

