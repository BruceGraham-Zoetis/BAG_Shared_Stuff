#!/usr/bin/env python3
# 
"""
File: test_run_hub_app.py

Purpose: An app that uses PySimpleGUI that interacts with the user
using a window that contains widgets.

pip3 install pysimplegui
pip3 install websockets

"""

from __future__ import absolute_import

## fix path so that contained py files can be imported
import os, sys
from posix import O_ACCMODE
strThisFilePath = os.path.dirname(__file__)
sys.path.append(strThisFilePath)
sys.path.append(strThisFilePath + "/hub_app")

# 
import PySimpleGUI as sg
import cv2
import os
import platform
import asyncio
import datetime
import hub_app_gui.class_vetscan_hub
import config
import thread_wait_for_clients

global camera

global strWindowtitle
strWindowtitle = 'Vetscan Hub'


def isCameraRotated() -> bool:
    bCameraIsRotated = False

    if (os.name != 'nt'):
        tuples = platform.uname()
        i = 0
        while (i < len(tuples)):
            strValue = tuples[i]
            # print(strValue)
            if ("lubuntu" == strValue):
                bCameraIsRotated = True
                break
            if ("ubuntu" == strValue):
                break
            i = i + 1
    return bCameraIsRotated



def gui_window():
    print("Starting GUI superloop")

    bCameraIsRotated = isCameraRotated()

    # open output g_window
    camera = cv2.VideoCapture(0)

    try:
        ret, frameOrig = camera.read()
    except:
        ret = False

    if (not ret):
        print("Error: Unable to read from camera.")
        print("Confirm that the camera is connected.")
        exit()

    sg.theme('BluePurple')

    camera_Width  = 320 # 480 # 640 # 1024 # 1280
    camera_Height = 240 # 320 # 480 # 780  # 960
    frameSize = (camera_Width, camera_Height)

    layout = [
            [sg.Image(filename='', key='image')],
            [sg.Text(size=(50, 1), key='-ANALYZER-')],
            [sg.Button('GET supported_consumables')],
            [sg.Button('PUT light blink')],
            [sg.Button('PUT light Off')],
            [sg.Button('PUT power off')],
            [sg.Button('PUT power reboot')],
            [sg.Text(size=(50, 20), key='-OUTPUT-')],
            [sg.Button('Exit')]
            ]

    config.g_window = sg.Window(strWindowtitle, layout)

    if (not bCameraIsRotated):
        ret, frameOrig = camera.read()
    else:
        ret, frameRotated = camera.read()
        frameOrig = cv2.flip(frameRotated, -1)
    frameIn = cv2.resize(frameOrig, frameSize)
    imgbytes = cv2.imencode('.png', frameIn)[1].tobytes()  # ditto

    while True:  # Event Loop
        event, values = config.g_window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

        if (not bCameraIsRotated):
            ret, frameOrig = camera.read()
        else:
            ret, frameRotated = camera.read()
            frameOrig = cv2.flip(frameRotated, -1)
        frameIn = cv2.resize(frameOrig, frameSize)
        imgbytes = cv2.imencode('.png', frameIn)[1].tobytes()  # ditto
        config.g_window['image'].update(data=imgbytes, size=(None,None))

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        o_current_analyzer = config.g_vetscan_hub.analyzer_get("127.0.0.1")
        if ("" == o_current_analyzer.get_ip_address()):
            config.g_window['-ANALYZER-'].update("no analyzer")
        else:
            str_anlyzer = "Analyzer: {ip} {name}".format( \
                            ip = o_current_analyzer.get_ip_address(), \
                            name = o_current_analyzer.get_name())

            config.g_window['-ANALYZER-'].update(str_anlyzer)

            if event == 'GET supported_consumables':
                str_output = o_current_analyzer.get_consumables()
            elif event == 'PUT light blink':
                str_output = o_current_analyzer.light_blink()
            elif event == 'PUT light Off':
                str_output = o_current_analyzer.light_off()
            elif event == 'PUT power off':
                str_output = o_current_analyzer.power_off()
            elif event == 'PUT power reboot':
                str_output = o_current_analyzer.power_reboot()
            
            config.g_window['-OUTPUT-'].update(str_output)

    config.g_window.close()

    # close output g_window
    camera.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    print("")

    config.g_vetscan_hub = hub_app_gui.class_vetscan_hub.CVetscanHub()

    threadHubServer = thread_wait_for_clients.start_thread_hub_server()
    gui_window() # returns when Exit button is pressed.
    
    # TODO - Kill threadHubServer