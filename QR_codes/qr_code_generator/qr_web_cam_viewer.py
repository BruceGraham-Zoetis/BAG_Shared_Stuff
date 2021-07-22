# see https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5

# pip3 install Pillow
# pip3 install opencv-python
# pip3 install pyzbar

#import libraries
import cv2
from pyzbar import pyzbar

##


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
    return frame

def main():
    #1
    camera = cv2.VideoCapture(0)
    
    ## Disable webcam LED
    """
    dRtn = camera.get(cv2.CAP_PROP_BACKLIGHT)
    print("get CAP_PROP_BACKLIGHT: ", dRtn)
    
    print("set CAP_PROP_BACKLIGHT: 0.0")
    bSupported = camera.set(cv2.CAP_PROP_BACKLIGHT, 0.0)
    if (bSupported):
        print("returned CAP_PROP_BACKLIGHT supported")
    else:
        print("CAP_PROP_returned BACKLIGHT not supported")
    
    dRtn = camera.get(cv2.CAP_PROP_BACKLIGHT)
    print("get CAP_PROP_BACKLIGHT: ", dRtn)

    dRtn = camera.get(cv2.CAP_PROP_SETTINGS)
    print("get CAP_PROP_SETTINGS: ", dRtn)
    dRtn = camera.set(cv2.CAP_PROP_SETTINGS, 1.0)
    print("set CAP_PROP_SETTINGS: 1.0")
    dRtn = camera.get(cv2.CAP_PROP_SETTINGS)
    print("get CAP_PROP_SETTINGS: ", dRtn)
    dRtn = camera.set(cv2.CAP_PROP_SETTINGS, 0.0)
    print("set CAP_PROP_SETTINGS: 0.0")
    dRtn = camera.get(cv2.CAP_PROP_SETTINGS)
    print("get CAP_PROP_SETTINGS: ", dRtn)
    """

    # The properties of videocapture have get / set methods as id/value pair
    #  and the led mode is the id 412. And led selector 411 !
    #  Technically you should do : vc.set(412,your_value ) but that one (412) is a constant.
    dRtn = camera.get(411)
    print("get 411: ", dRtn)
    dRtn = camera.set(411, 1.0)
    print("set 411: 1.0")
    dRtn = camera.get(411)
    print("get 411: ", dRtn)


    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()

