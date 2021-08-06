#!/usr/bin/env python3

"""
File: json_file_generator.py

Purpose: Reads files in directory json_data_files containing JSON strings and makes QR codes from them.

See https://zxing.org/w/decode.jspx for decoding the image files.

"""

import json
import os

from typing import Text

import qrcode
from qrcode.main import QRCode



"""
=====================================
Data types in Python and JSON
=====================================

Python              JSON
==================  ==========
dict                object
list, tuple         array
str                 string
int, long, float    number
True                true
False               false
None                null
"""

def traverese(d, current_key=''):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from traverese(v, current_key + k + '.')
    elif isinstance(d, list):
        for i, vv in enumerate(d):
            yield from traverese(vv, current_key + '[' + str(i) + '].')
    else:
        yield current_key + str(d)


def saveImages(txtOutputDirectory : str, txtPngFileName : str, strTestText : str):
    txtFilePath = os.getcwd()
    txtFilePath += "/"
    txtFilePath += txtOutputDirectory

    if (not os.path.isdir(txtFilePath)):
        os.mkdir(txtFilePath)

    iVersion = 1

    while iVersion <= 40:

        qr = qrcode.QRCode(
            version=iVersion,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            #error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1, # 1 pixel per box in the saved image. A version 11 png will be 37 x 37 pixels
            border=0, # no border around the saved png image.
        )

        qr.clear()
        qr.add_data(strTestText)

        try:
            qr.make(fit=False) # Don't 'fit' the data to a larger version.
            img = qr.make_image(fill_color="black", back_color="white")
            txtFilePath = txtOutputDirectory + txtPngFileName + "_" + str(iVersion) + ".png"
            img.save(txtFilePath)
        except:
            pass

        # setup for the next version
        iVersion += 1


if __name__ == '__main__':
    relevant_path = "./json_data_files" # path to folder
    included_extensions = ['txt']
    file_names =\
        [\
            fn for fn in os.listdir(relevant_path)\
                if any(fn.endswith(ext) for ext in included_extensions)\
        ]

    for txtfileName in file_names:
        print("\n-------------------------")
        print(txtfileName)
        print("-------------------------\n")
        f = open("./json_data_files/" + txtfileName, "r")
        json_text = f.read()

        """
        for index in traverese(json_text):
            print(index)
        """

        filename, file_extension = os.path.splitext(txtfileName)

        saveImages("./QR_labels_from_files/", filename, json_text)
        f.close()

    print("\nEnd of test\n")


