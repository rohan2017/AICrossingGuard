import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
# so far, this method is not very promising.

people = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture(0)
image = cv2.imread("C:/Users/rohan/PycharmProjects/TrafficLight/Pictures/street.jpg")
while 1:
    # ret, img = cap.read()
    img = image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pedestrians = people.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
