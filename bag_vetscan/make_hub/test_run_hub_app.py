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
import threading
import socket

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
Handle client connections.
"""
def thread_wait_for_clients():
    global g_vetscan_hub
    global g_window

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname() # Get local machine name
    port = 1024                 # Reserve a port for your service.
    try:
        soc.bind((host, port))        # Bind to the port
    except:
        print("error bind()")
        return

    while True:
        while True:
            print("listen() for client connection.")
            soc.listen()
            print("accept()")
            client, strAddress = soc.accept()

            print("Connected client: " + strAddress)
            g_vetscan_hub.analyzer_add(strAddress)
            try:
                g_window['-OUTPUT-'].update(strAddress)
            except:
                pass

            if (True):
                print("Diconnected client: " + strAddress)
                g_vetscan_hub.analyzer_remove(strAddress)
                client.close()



def start_thread_hub_server():
    print("Starting Hub server")
    thread = threading.Thread(target = thread_wait_for_clients)
    thread.start()
    return thread


def gui_window():
    global g_vetscan_hub
    global g_window

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
            [sg.Text(size=(100,20), key='-OUTPUT-')],
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

        o_analyzer_dracula = g_vetscan_hub.analyzer_get("127.0.0.1")
        if ("" == o_analyzer_dracula.get_ip_address()):
            g_window['-OUTPUT-'].update("no analyzer")
        else:
            strOUTPUT = "Analyzer: %s ", o_analyzer_dracula.get_ip_address()
            strOUTPUT += o_analyzer_dracula.get_name()

            if event == 'GET supported_consumables':
                strRtn = o_analyzer_dracula.get_consumables()
            elif event == 'PUT light blink':
                strRtn = o_analyzer_dracula.light_blink()
            elif event == 'PUT light Off':
                strRtn = o_analyzer_dracula.light_off()
            elif event == 'PUT power off':
                strRtn = o_analyzer_dracula.power_off()
            elif event == 'PUT power reboot':
                strRtn = o_analyzer_dracula.power_reboot()
            else:
                strRtn = "event ?"
            
            strOUTPUT += strRtn
            g_window['-OUTPUT-'].update(strOUTPUT)

    g_window.close()

    # close output g_window
    camera.release()
    cv2.destroyAllWindows()


def start_thread_waiting_for_clients():
    print("Starting waiting for clients")
    thread = threading.Thread(target=thread_wait_for_clients)
    thread.start()
    return thread


if __name__ == '__main__':
    global g_vetscan_hub

    print("")
    g_vetscan_hub = hub_app_gui.class_vetscan_hub.CVetscanHub()

    threadWaitForClients = start_thread_waiting_for_clients()
    threadHubServer = start_thread_hub_server()
    gui_window() # returns when Exit button is pressed.
    
    # TODO - Kill threadWaitForClients
    # TODO - Kill threadHubServer