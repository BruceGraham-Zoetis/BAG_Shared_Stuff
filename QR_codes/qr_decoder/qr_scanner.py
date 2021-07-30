#!/usr/bin/env python3
# 
# # see https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5

# pip3 install pyzbar
# pip3 install playsound

#import libraries
import subprocess
import cv2
from pyzbar import pyzbar
import json
import os
import playsound
import time

def decode_display_barcodes(frame):
    try:
        barcodes = pyzbar.decode(frame)
    except:
        return

    for barcode in barcodes:
        try:
            # Detected some data in the QR code, so beep.
            playsound.playsound('beep-08b.wav')
            time.sleep(0.2)
        except:
            pass

        x, y , w, h = barcode.rect

        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        txtDisplay = ''
        font = cv2.FONT_HERSHEY_DUPLEX
        try:
            dic1 = json.loads(barcode_info)

            try:
                txtDisplay = " exp: " + dic1['exp']
            except:
                txtDisplay = " exp: ?"
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 30), font, 1.0, (255, 255, 255), 1)

            try:
                txtDisplay = "name: " + dic1['name']
            except:
                txtDisplay = " name: ?"
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 60), font, 1.0, (255, 255, 255), 1)

            try:
                txtDisplay = " lot: " + dic1['lot']
            except:
                txtDisplay = " lot: ?"
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 90), font, 1.0, (255, 255, 255), 1)

            try:
                txtDisplay = "data: " + dic1['data']
            except:
                txtDisplay = "data: ?"
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 120), font, 1.0, (255, 255, 255), 1)

        except:
            txtDisplay = barcode_info
            cv2.putText(frame, txtDisplay, (x + 6, y + h + 30), font, 1.0, (255, 255, 255), 1)

    return frame

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)

    # turn off the LED
    if (os.name == 'nt'):
        print("NT")
    elif (os.name == 'posix'):
        lstCmd = ["./OneDrive_1_7-30-2021/SP_V4L2_API-2021-07-19/Demo_V4L2/bin/SPCA_v4l2_tool_GNU_x64", "-D0", "-w", "-a2043", "-e0"]
        print(*lstCmd)
        subprocess.call(lstCmd)

    ret, frame = camera.read()

    while ret:
        frame = decode_display_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        ret, frame = camera.read()

    camera.release()
    cv2.destroyAllWindows()

