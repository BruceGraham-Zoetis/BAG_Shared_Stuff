
"""
File: data_matix_decoder.py

pip3 install pylibdmtx
pip3 install pylibdmtx[scripts]
"""

import time
from pylibdmtx.pylibdmtx import decode
from PIL import Image

# returned from decode: 
#   [Decoded(data=b'+EABA5000038480/$$70311AA2/S03085E1/14D20210727E', rect=Rect(left=115, top=215, width=111, height=-118))]


def data_matrix_decode_image(image) -> str:
    lstRtn = decode(image)
    if (0 < len(lstRtn)):
        lst0 = lstRtn[0] # get first decoded "data matrix"
        strRtn = lst0[0] # get data from first decoded "data matrix"
    else:
        strRtn = ""

    return strRtn

def data_matrix_decode_file(strFile : str) -> str:
    lstRtn = decode(Image.open(strFile))
    if (0 < len(lstRtn)):
        lst0 = lstRtn[0] # get first decoded "data matrix"
        strRtn = lst0[0] # get data from first decoded "data matrix"
    else:
        strRtn = ""

    return strRtn


"""
timing test of the decoder
    clean image decode: 0.08, 0.05 seconds
    camera image decode: 1.86, 1.88 seconds
"""
if __name__ == '__main__':
    for i in range(0, 4):
        timeStart = time.time()
        if 0 == i:
            strDecoded = data_matrix_decode_file("../../data_matrix_codes/data_matrix_cdp.png")
        elif 1 == i:
            strDecoded = data_matrix_decode_file("../../data_matrix_codes/data_matrix_cpl.png")
        elif 2 == i:
            strDecoded = data_matrix_decode_file("../../data_matrix_codes/data_matrix_cpl_camera.png")
        elif 3 == i:
            strDecoded = data_matrix_decode_file("../../data_matrix_codes/data_matrix_cpl_camera_glare.png")

        timeEnd = time.time()
        print("  decode time: %.2f seconds" % (timeEnd - timeStart))
        print(strDecoded)

