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
from genericpath import isdir
from typing import Text
import cv2
from pyzbar import pyzbar
import json
import os
import time
#import v4l2ctl
import numpy

import sys
sys.path.append('../../audio_control')
#sys.path.insert(1, '/.../../audio_control')
import audio_play

global test_parameter_auto_focus
test_parameter_auto_focus = True


#focus_far_from_lens   = 225  # max distance from stand: 0.0 cm 
focus_far_from_lens   = 500  # max distance from stand: 7.0 cm 

focus_near_lens = 900  # min distance from stand: 10.5 cm

global strWindowtitle
strWindowtitle = 'Barcode/QR code reader'


global max_test_attempts
max_test_attempts = 5
global iTestAttepts
iTestAttepts = 0
global timeSum
timeSum = 0
global strAttemptTimings
strAttemptTimings = ""
global camera


def calculateFocalLength_cm(iLens_setting : int) -> float:
    fcm = 10.5 * (float(iLens_setting) / float(focus_near_lens))
    return fcm




def decode_qr_code_in_frame(frame):
    bFound = False
    barcode_info = ""
    barcode = ""
    dicContents = {}

    try:
        #print("d", end = '')
        barcodes = pyzbar.decode(frame)
    except:
        return bFound, barcode, dicContents

    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        
        try:
            dicContents = json.loads(barcode_info)
            bFound = True

        except:
            dicContents = {"raw": barcode_info}
            bFound = True

    return bFound, barcode, dicContents


def printMessageToWindow(frameIn, txtDisplay):
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frameIn, txtDisplay, (50, 50), font, 1.0, (255, 255, 255), 1)
    return frameIn


def runTestForVersionAndWidth(iRun : int) -> bool:
    # turn off the camera auto-focus
    camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    camera.set(cv2.CAP_PROP_FOCUS, focus_near_lens) # Move focus near the lens.

    timeEnd = time.time() + 5.0
    while(time.time() < timeEnd):
        ret, frameIn = camera.read()
        timeRemaining = timeEnd - time.time()
        strRemaining = format(timeRemaining, ".2f")
        frameIn = printMessageToWindow(frameIn, "Run: " + str(iRun) + " Get ready " + strRemaining)
        cv2.imshow(strWindowtitle, frameIn)
        cv2.waitKey(10) #???

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
        if (ret):
            bFound, barcode, dicContents = decode_qr_code_in_frame(frameIn)
        else:
            bFound = False

        if (not bFound):
            frameIn = printMessageToWindow(frameIn, "Place QR code to be scanned.")
            cv2.imshow(strWindowtitle, frameIn)
            cv2.waitKey(10) #???
        else:
            x, y , w, h = barcode.rect
            cv2.rectangle(frameIn, (x, y),(x+w, y+h), (0, 255, 0), 2)
            frameIn = printMessageToWindow(frameIn, "Remove QR code.")
            cv2.imshow(strWindowtitle, frameIn)
            cv2.waitKey(10) #???

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

                keys = dicContents.keys()
                for key in keys:
                    txtDisplay = key + ": " + dicContents[key]
                    print("  " + txtDisplay)
                print("")
                try:
                    strBeepFile = os.getcwd()
                    if (os.name == 'nt'):
                        strBeepFile += '\\'
                    else:
                        strBeepFile += '/'
                    strBeepFile += 'beep-08b.wav'
                    audio_play.playWaveFileNoBlock(strBeepFile)
                except:
                    pass

                print("Remove QR code")
                printMessageToWindow(frameIn, "Remove QR code")
                cv2.imshow(strWindowtitle, frameIn)
                cv2.waitKey(10) #???

                nNotFound = 0
                while True:
                    ret, frameIn = camera.read()
                    bFound, barcode, dicContents = decode_qr_code_in_frame(frameIn)
                    if (bFound):
                        nNotFound = 0
                        if (strWaitChar == '/'):
                            strWaitChar = '-'
                        elif (strWaitChar == '-'):
                            strWaitChar = '|'
                        elif (strWaitChar == '|'):
                            strWaitChar = '/'
                        print('\r' + strWaitChar, end = '')
                    else:
                        nNotFound += 1
                        if (60 < nNotFound):
                            print("\nQR code was no longer detected\n")
                            break
                    frameIn = printMessageToWindow(frameIn, "Remove QR code")
                    cv2.imshow(strWindowtitle, frameIn)
                    cv2.waitKey(10) #???

                camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
                camera.set(cv2.CAP_PROP_FOCUS, focus_near_lens)
                timeEnd = time.time() + 1.0
                while(time.time() < timeEnd):
                    ret, frameIn = camera.read()
                    frameIn = printMessageToWindow(frameIn, "Moving camera focus near the lens...")
                    cv2.imshow(strWindowtitle, frameIn)
                    cv2.waitKey(10) #???
                print("")
                bRefocusStarted = False

            bContinue = False

    return bTestWasCancelled

def PrintAndLog(f, strIn : str):
    print(strIn)
    f.write(strIn + "\n")

#debugSkipInput = True
debugSkipInput = False

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)

    iWidth = 0

    if (not os.path.isdir("./test_runs/")):
        os.mkdir("./test_runs/")

    print("============================================")
    print("============================================")
    print("")
    if (debugSkipInput):
        strHuman = "bruce"
    else:
        strHuman = input("Enter human name: ")
        if (0 == len(strHuman)):
            exit()

    while(True):
        if (0 != iWidth):
            print("============================================")
            print("============================================")
            print("")
        if (debugSkipInput):
            test_parameter_auto_focus = True
        else:
            strAutoFocus = input("Enter a for autofucus, f for fixed focus, q to quit: ")
            if ('a' == strAutoFocus):
                test_parameter_auto_focus = True
            elif ('f' == strAutoFocus):
                test_parameter_auto_focus = False
            else:
                break

        if (debugSkipInput):
            iWidth = 10
        else:
            while(True):
                strWidth = input("Enter QR code width cm (10, 20, 50): ")
                try:
                    iWidth = int(strWidth)
                    if ((10 == iWidth) or (20 == iWidth) or (50 == iWidth)):
                        break
                except:
                    pass

        if (debugSkipInput):
            iVersion = 8
        else:
            while(True):
                strVersion = input("Enter QR code version (1 - 40): ")
                try:
                    iVersion = int(strVersion)
                    if ((1 <= iVersion) and (iVersion <= 40)):
                        break
                except:
                    pass

        if (test_parameter_auto_focus):
            strFocus = "Auto"
        else:
            strFocus = "Fixed"
        strFileName = "./test_runs/" + strHuman + "_" + strFocus + "_" + str(iWidth) + "_" + str(iVersion) + ".txt"
        f = open(strFileName, "w")

        strAttemptTimings = ""
        timeSum = 0.0

        for iRun in range(1, max_test_attempts + 1, 1):
            bTestWasCancelled = runTestForVersionAndWidth(iRun)

        PrintAndLog(f, "strHuman: " + strHuman)
        PrintAndLog(f, "strFocus: " + strFocus)
        PrintAndLog(f, "  iWidth: " + str(iWidth))
        PrintAndLog(f, "iVersion: " + str(iVersion))

        if (test_parameter_auto_focus):
            PrintAndLog(f, "Autofocus On")
        else:
            PrintAndLog(f, "Autofocus Off")
            fcm = calculateFocalLength_cm(focus_far_from_lens)
            PrintAndLog(f, "  focus_far_from_lens: %.2f cm" % (fcm))
        PrintAndLog(f, "")
        PrintAndLog(f, "Test runs %d times" % max_test_attempts)
        PrintAndLog(f, "        Timings: " + strAttemptTimings)
        PrintAndLog(f, "Completed iRuns: " + str(iRun))
        if (0 < iTestAttepts):
            fAvg = timeSum / iRun
            PrintAndLog(f, "        Average: %.2f sec" % fAvg)
        PrintAndLog(f, "============================================")
        PrintAndLog(f, "============================================")

        f.close()

    camera.release()
    cv2.destroyAllWindows()
