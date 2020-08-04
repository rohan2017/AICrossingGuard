import cv2
import numpy as np

cap = cv2.VideoCapture(0)
previmg = 0

while 1:

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    diff = gray - previmg

    diff = cv2.blur(diff, (10, 10))

    diff = cv2.blur(diff, (100, 100))

    cv2.imshow('motion ', diff)

    previmg = gray

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
