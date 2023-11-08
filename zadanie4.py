from pyzbar.pyzbar import decode
from PIL import Image
import cv2
print(decode(Image.open('barcode.png')))


def BarcodeReader(image):
    img = cv2.imread(image)
    detectedBarcodes = decode(img)
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                print(barcode.data)
                print(barcode.type)

    # Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


BarcodeReader('barcode.png')