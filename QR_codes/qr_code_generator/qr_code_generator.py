
# pip3 install qrcode
import qrcode
from qrcode.main import QRCode


"""
The version parameter is an integer from 1 to 40 that controls the size of the QR Code.

Version	Modules	Error Correction	Data bits	Numeric	Alphanumeric	Binary
    1	21x21	L	                152	        41	    25	            17
                M	                128	        34	    20	            14
                Q	                104     	27	    16	            11
                H	                72	        17	    10	            7

    40	177x177	L	                23.648	    7.089	4.296	        2.953
                M	                18.672	    5.596	3.391	        2,331
                Q	                13.328	    3.993	2,420	        1.663
                H	                10.208	    3,057	1.852	        1.273

    
Set to None and use the fit parameter when making the code to determine this automatically.
See https://blog.qr4.nl/page/QR-Code-Data-Capacity.aspx for versions and max data.

fill_color and back_color can change the background and the painting color of the QR, when using the default image factory.
Both parameters accept RGB color tuples.

img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))

The error_correction parameter controls the error correction used for the QR Code.
The following four constants are made available on the qrcode package:
    ERROR_CORRECT_L - About 7% or less errors can be corrected.
    ERROR_CORRECT_M (default) - About 15% or less errors can be corrected.
    ERROR_CORRECT_Q - About 25% or less errors can be corrected.
    ERROR_CORRECT_H - About 30% or less errors can be corrected.

The box_size parameter controls how many pixels each “box” of the QR code is.

The border parameter controls how many boxes thick the border should be.
The default is 4, which is the minimum according to the specs.
"""


def fncMakeFileData(iDataLength : int):
    strTestText = str(iDataLength) + " characters\n"
    iStrLen = len(strTestText)
    chChar = 'A'
    while (iStrLen < iDataLength):
        strTestText += chChar
        iStrLen = len(strTestText)
        if ('Z' == chChar):
            chChar = 'A'
        else:
            chChar = chr(ord(chChar) + 1)
    return strTestText


txDirectory_QR_Labels = "QR_labels/"
# works
# version 10, 400 chars
# version 20, ?? chars
# version 40, ?? chars

class cLabel: 
    def __init__(self, iVersion, iDataLength): 
        self.iVersion = iVersion 
        self.iDataLength = iDataLength
   
# creating list       
list = [] 
  
# appending instances to list 

# 10 mm -scanned at 3.5'
#=======================================
## Version 1 max theoretical limit: 14 Alphanumeric Chars
#list.append( cLabel(1, 12) ) # pass 
#list.append( cLabel(1, 13) ) # pass 
#list.append( cLabel(1, 14) ) # pass 

# Version 3 max theoretical limit: 53 Alphanumeric Chars
#list.append( cLabel(3, 40) ) # pass
#list.append( cLabel(3, 50) ) # pass
#list.append( cLabel(3, 53) ) # pass

# Version 4 max theoretical limit: 82 Alphanumeric Chars
list.append( cLabel(4, 60) ) # fail
list.append( cLabel(4, 70) ) # fail
list.append( cLabel(4, 82) ) # fail

# Version 5 max theoretical limit: 113 Alphanumeric Chars
#list.append( cLabel(5, 100) ) # fail
#list.append( cLabel(5, 110) ) # fail
#list.append( cLabel(5, 113) ) # fail


# 50 mm - scanned at 1.7'
#=======================================
## Version 1 max theoretical limit: 14 Alphanumeric Chars
##list.append( cLabel(1, 12) ) # pass 
##list.append( cLabel(1, 13) ) # pass 
##list.append( cLabel(1, 14) ) # pass 

## Version 10 max theoretical limit: 301 Alphanumeric Chars
#list.append( cLabel(10, 100) ) # pass
#list.append( cLabel(10, 150) ) # pass
#list.append( cLabel(10, 200) ) # pass
#list.append( cLabel(10, 250) ) # pass
#list.append( cLabel(10, 300) ) # pass
#list.append( cLabel(10, 301) ) # pass

## Version 12 max theoretical limit: 408 Alphanumeric Chars
#list.append( cLabel(12, 100) ) # pass
#list.append( cLabel(12, 200) ) # pass
#list.append( cLabel(12, 300) ) # pass
#list.append( cLabel(12, 408) ) # pass

## Version 14 max theoretical limit: 517 Alphanumeric Chars
#list.append( cLabel(14, 100) ) # pass
#list.append( cLabel(14, 200) ) # pass
#list.append( cLabel(14, 300) ) # pass
#list.append( cLabel(14, 517) ) # pass

## Version 15 max theoretical limit: 590 Alphanumeric Chars
#list.append( cLabel(15, 100) ) # fail
#list.append( cLabel(15, 200) ) # fail
#list.append( cLabel(15, 300) ) # fail
#list.append( cLabel(15, 590) ) # fail

## Version 10 max theoretical limit: 959 Alphanumeric Chars
#list.append( cLabel(20, 100) ) # fail
#list.append( cLabel(20, 200) ) # fail
#list.append( cLabel(20, 400) ) # fail
#list.append( cLabel(20, 800) ) # fail
#list.append( cLabel(20, 959) ) # fail


## Version 10 max theoretical limit: 3380 Alphanumeric Chars
#list.append( cLabel(40, 100) ) # fail
#list.append( cLabel(40, 500) ) # fail
#list.append( cLabel(40, 1000) ) # fail
#list.append( cLabel(40, 2000) ) # fail
#list.append( cLabel(40, 3000) ) # fail
#list.append( cLabel(40, 3380) ) # fail 

  
for obj in list:
    print( obj.iVersion, obj.iDataLength, sep =' ' )

    qr = qrcode.QRCode(
        version=obj.iVersion,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=0,
    )
    txfileName = "Ver_" + str(obj.iVersion) + "_" + str(obj.iDataLength) + "_chars.png"
    txFilePath = txDirectory_QR_Labels + txfileName
    strTestText = fncMakeFileData(obj.iDataLength)
    qr.clear()
    qr.add_data(strTestText)
    qr.make(fit=False) # Don't 'fit' the data to a larger version.
    img = qr.make_image(fill_color="black", back_color="white")
    print("file:" + txFilePath)
    img.save(txFilePath)

