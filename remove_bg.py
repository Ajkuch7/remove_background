import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,750)
cap.set(4, 500)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img,(0,255,0), threshold=0.81)

    imagestack = cvzone.stackImages([img,imgOut],2,1)
    _,imgagestack = fpsReader.update(imagestack, color=(0,0,255))
    cv2.imshow("Image", imagestack)
    cv2.waitKey(1)
