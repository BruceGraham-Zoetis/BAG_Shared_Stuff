#!/usr/bin/env python3
# 
"""
File: main.py

Purpose: An app that uses PySimpleGUI that interacts with the user
using a window that contains widgets.

pip install pysimplegui

"""
import PySimpleGUI as sg
import cv2
import os

global camera

global strWindowtitle
strWindowtitle = 'Barcode/QR code reader'



if __name__ == '__main__':

    # open output window
    camera = cv2.VideoCapture(0)

    sg.theme('BluePurple')

    camera_Width  = 320 # 480 # 640 # 1024 # 1280
    camera_Height = 240 # 320 # 480 # 780  # 960
    frameSize = (camera_Width, camera_Height)

    layout = [
            [sg.Image(filename='', key='image')],
            [sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Input(key='-IN-')],
            [sg.Button('Show'), sg.Button('Exit')]
            ]

    window = sg.Window('Pattern 2B', layout)

    if (os.name == 'nt'):
        ret, frameOrig = camera.read()
    else:
        ret, frameRotated = camera.read()
        frameOrig = cv2.flip(frameRotated, -1)
    frameIn = cv2.resize(frameOrig, frameSize)
    imgbytes = cv2.imencode('.png', frameIn)[1].tobytes()  # ditto

    while True:  # Event Loop
        event, values = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

        if (os.name == 'nt'):
            ret, frameOrig = camera.read()
        else:
            ret, frameRotated = camera.read()
            frameOrig = cv2.flip(frameRotated, -1)
        frameIn = cv2.resize(frameOrig, frameSize)
        imgbytes = cv2.imencode('.png', frameIn)[1].tobytes()  # ditto
        window['image'].update(data=imgbytes, size=(None,None))

        cv2.imshow(strWindowtitle, frameIn)
        cv2.waitKey(10) #???

        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            # Update the "output" text element to be the value of "input" element
            window['-OUTPUT-'].update(values['-IN-'])

    window.close()

    # close output window
    camera.release()
    cv2.destroyAllWindows()


