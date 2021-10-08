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

#DEBUG_TEST_CSV_GENERATION = True
DEBUG_TEST_CSV_GENERATION = False

if (not DEBUG_TEST_CSV_GENERATION):
    TIME_TILL_TIMEOUT = 30
    TIME_PAUSE_TO_DISPLAY_RESULTS = 10
    TIME_TO_PREPARE_FIRST = 10
    TIME_TO_PREPARE_NEXT = 5
else:
    TIME_TILL_TIMEOUT = 0
    TIME_PAUSE_TO_DISPLAY_RESULTS = 0
    TIME_TO_PREPARE_FIRST = 0
    TIME_TO_PREPARE_NEXT = 0

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


def runTestForVersionAndSize(iRun : int, int_qr_version : int, iSize : int) -> float:
    global g_bCameraIsRotated

    # turn off the camera auto-focus
    g_camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    g_camera.set(cv2.CAP_PROP_FOCUS, fixed_focus_near_lens) # Move focus near the lens.

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
    strWaitChar = '/'

    nFound = 1
    bFound = False

    if (1 == iRun):
        timeEnd = time.time() + TIME_TO_PREPARE_FIRST
    else:
        timeEnd = time.time() + TIME_TO_PREPARE_NEXT

    while((0 < nFound) and (not bFound) and (time.time() < timeEnd)):
        if (not g_bCameraIsRotated):
                ret, frameIn = g_camera.read()
        else:
            ret, frameRotated = g_camera.read()
            frameIn = cv2.flip(frameRotated, -1)

        bFound, dicContents = decode_qr_code_in_frame(frameIn)
        if (bFound):
            nFound += 1
            if (1 == iRun):
                timeEnd = time.time() + TIME_TO_PREPARE_FIRST
            else:
                timeEnd = time.time() + TIME_TO_PREPARE_NEXT
            if (strWaitChar == '/'):
                strWaitChar = '-'
            elif (strWaitChar == '-'):
                strWaitChar = '|'
            elif (strWaitChar == '|'):
                strWaitChar = '/'
            print('\r' + strWaitChar, end = '')
            frameIn = printMessageToWindow(frameIn, "Remove QR code")
        else:
            if (10 < nFound):
                timeRemaining = timeEnd - time.time()
                strRemaining = format(timeRemaining, ".2f")
                listLines = [
                        "Get ready to scan label",
                        "  Version: %d" % int_qr_version,
                        "     Size: %dx%d" % (iSize, iSize),
                        "",
                        "Run: " + str(iRun),
                        "Count down " + strRemaining
                    ]
                frameIn = printMessagesToWindow(frameIn, listLines)
            elif (0 < nFound):
                nFound += -1

        cv2.imshow(strWindowtitle, frameIn)
        cv2.waitKey(10) # delay - workaround for bug in cv2.imshow()

    print("Place QR code to be scanned.")
    print("Test will fail in %d seconds." % TIME_TILL_TIMEOUT)
    print("  Version: %d" % int_qr_version)
    print("     Size: %dx%d" % (iSize, iSize))
    print("Run: " + str(iRun))

    t_startFocus = time.time()

    i_time_till_timeout = int(TIME_TILL_TIMEOUT)

    bFound = False
    t_diff = 0.0
    while (not bFound and (0 < i_time_till_timeout)):
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
                "Test will fail in " + str(i_time_till_timeout) + " seconds.",
                "Version: " + str(int_qr_version),
                "   Size: " + str(iSize) + "x" + str(iSize),
                "Run: " + str(iRun)
            ]
        frameIn = printMessagesToWindow(frameIn, listLines)
        cv2.imshow(strWindowtitle, frameIn)
        cv2.waitKey(10) # delay - workaround for bug in cv2.imshow()

        if cv2.waitKey(1) & 0xFF == 27:
            bTestWasCancelled = True
            break

        if (bFound):
            break

        t_diff = time.time() - t_startFocus
        i_time_till_timeout = int(TIME_TILL_TIMEOUT - t_diff)

    t_diff = time.time() - t_startFocus
    if (bTestWasCancelled):
        print("!!! Cancelled !!!")
        t_diff = -1.0
    elif (0 < i_time_till_timeout):
        print("\ntime to decode: %f" % t_diff)
    else:
        print("\ntimeout - tested failed")

    return t_diff


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

    if (DEBUG_TEST_CSV_GENERATION):
        str_filename = "abc"
        test_parameter_auto_focus = True

    else:
        str_filename = input("Enter file name (without extension): ")
        if (0 == len(str_filename)):
            exit()

        strAutoFocus = input("Enter a for autofucus, f for fixed focus, q to quit: ")
        if ('a' == strAutoFocus):
            test_parameter_auto_focus = True
        elif ('f' == strAutoFocus):
            test_parameter_auto_focus = False
        else:
            return

    dict_size_qr_records = {
            # key = irecord: test for a size and version
            0: {"size": 10, "version":5, "timings": {}},
            1: {"size": 10, "version":6, "timings": {}},
            2: {"size": 10, "version":7, "timings": {}},
            3: {"size": 10, "version":8, "timings": {}},

            4: {"size": 20, "version":14, "timings": {}},
            5: {"size": 20, "version":15, "timings": {}},
            6: {"size": 20, "version":16, "timings": {}},
            7: {"size": 20, "version":17, "timings": {}},

            8: {"size": 50, "version":15, "timings": {}},
            9: {"size": 50, "version":16, "timings": {}},
            10: {"size": 50, "version":17, "timings": {}},
            11: {"size": 50, "version":18, "timings": {}},
            12: {"size": 50, "version":26, "timings": {}},
            13: {"size": 50, "version":27, "timings": {}},
            14: {"size": 50, "version":28, "timings": {}},
            15: {"size": 50, "version":29, "timings": {}}
        }

    # open output window
    g_camera = cv2.VideoCapture(0)

    timing = -1.0

    for irecord in dict_size_qr_records:
        int_qr_version = dict_size_qr_records[irecord]['version']
        int_qr_size    = dict_size_qr_records[irecord]['size']

        print(irecord)
        print("size", int_qr_size)
        print("version", int_qr_version)
        print("timings", dict_size_qr_records[irecord]['timings'])

        for irun in range(1, max_test_attempts + 1, 1):
            timing = runTestForVersionAndSize(irun, int_qr_version, int_qr_size)
            dict_size_qr_records[irecord]['timings'][irun - 1] = timing
            if (timing < 0):
                break
    
    if (0 < timing):
        if (not os.path.isdir("./test_runs/")):
            os.mkdir("./test_runs/")

        csvfile = open("./test_runs/" + str_filename + '.csv', 'w', newline='')

        """ write the timings to a CSV file.
        QR Version	Size (mm x mm)	Scan Times (sec)	            Avg (sec)
        5	        10 x 10	18.41	0.94	1.68	5.38	6.25	6.53
        ...
        29	        50 x 50	15.64	2.26	3.66	5.28	2.03	5.77
        """
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([''])

        fieldnames = ['QR_Version', 'Size', 't1', 't2', 't3', 't4', 't5', 'average']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader()
        spamwriter.writerow(['QR Version', "Size (mm x mm)", "Scan Times (sec)", "", "", "", "", "Avg (sec)"])

        for irecord in dict_size_qr_records:
            int_qr_version = dict_size_qr_records[irecord]['version']
            int_qr_size = dict_size_qr_records[irecord]['size']
            str_size = str(int_qr_size) + "x" + str(int_qr_size)

            for iRun in range(1, max_test_attempts + 1, 1):
                dict_timings = dict_size_qr_records[iRun]['timings']

                fTimeSum = 0.0
                for ftime in dict_timings.values():
                    fTimeSum += ftime

                faverage = fTimeSum / max_test_attempts
                writer.writerow(
                    {'QR_Version': int_qr_version,
                    'Size': str_size, 
                    't1': "{:.2f}".format(dict_timings[0]),
                    't2': "{:.2f}".format(dict_timings[1]),
                    't3': "{:.2f}".format(dict_timings[2]),
                    't4': "{:.2f}".format(dict_timings[3]),
                    't5': "{:.2f}".format(dict_timings[4]),
                    'average': "{:.2f}".format(faverage)})
    
    # close output window
    g_camera.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    create_csv_for_tests()
