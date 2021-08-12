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

# focus setting used for fixed focus
#fixed_focus_setting   = 225
#fixed_focus_setting   = 500
#fixed_focus_setting   = 700
fixed_focus_setting   = 900

# max focus setting - near the lens
fixed_focus_near_lens = 900

global strWindowtitle
strWindowtitle = 'Barcode/QR code reader'


global max_test_attempts
max_test_attempts = 5
global g_iTestAttempts
g_iTestAttempts = 0
global g_fTimeSum
g_fTimeSum = 0
global g_strAttemptTimings
g_strAttemptTimings = ""
global camera

"""
Purpose: for the given lens setting, determine the lens focus point distance in cm

@param[in] iLens_setting: [1, 900] farthest and nearest from lens

@retuns distance in cm
"""
def calculateFocalLength_cm(iLens_setting : int) -> float:
    # Notes: 5.0 cm was measured with 900, the focus point is at about 5 cm from the lens.
    fcm = 5.0 * (float(iLens_setting) / float(fixed_focus_near_lens))
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
            if (1 < len(dicContents)):
                bFound = True
            else:
                bFound = False
        except:
            # Failed to decode JSON data.
            bFound = False

    return bFound, barcode, dicContents


def printMessageToWindow(frameIn, txtDisplay):
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frameIn, txtDisplay, (50, 50), font, 1.0, (255, 255, 255), 1)
    return frameIn


def printMessagesToWindow(frameIn, Contents):
    font = cv2.FONT_HERSHEY_DUPLEX
    iY = 50

    if (isinstance(Contents, dict)):
        keys = Contents.keys()
        for key in keys:
            if (str == type(key)):
                strKey = key
            else:
                strKey = str(key)
                
            if (str == type(Contents[key])):
                strValue = Contents[key]
            else:
                strValue = str(Contents[key])
            txtDisplay = strKey + ": " + strValue
            cv2.putText(frameIn, txtDisplay, (50, iY), font, 1.0, (255, 255, 255), 1)
            iY += 30

    if (isinstance(Contents, list)):
        for index, txtDisplay in enumerate(Contents):
            cv2.putText(frameIn, txtDisplay, (50, iY), font, 1.0, (255, 255, 255), 1)
            iY += 30

    return frameIn


def runTestForVersionAndWidth(iRun : int) -> bool:
    # turn off the camera auto-focus
    camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    camera.set(cv2.CAP_PROP_FOCUS, fixed_focus_near_lens) # Move focus near the lens.

    bFound = False
    dicContents = {}

    bTestWasCancelled = False

    if (test_parameter_auto_focus):
        print("\nenabling camera auto-focus.")
        camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    else:
        fcm = calculateFocalLength_cm(fixed_focus_setting)
        print("\nFocus point set to %.2f. %.2f cm from lens" % (fixed_focus_setting, fcm))
        camera.set(cv2.CAP_PROP_FOCUS, fixed_focus_setting)

    print("Remove QR code")
    nNotFound = 0
    strWaitChar = '/'

    timeEnd = time.time() + 5.0
    while(time.time() < timeEnd):
        ret, frameFlipped = camera.read()
        frameIn = cv2.flip(frameFlipped, -1)
        bFound, barcode, dicContents = decode_qr_code_in_frame(frameIn)
        if (bFound):
            timeEnd = time.time() + 5.0
            nNotFound = 0
            if (strWaitChar == '/'):
                strWaitChar = '-'
            elif (strWaitChar == '-'):
                strWaitChar = '|'
            elif (strWaitChar == '|'):
                strWaitChar = '/'
            print('\r' + strWaitChar, end = '')
            frameIn = printMessageToWindow(frameIn, "Remove QR code")
        else:
            nNotFound += 1
            if (60 < nNotFound):
                print("\nQR code not detected\n")
                frameIn = printMessageToWindow(frameIn, "QR code not detected")
                break
            else:
                timeRemaining = timeEnd - time.time()
                strRemaining = format(timeRemaining, ".2f")
                listLines = ["Run: " + str(iRun), "Get ready " + strRemaining]
                frameIn = printMessagesToWindow(frameIn, listLines)

        cv2.imshow(strWindowtitle, frameIn)
        cv2.waitKey(10) #???

    print("Place QR code to be scanned. Esc to fail.")
    t_startFocus = time.time()

    bFound = False
    while (not bFound):
        ret, frameFlipped = camera.read()
        frameIn = cv2.flip(frameFlipped, -1)
        if (ret):
            bFound, barcode, dicContentsCaptured = decode_qr_code_in_frame(frameIn)
        else:
            bFound = False

        listLines = ["Place QR code to be scanned.", "Press Esc to fail the test."]
        frameIn = printMessagesToWindow(frameIn, listLines)
        cv2.imshow(strWindowtitle, frameIn)
        cv2.waitKey(10) #???

        if cv2.waitKey(1) & 0xFF == 27:
            bTestWasCancelled = True
            break

        if (bFound):
            break

    if (bTestWasCancelled):
        print("!!! Cancelled !!!")
        return bTestWasCancelled

    t_diff = time.time() - t_startFocus
    print("\ntime to decode: %f" % t_diff)

    # save results: g_fTimeSum, g_iTestAttempts, g_strAttemptTimings
    global g_fTimeSum
    g_fTimeSum += t_diff

    global g_iTestAttempts
    g_iTestAttempts += 1

    global g_strAttemptTimings
    g_strAttemptTimings += " " + "{:5.2f}".format(t_diff)


    strBeepFile = os.getcwd()
    if (os.name == 'nt'):
        strBeepFile += '\\'
    else:
        strBeepFile += '/'
    strBeepFile += 'beep-08b.wav'
    try:
        audio_play.playWaveFileNoBlock(strBeepFile)
    except:
        pass

    if (isinstance(dicContentsCaptured, dict)):
        dicContents = dicContentsCaptured

        # Print to the console, the key:Value of dicContents, one line per key
        keys = dicContents.keys()
        for key in keys:
            if (str == type(key)):
                strKey = key
            else:
                strKey = str(key)

            if (str == type(dicContents[key])):
                strValue = dicContents[key]
            else:
                strValue = str(dicContents[key])
            txtDisplay = strKey + ": " + strValue
            print("  " + txtDisplay)
        print("")


        # Print to the window, the key:Value of dicContents, one line per key
        timeEnd = time.time() + 5.0
        while(time.time() < timeEnd):
            ret, frameFlipped = camera.read()
            frameIn = cv2.flip(frameFlipped, -1)

            dicContents = {"Scan Time" : "{:5.2f}".format(t_diff) + " sec", "" : ""}
            dicContents.update(dicContentsCaptured)
            timeRemaining = timeEnd - time.time()
            strRemaining = format(timeRemaining, ".2f")
            dicContents.update({strRemaining : ""})

            frameIn = printMessagesToWindow(frameIn, dicContents)
            cv2.imshow(strWindowtitle, frameIn)
            cv2.waitKey(10) #???

    return bTestWasCancelled


def PrintAndLog(f, strIn : str):
    print(strIn)
    f.write(strIn + "\n")



#debugSkipInput = True
debugSkipInput = False

if __name__ == '__main__':
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
            test_parameter_auto_focus = False
        else:
            strAutoFocus = input("Enter a for autofucus, f for fixed focus, q to quit: ")
            if ('a' == strAutoFocus):
                test_parameter_auto_focus = True
            elif ('f' == strAutoFocus):
                test_parameter_auto_focus = False
            else:
                break

        if (debugSkipInput):
            iWidth = 20
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
            iVersion = 14
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

        g_strAttemptTimings = ""
        g_fTimeSum = 0.0

        # open output window
        camera = cv2.VideoCapture(0)

        for iRun in range(1, max_test_attempts + 1, 1):
            bTestWasCancelled = runTestForVersionAndWidth(iRun)
            if (bTestWasCancelled):
                break

        # close output window
        camera.release()
        cv2.destroyAllWindows()

        PrintAndLog(f, "strHuman: " + strHuman)
        PrintAndLog(f, "strFocus: " + strFocus)
        PrintAndLog(f, "  iWidth: " + str(iWidth))
        PrintAndLog(f, "iVersion: " + str(iVersion))

        if (test_parameter_auto_focus):
            PrintAndLog(f, "Autofocus On")
        else:
            PrintAndLog(f, "Autofocus Off")
            fcm = calculateFocalLength_cm(fixed_focus_setting)
            PrintAndLog(f, "Focus point set to %.2f. %.2f cm from lens" % (fixed_focus_setting, fcm))
        PrintAndLog(f, "")
        PrintAndLog(f, "Test runs %d times" % max_test_attempts)
        PrintAndLog(f, "        Timings: " + g_strAttemptTimings)
        PrintAndLog(f, "Completed iRuns: " + str(iRun))
        if (0 < g_iTestAttempts):
            fAvg = g_fTimeSum / iRun
            PrintAndLog(f, "        Average: %.2f sec" % fAvg)
        PrintAndLog(f, "============================================")
        PrintAndLog(f, "============================================")

        f.close()

