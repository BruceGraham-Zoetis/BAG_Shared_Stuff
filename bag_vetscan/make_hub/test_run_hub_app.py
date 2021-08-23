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
import websockets
import asyncio

import hub_app_gui.class_vetscan_hub

global camera

global strWindowtitle
strWindowtitle = 'Vetscan Hub'

def isCameraFlipped() -> bool:
    bCameraIsFlipped = False

    if (os.name != 'nt'):
        tuples = platform.uname()
        i = 0
        while (i < len(tuples)):
            strValue = tuples[i]
            # print(strValue)
            if ("lubuntu" == strValue):
                bCameraIsFlipped = True
                break
            if ("ubuntu" == strValue):
                break
            i = i + 1
    return bCameraIsFlipped


async def hub_server(websocket, path):
    async for message in websocket:
        print("Connected to analyzer")
        strRtn = message
        window['-OUTPUT-'].update(strRtn)


if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(
        websockets.serve(hub_server, 'localhost', 8765))

    bCameraIsFlipped = isCameraFlipped()

    o_vetscan_hub = hub_app_gui.class_vetscan_hub.CVetscanHub()

    bRtn = o_vetscan_hub.add_analyzer("127.0.0.1", "xxx")
    bRtn = o_vetscan_hub.remove_analyzer("127.0.0.1")

    bRtn = o_vetscan_hub.add_analyzer("127.0.0.1", "dracula")
    o_analyzer_dracula = o_vetscan_hub.get_analyzer("127.0.0.1")
    print("o_analyzer_dracula IP: %s" % o_analyzer_dracula.get_ip_address())

    # open output window
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
            [sg.Button('GET supported_consumables')],
            [sg.Button('PUT light blink')],
            [sg.Button('PUT light Off')],
            [sg.Button('PUT power off')],
            [sg.Button('PUT power reboot')],
            [sg.Text(size=(20,30), key='-OUTPUT-')],
            [sg.Button('Exit')]
            ]

    window = sg.Window(strWindowtitle, layout)

    if (not bCameraIsFlipped):
        ret, frameOrig = camera.read()
    else:
        ret, frameFlipped = camera.read()
        frameOrig = cv2.flip(frameFlipped, -1)
    frameIn = cv2.resize(frameOrig, frameSize)
    imgbytes = cv2.imencode('.png', frameIn)[1].tobytes()  # ditto

    while True:  # Event Loop
        event, values = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

        if (not bCameraIsFlipped):
            ret, frameOrig = camera.read()
        else:
            ret, frameFlipped = camera.read()
            frameOrig = cv2.flip(frameFlipped, -1)
        frameIn = cv2.resize(frameOrig, frameSize)
        imgbytes = cv2.imencode('.png', frameIn)[1].tobytes()  # ditto
        window['image'].update(data=imgbytes, size=(None,None))

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'GET supported_consumables':
            strConsumables = o_analyzer_dracula.get_consumables()
            window['-OUTPUT-'].update(strConsumables)
        elif event == 'PUT light blink':
            strRtn = o_analyzer_dracula.light_blink()
            window['-OUTPUT-'].update(strRtn)
        elif event == 'PUT light Off':
            strRtn = o_analyzer_dracula.light_off()
            window['-OUTPUT-'].update(strRtn)

        elif event == 'PUT power off':
            strRtn = o_analyzer_dracula.power_off()
            window['-OUTPUT-'].update(strRtn)
        elif event == 'PUT power reboot':
            strRtn = o_analyzer_dracula.power_reboot()
            window['-OUTPUT-'].update(strRtn)

    window.close()

    # close output window
    camera.release()
    cv2.destroyAllWindows()


