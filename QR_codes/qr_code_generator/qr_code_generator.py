
# pip3 install qrcode
import qrcode
from qrcode.main import QRCode

# pseudorandom number generator
from random import seed
from random import random
from random import randrange

import os

txtMinTestText = "{\n\"exp\":\"2022-05-27\",\n\"name\":\"CDP\",\n\"lot\":\"500-1038\",\n\"data\":\""


def fncMakeJsonData(TestData, iDataLength : int):
    strTestText = txtMinTestText

    # -2 for ending "\n}
    iRemainder = iDataLength - len(txtMinTestText) -3

    if (0 < iRemainder):
        strTestText += TestData[:iRemainder]

    strTestText += "\"\n}"

    return strTestText


def fncMakeRawData(TestData, iDataLength : int):
    strTestText = TestData[:iDataLength]
    return strTestText


# find max data length by trail and error
def findAndSaveMaxImage(txtDirectory : str, bUseJson : bool, TestData):
    txtFilePath = os.getcwd()
    txtFilePath += "/"
    txtFilePath += txtDirectory

    if (not os.path.isdir(txtFilePath)):
        os.mkdir(txtFilePath)

    file = open(txtFilePath + "version_sizes.txt", "wt")
    file.write("File: " + txtFilePath + "version_sizes.txt" + "\n")

    iDataLength = len(txtMinTestText) + 3
    iVersion = 1

    iLow = 0
    iHigh = 5000
    bFit = False

    while iVersion <= 40:

        qr = qrcode.QRCode(
            version=iVersion,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            #error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1, # 1 pixel per box in the saved image. A version 11 png will be 37 x 37 pixels
            border=0, # no border around the saved png image.
        )

        while (True): 
            qr.clear()
            if (bUseJson):
                strTestText = fncMakeJsonData(TestData, iDataLength)
            else:
                strTestText = fncMakeRawData(TestData, iDataLength)
            qr.add_data(strTestText)

            try:
                qr.make(fit=False) # Don't 'fit' the data to a larger version.
                bFit = True
            except:
                bFit = False

            if (bFit):
                # try between iDataLength and iHigh
                # iDataLength:20 + iHigh:30 / 2 = 25
                iLow = iDataLength
                iTried = iDataLength
                iDataLength = (iDataLength + iHigh) // 2
                #print("fit " + str(iTried) + "  Try " + str(iDataLength))
                if ((iTried + 1) == iHigh):
                    print("Version: " + str(iVersion) + " Length: " + str(iDataLength))
                    # print("JSON: " + strTestText)

                    qr.clear()
                    if (bUseJson):
                        strTestText = fncMakeJsonData(TestData, iDataLength)
                    else:
                        strTestText = fncMakeRawData(TestData, iDataLength)
                    qr.add_data(strTestText)
                    qr.make(fit=False) # Don't 'fit' the data to a larger version.
                    img = qr.make_image(fill_color="black", back_color="white")

                    txfileName = "Ver_" + str(iVersion) + "_" + str(iDataLength) + "_chars.png"
                    txFilePath = txtDirectory + txfileName
                    img.save(txFilePath)

                    txtRecord = str(iVersion) + " " + str(iDataLength) + "\n"
                    file.write(txtRecord)

                    # setup for the next version
                    iHigh *= 2
                    iVersion += 1
                    break
            else:
                if (iDataLength < (len(txtMinTestText) + 3)):
                    print("QR version " + str(iVersion) + " is too small")

                    # setup for the next version
                    iHigh *= 2
                    iVersion += 1
                    break

                # try between iLow and iDataLength
                # iLow:10 + iDataLength:20 / 2 = 15
                iHigh = iDataLength
                iTried = iDataLength
                iDataLength = (iLow + iDataLength) // 2
                #print("big " + str(iTried) + "  Try " + str(iDataLength))

    file.close()

######## main #########

# seed random number generator
# seed(1)

# 'd' = chr(ord('a') + 3)

# 23,648 = max data length for version = 40, ECC = L
print("Building QR_labels_Alphanumeric")
TestData = ""
for iCount in range(0, 23648):
    TestData += "A0"   # Alphanumeric, class str, "A0A0A0"

findAndSaveMaxImage("QR_labels_Alphanumeric_JSON/", True, TestData)
findAndSaveMaxImage("QR_labels_Alphanumeric/", False, TestData)


print("Building QR_labels_Numeric")
TestData = ""
for iCount in range(0, 23648):
    TestData += str(randrange(0, 9))  # Numeric, class str, "3546868"

findAndSaveMaxImage("QR_labels_Numeric_JSON/", True, TestData)
findAndSaveMaxImage("QR_labels_Numeric/", False, TestData)


print("Building QR_labels_Binary_not_displayable")
TestData = ""
for iCount in range(0, 23648):
    TestData += chr(randrange(0, 9))  # Binary, class str, -- not displayable

findAndSaveMaxImage("QR_labels_Binary_not_displayable_JSON/", True, TestData)
findAndSaveMaxImage("QR_labels_Binary_not_displayable/", False, TestData)


print("Building QR_labels_Binary_displayable")
TestData = ""
for iCount in range(0, 23648):
    TestData += "A{\n"    # Binary, class str, "A{\nA{\nA{\n"

findAndSaveMaxImage("QR_labels_Binary_displayable_JSON/", True, TestData)
findAndSaveMaxImage("QR_labels_Binary_displayable/", False, TestData)
