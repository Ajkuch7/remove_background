import time

import cv2

video = cv2.VideoCapture(0)
check,frame = video.read()
print(check)
print(frame)

time.sleep(3)
