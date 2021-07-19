
# pip3 install qrcode

import qrcode

strTestText = "100 characters\n012345678901234567890123456789012345678901234567890123456789012345678901234567890123"

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

The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).
"""

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=0,
)
qr.add_data(strTestText)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("QR_label_100_chars.png")
