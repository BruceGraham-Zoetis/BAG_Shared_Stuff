#!/usr/bin/env python3
# 
# File: camera.py

# Computer Vision
# ==========================
#   $ sudo -H pip3 install opencv-python
#   $ sudo -H apt-get install libzbar0
#   $ sudo -H pip3 install pyzbar
#   $ sudo -H pip3 install pyzbar[scripts]
#
from genericpath import isdir
from typing import Text
import cv2
from pyzbar import pyzbar
import os
import time
import numpy

global strWindowtitle
strWindowtitle = "Camera"

if __name__ == '__main__':
    font = cv2.FONT_HERSHEY_DUPLEX

    if (not os.path.isdir("./camera/")):
        os.mkdir("./camera/")

    while(True):
        strName = input("Enter file name, q to quit: ")
        if ('q' == strName):
            break

        strFileName = "./camera/" + strName

        # open output window
        camera = cv2.VideoCapture(0)

        # turn on the camera auto-focus
        camera.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        while(True):
            ret, frameIn = camera.read()
            frameWithText = frameIn
            cv2.putText(frameWithText, "Press Esc when ready", (50, 50), font, 1.0, (255, 255, 255), 1)
            cv2.imshow(strWindowtitle, frameWithText)
            cv2.waitKey(10) #???
            if cv2.waitKey(1) & 0xFF == 27:
                break

        cv2.imwrite(strFileName, frameIn)
        print("Saved to file")

        # close output window
        camera.release()
        cv2.destroyAllWindows()

