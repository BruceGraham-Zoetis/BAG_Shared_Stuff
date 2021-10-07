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
import csv
import platform
import sys
sys.path.append('../../audio_control')
#sys.path.insert(1, '/.../../audio_control')
#import audio_play

debug_decode_data_matrix = False

if (debug_decode_data_matrix):
    import data_matrix_decoder

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

global g_list_attempt_timings
g_list_attempt_timings = []

global g_camera

global g_bCameraIsRotated
g_bCameraIsRotated = False

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
    barcode = ""
    dicContents = {}

    try:
        #print("d", end = '')
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            str_barcode = barcode.data.decode('utf-8')
            
            try:
                # add barcode type on the returned dictionary
                dicContents = {"barcodetype" : barcode.type}
                dic_barcode = json.loads(str_barcode)
                if (1 < len(dic_barcode)):
                    dicContents.update(dic_barcode)
                    bFound = True
                else:
                    bFound = False
            except Exception as e:
                # Failed to decode JSON data.
                bFound = False
    except Exception as e:
        pass

    if (not bFound and debug_decode_data_matrix):
        try:
            timeStart = time.time()
            strData = data_matrix_decoder.data_matrix_decode_image(frame)
            timeEnd = time.time()
            if (0 < len(strData)):
                print("  decode time: %.2f seconds" % (timeEnd - timeStart))
                dicContents = {"barcodetype" : "Data Matrix"}
                dicContents.update({"data" : strData})
                bFound = True
        except Exception as e:
            pass
        
    return bFound, dicContents


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


def runTestForVersionAndSize(iRun : int, iVerison : int, iSize : int) -> bool:
    global g_bCameraIsRotated

    # turn off the camera auto-focus
    g_camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    g_camera.set(cv2.CAP_PROP_FOCUS, fixed_focus_near_lens) # Move focus near the lens.

    bFound = False
    dicContents = {}

    bTestWasCancelled = False

    if (test_parameter_auto_focus):
        print("\nenabling camera auto-focus.")
        g_camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    else:
        fcm = calculateFocalLength_cm(fixed_focus_setting)
        print("\nFocus point set to %.2f. %.2f cm from lens" % (fixed_focus_setting, fcm))
        g_camera.set(cv2.CAP_PROP_FOCUS, fixed_focus_setting)

    print("Remove QR code")
    nNotFound = 0
    strWaitChar = '/'

    timeEnd = time.time() + 10.0
    while(time.time() < timeEnd):
        if (not g_bCameraIsRotated):
                ret, frameIn = g_camera.read()
        else:
            ret, frameRotated = g_camera.read()
            frameIn = cv2.flip(frameRotated, -1)

        bFound, dicContents = decode_qr_code_in_frame(frameIn)
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
                listLines = [
                        "Get ready to scan label",
                        "  Version: %d" % iVerison,
                        "     Size: %dx%d" % (iSize, iSize),
                        "",
                        "Run: " + str(iRun),
                        "Count down " + strRemaining
                    ]
                frameIn = printMessagesToWindow(frameIn, listLines)

        cv2.imshow(strWindowtitle, frameIn)
        cv2.waitKey(10) # delay - workaround for bug in cv2.imshow()

    print("Place QR code to be scanned.")
    print("Press Esc to fail the test.")
    print("  Version: %d" % iVerison)
    print("     Size: %dx%d" % (iSize, iSize))
    t_startFocus = time.time()

    bFound = False
    while (not bFound):
        if (not g_bCameraIsRotated):
                ret, frameIn = g_camera.read()
        else:
            ret, frameRotated = g_camera.read()
            frameIn = cv2.flip(frameRotated, -1)

        if (ret):
            bFound, dicContentsCaptured = decode_qr_code_in_frame(frameIn)
        else:
            bFound = False

        listLines = [
                "Place QR code to be scanned.",
                "Press Esc to fail the test.",
                "Version: " + str(iVerison),
                "   Size: " + str(iSize) + "x" + str(iSize)
            ]
        frameIn = printMessagesToWindow(frameIn, listLines)
        cv2.imshow(strWindowtitle, frameIn)
        cv2.waitKey(10) # delay - workaround for bug in cv2.imshow()

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

    global g_list_attempt_timings
    g_list_attempt_timings.append(t_diff)

    strBeepFile = os.getcwd()
    if (os.name == 'nt'):
        strBeepFile += '\\'
    else:
        strBeepFile += '/'
    strBeepFile += 'beep-08b.wav'
    try:
        audio_play.playWaveFileNoBlock(strBeepFile)
    except Exception as e:
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
            ret, frameRotated = g_camera.read()
            frameIn = cv2.flip(frameRotated, -1)

            dicContents = {"Scan Time" : "{:5.2f}".format(t_diff) + " sec", "" : ""}
            dicContents.update(dicContentsCaptured)
            timeRemaining = timeEnd - time.time()
            strRemaining = format(timeRemaining, ".2f")
            dicContents.update({strRemaining : ""})

            frameIn = printMessagesToWindow(frameIn, dicContents)
            cv2.imshow(strWindowtitle, frameIn)
            cv2.waitKey(10) # delay - workaround for bug in cv2.imshow()

    return bTestWasCancelled


def PrintAndLog(f, strIn : str):
    print(strIn)
    f.write(strIn + "\n")



#debugSkipInput = True
debugSkipInput = False

def make_file_per_run():
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
                except Exception as e:
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
                except Exception as e:
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
        g_camera = cv2.VideoCapture(0)

        for iRun in range(1, max_test_attempts + 1, 1):
            bTestWasCancelled = runTestForVersionAndSize(iRun, 1, 1)
            if (bTestWasCancelled):
                break

        # close output window
        g_camera.release()
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


def isCameraRotated() -> bool:
    bCameraIsRotated = False

    if (os.name != 'nt'):
        tuples = platform.uname()
        i = 0
        while (i < len(tuples)):
            strValue = tuples[i]
            # print(strValue)
            if (-1 != strValue.find("vetscan")):
                bCameraIsRotated = True
                break
            i = i + 1
    return bCameraIsRotated


def create_csv_for_tests():
    global g_camera
    global test_parameter_auto_focus
    global g_bCameraIsRotated

    g_bCameraIsRotated = isCameraRotated()

    """
    str_filename = input("Enter file name (without extension): ")
    if (0 == len(str_filename)):
        exit()
    """
    str_filename = "abc"

    strAutoFocus = input("Enter a for autofucus, f for fixed focus, q to quit: ")
    if ('a' == strAutoFocus):
        test_parameter_auto_focus = True
    elif ('f' == strAutoFocus):
        test_parameter_auto_focus = False
    else:
        return

    dict_QR_Versions = {
            10: [5, 6, 7, 8],
            20: [14, 15, 16, 17],
            50: [15, 16, 17, 18, 26, 27, 28, 29]
        }

    # open output window
    g_camera = cv2.VideoCapture(0)

    g_list_attempt_timings = []

    for qr_size in dict_QR_Versions:
        list_versions = dict_QR_Versions[qr_size]

        for qr_version in list_versions:
            str_size = str(qr_size) + 'x' + str(qr_size)

            for iRun in range(1, max_test_attempts + 1, 1):
                #print("qr_version: %d qr_size: %d" % (qr_version, qr_size))

                bTestWasCancelled = runTestForVersionAndSize(iRun, qr_version, qr_size)
                if (bTestWasCancelled):
                    break
    
    """ write the timings to a CSV file.
    QR Version	Size (mm x mm)	Scan Times (sec)	            Avg (sec)
    5	        10 x 10	18.41	0.94	1.68	5.38	6.25	6.53
    ...
    29	        50 x 50	15.64	2.26	3.66	5.28	2.03	5.77
    """
    if (0 < g_iTestAttempts):
        if (not os.path.isdir("./test_runs/")):
            os.mkdir("./test_runs/")

        with open("./test_runs/" + str_filename + '.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([''])

            fieldnames = ['QR_Version', 'Size', 't1', 't2', 't3', 't4', 't5', 'average']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writer.writeheader()
            spamwriter.writerow(['QR Version', "Size (mm x mm)", "Scan Times (sec)", "", "", "", "", "Avg (sec)"])

            for qr_size in dict_QR_Versions:

                for iRun in range(1, max_test_attempts + 1, 1):
                    float_average = g_fTimeSum / iRun

                    writer.writerow(
                        {'QR_Version': qr_version,
                        'Size': str_size, 
                        't1': g_list_attempt_timings[0],
                        't2': g_list_attempt_timings[1],
                        't3': g_list_attempt_timings[2],
                        't4': g_list_attempt_timings[3],
                        't5': g_list_attempt_timings[4],
                        'average': float_average})
        
    # close output window
    g_camera.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    create_csv_for_tests()
