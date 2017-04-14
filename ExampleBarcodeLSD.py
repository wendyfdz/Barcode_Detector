from skimage import io
import cv2
import numpy as np

barcode=io.imread('05102009081.jpg')
barcodeGray=cv2.cvtColor(barcode, cv2.COLOR_BGR2GRAY)

det=cv2.createLineSegmentDetector()
parameters=det.detect(barcodeGray)

imageShape=np.shape(barcodeGray)
barcodeWhiteBackground=np.ones(imageShape)
barcodeLSD=det.drawSegments(barcodeWhiteBackground,parameters[0])
io.imshow(barcodeLSD)
io.show()

# Integer array


