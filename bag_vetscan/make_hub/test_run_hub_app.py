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
import datetime
import hub_app_gui.class_vetscan_hub

global camera

global strWindowtitle
strWindowtitle = 'Vetscan Hub'

global g_window

global g_vetscan_hub


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


"""
Web Server handler coroutine. runs while client is connected.
"""
async def hub_server_connetion(websocket, path):
    global g_vetscan_hub
    global g_window

    tupleRemote = websocket.remote_address
    strAddress = tupleRemote[0]
    print("Connected client: " + strAddress)

    g_vetscan_hub.analyzer_add(strAddress)

    strAnalyzerName = ""
    bConnected = True

    while bConnected:
        print("wait on recv")
        try:
            strFromClient = await websocket.recv()
        except:
            bConnected = False

        try:
            g_window['-OUTPUT-'].update(strFromClient)
        except:
            pass

        print("server(Hub) -> client(" + strAnalyzerName + ")\n\t" + strFromClient)

        if ("get datetime" == strFromClient):
            strToClient = datetime.datetime.utcnow().isoformat() + 'Z'
            print("client(" + strAnalyzerName + ") -> server(Hub)\n\t" + strToClient)
            try:
                await websocket.send(strToClient)
                try:
                    g_window['-OUTPUT-'].update(strFromClient + " " + strToClient)
                except:
                    pass
            except:
                bConnected = False

        elif ("set name" in strFromClient):
            strParts = strFromClient.split(" ")
            strAnalyzerName = strParts[2]
            g_vetscan_hub.analyzer_set_name(strAddress, strAnalyzerName)

    print("Diconnected client: " + strAddress)
    g_vetscan_hub.analyzer_remove(strAddress)


if __name__ == '__main__':
    global g_vetscan_hub
    global g_window

    g_vetscan_hub = hub_app_gui.class_vetscan_hub.CVetscanHub()

    print("Starting web server")
    start_server = websockets.serve(hub_server_connetion, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    print("Starting GUI superloop")
    bCameraIsFlipped = isCameraFlipped()

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
            [sg.Button('GET supported_consumables')],
            [sg.Button('PUT light blink')],
            [sg.Button('PUT light Off')],
            [sg.Button('PUT power off')],
            [sg.Button('PUT power reboot')],
            [sg.Text(size=(20,30), key='-OUTPUT-')],
            [sg.Button('Exit')]
            ]

    g_window = sg.Window(strWindowtitle, layout)

    if (not bCameraIsFlipped):
        ret, frameOrig = camera.read()
    else:
        ret, frameFlipped = camera.read()
        frameOrig = cv2.flip(frameFlipped, -1)
    frameIn = cv2.resize(frameOrig, frameSize)
    imgbytes = cv2.imencode('.png', frameIn)[1].tobytes()  # ditto

    while True:  # Event Loop
        event, values = g_window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

        if (not bCameraIsFlipped):
            ret, frameOrig = camera.read()
        else:
            ret, frameFlipped = camera.read()
            frameOrig = cv2.flip(frameFlipped, -1)
        frameIn = cv2.resize(frameOrig, frameSize)
        imgbytes = cv2.imencode('.png', frameIn)[1].tobytes()  # ditto
        g_window['image'].update(data=imgbytes, size=(None,None))

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'GET supported_consumables':
            strConsumables = o_analyzer_dracula.get_consumables()
            g_window['-OUTPUT-'].update(strConsumables)
        elif event == 'PUT light blink':
            strRtn = o_analyzer_dracula.light_blink()
            g_window['-OUTPUT-'].update(strRtn)
        elif event == 'PUT light Off':
            strRtn = o_analyzer_dracula.light_off()
            g_window['-OUTPUT-'].update(strRtn)

        elif event == 'PUT power off':
            strRtn = o_analyzer_dracula.power_off()
            g_window['-OUTPUT-'].update(strRtn)
        elif event == 'PUT power reboot':
            strRtn = o_analyzer_dracula.power_reboot()
            g_window['-OUTPUT-'].update(strRtn)

    g_window.close()

    # close output g_window
    camera.release()
    cv2.destroyAllWindows()


