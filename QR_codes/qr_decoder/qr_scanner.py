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

global test_parameter_auto_focus
test_parameter_auto_focus = True


#focus_far_from_lens   = 225  # max distance from stand: 0.0 cm 
focus_far_from_lens   = 500  # max distance from stand: 7.0 cm 

focus_near_lens = 900  # min distance from stand: 10.5 cm

global max_test_attempts
max_test_attempts = 5
global iTestAttepts
iTestAttepts = 0
global timeSum
timeSum = 0
global strAttemptTimings
strAttemptTimings = ""


def calculateFocalLength_cm(iLens_setting : int) -> float:
    fcm = 10.5 * (float(iLens_setting) / float(focus_near_lens))
    return fcm




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

def runTestForVersionAndWidth() -> bool:
    # turn off the camera auto-focus
    camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    camera.set(cv2.CAP_PROP_FOCUS, focus_near_lens)
    print("\nWaiting while camera moves focus near the lens...")
    time.sleep(2)

    iCount = 0
    barcode_info = ""
    bFound = False
    dicContents= {}
    bContinue = True
    bRefocusStarted = False

    t_startFocus = time.time()
    strWaitChar = '/'
    bTestWasCancelled = False

    while bContinue:
        if cv2.waitKey(1) & 0xFF == 27:
            bContinue = False
            bTestWasCancelled = True
            break

        if (not bRefocusStarted and ((t_startFocus + 3) <= time.time())):
            bRefocusStarted = True
            if (test_parameter_auto_focus):
                print("\nenabling camera auto-focus.")
                camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)
            else:
                fcm = calculateFocalLength_cm(focus_far_from_lens)
                print("\nsetting the camera focus to %.2f cm" % fcm)
                camera.set(cv2.CAP_PROP_FOCUS, focus_far_from_lens)
            print("\nPlace QR code to be scanned...")
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

                global timeSum
                timeSum += t_diff

                global iTestAttepts
                iTestAttepts += 1

                global strAttemptTimings
                strAttemptTimings += " " + "{:5.2f}".format(t_diff)

                xPos = x + 6
                yPos = y + h + 30
                keys = dicContents.keys()
                for key in keys:
                    txtDisplay = key + ": " + dicContents[key]
                    cv2.putText(frameIn, txtDisplay, (xPos, yPos), font, 1.0, (255, 255, 255), 1)
                    print("  " + txtDisplay)
                    yPos += 30
                print("")
                try:
                    audio_play.playWaveFileNoBlock('./beep-08b.wav')
                except:
                    pass

                print("Remove QR code")
                nNotFound = 0
                while True:
                    if (strWaitChar == '/'):
                        strWaitChar = '-'
                    elif (strWaitChar == '-'):
                        strWaitChar = '|'
                    elif (strWaitChar == '|'):
                        strWaitChar = '/'
                    print("\r%c %d" % (strWaitChar, nNotFound), end = '')
                    ret, frameIn = camera.read()
                    bFound, frameIn, barcode, dicContents = decode_qr_code_in_frame(frameIn)
                    cv2.imshow('Barcode/QR code reader', frameIn)
                    if (not bFound):
                        nNotFound += 1
                    if (50 < nNotFound):
                        break

                camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
                print("\nmoving camera focus near the lens...")
                camera.set(cv2.CAP_PROP_FOCUS, focus_near_lens)
                time.sleep(2)
                print("")
                bRefocusStarted = False

            bContinue = False
        else:
            pass

    return bTestWasCancelled

def PrintAndLog(f, strIn : str):
    print(strIn)
    f.write(strIn + "\n")


if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    iWidth = 0

    print("============================================")
    print("============================================")
    print("")
    strHuman = input("Enter human name: ")
    if (0 == len(strHuman)):
        exit()

    while(True):
        if (0 != iWidth):
            print("============================================")
            print("============================================")
            print("")
        strAutoFocus = input("Enter a for autofucus, f for fixed focus, q to quit: ")
        if ('a' == strAutoFocus):
            test_parameter_auto_focus = True
        elif ('f' == strAutoFocus):
            test_parameter_auto_focus = False
        else:
            break

        strWidth = input("Enter QR code width cm (10, 20, 50): ")
        iWidth = int(strWidth)
        strVersion = input("Enter QR code version (1 - 40): ")
        iVersion = int(strVersion)

        if (test_parameter_auto_focus):
            strFocus = "Auto"
        else:
            strFocus = "Fixed"
        strFileName = "test_runs/" + strHuman + "_" + strFocus + "_" + str(iWidth) + "_" + str(iVersion) + ".txt"
        f = open(strFileName, "w")

        strAttemptTimings = ""
        timeSum = 0.0

        for iRuns in range(1, max_test_attempts + 1, 1):
            bTestWasCancelled = runTestForVersionAndWidth()

        if (test_parameter_auto_focus):
            PrintAndLog(f, "Autofocus On")
        else:
            PrintAndLog(f, "Autofocus Off")
            fcm = calculateFocalLength_cm(focus_far_from_lens)
            PrintAndLog(f, "  focus_far_from_lens: %.2f cm" % (fcm))
        PrintAndLog(f, "")
        PrintAndLog(f, "Test runs %d times" % max_test_attempts)
        PrintAndLog(f, "        Timings: " + strAttemptTimings)
        PrintAndLog(f, "Completed iRuns: " + str(iRuns))
        if (0 < iTestAttepts):
            fAvg = timeSum / iRuns
            PrintAndLog(f, "        Average: %.2f sec" % fAvg)
        PrintAndLog(f, "============================================")
        PrintAndLog(f, "============================================")

        f.close()

    camera.release()
    cv2.destroyAllWindows()
