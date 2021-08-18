#!/usr/bin/env python3
# 
"""
File: test_run_hub_app.py

Purpose: An app that uses PySimpleGUI that interacts with the user
using a window that contains widgets.

pip install pysimplegui

"""

from __future__ import absolute_import

## fix path so that contained py files can be imported
import os, sys
sys.path.append(os.path.curdir + "/hub_app")

# 
import PySimpleGUI as sg
import cv2
import os

import class_vetscan_hub

global camera

global strWindowtitle
strWindowtitle = 'Vetscan Hub'

#bCameraIsFlipped = True
bCameraIsFlipped = False

if __name__ == '__main__':

    o_vetscan_hub = class_vetscan_hub.CVetscanHub()

    o_analyzer_dracula = o_vetscan_hub.add_analyzer("127.0.0.1", "dracula")

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
            [sg.Text(size=(50,1), key='TEXT_CONSUMABLES')],
            [sg.Button('GET supported_consumables')],
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

    window.close()

    # close output window
    camera.release()
    cv2.destroyAllWindows()


