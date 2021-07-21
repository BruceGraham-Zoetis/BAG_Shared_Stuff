# pip3 install qrcode
import qrcode
from qrcode.main import QRCode

# pip install pyqrcode
# pip install pyzbar
from PIL import Image
from pyzbar.pyzbar import decode

results = decode(Image.open("QR_labels/" + "Ver_12_408_chars.png"))
for result in results:
    print("data:" + str(result.data))
    print("type:" + result.type)
