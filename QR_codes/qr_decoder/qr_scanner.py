# pip install pyzbar

#import libraries
import cv2
from pyzbar import pyzbar
import json

def main():
    print("Scanning for QR code...")
    camera = cv2.VideoCapture(0)

    bFound = False

    while not bFound:
        ret, frame = camera.read()

        barcodes = pyzbar.decode(frame)
        if (len(barcodes) == 0):
            continue

        for barcode in barcodes:
            barcode_info = barcode.data.decode('utf-8')
            bFound = True

        print("Found QR code")
        print(barcode_info)
        print("Data length:", str(len(barcode_info)))
        print()
        dic1 = json.loads(barcode_info)
        print(" exp:", dic1['exp'])
        print("name:", dic1['name'])
        print(" lot:", dic1['lot'])
        print("data:", dic1['data'])
        break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

