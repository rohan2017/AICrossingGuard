import cv2
import numpy as np
from YOLO import detector
import serial
import time

yolodetector = detector.Detector()

# Weights for the crosswalk/street
street = 0
crosswalk = 0

cars_go = False
people_go = not cars_go

capN = cv2.VideoCapture(0)
capS = cv2.VideoCapture(1)
# filler = cv2.imread("filler.jpg")  # Filler image to test dealing with full 360 view

# Create search-zones where the detector will look for people in the image
searchzoneCWN = [0, 640, 40, 440]  # lowerX, upperX, lowerY, upperY
searchzoneCWS = [0, 640, 40, 440]

# Calculate the dimensions to resize the images by before concatination (Make heights the same)
"""
heightN = searchzoneCWN[3] - searchzoneCWN[2]
widthN = searchzoneCWN[1] - searchzoneCWN[0]
aspectN = widthN/heightN
heightS = searchzoneCWS[3] - searchzoneCWS[2]
widthS = searchzoneCWS[1] - searchzoneCWS[0]
aspectS = widthS/heightS
"""


# Count the number of objects that are people
def countpeople(objectslist):
    numberofpeople = 0
    for objct in objectslist:
        if objct[0] == "person":
            numberofpeople += 1
    return numberofpeople


counter = 0

ser = serial.Serial('COM3', 9600)
time.sleep(2)  # wait for the serial connection to initialize

print(capN.isOpened())
print(capS.isOpened())

while capN.isOpened() and capS.isOpened():

    # Get camera feed from each direction. With current x2 webcam setup, each image is 480x640
    _, frameN = capN.read()
    _, frameS = capS.read()
    # framePano = np.concatenate((frameN, frameS), axis=1)

    cv2.imshow("frameN", frameN)
    cv2.imshow("frameS", frameS)

    # Create new images soley of the search-zone
    frameSzN = frameN[searchzoneCWN[2]:searchzoneCWN[3], searchzoneCWN[0]:searchzoneCWN[1]]
    frameSzS = frameS[searchzoneCWS[2]:searchzoneCWS[3], searchzoneCWS[0]:searchzoneCWS[1]]

    # frameResizedN = cv2.resize(frameSzN, ())
    # frameResizedS = cv2.resize(frameSzN, ())

    objectsN = yolodetector.detect(frameSzN, False)
    objectsS = yolodetector.detect(frameSzS, False)

    peopleN = countpeople(objectsN)
    peopleS = countpeople(objectsS)

    if peopleN + peopleS > 0:
        people_go = True
        cars_go = False
        ser.write(b'S')
    else:
        people_go = False
        cars_go = True
        ser.write(b'G')

    key_code = cv2.waitKey(5) & 0xFF
    if key_code == 27:
        break

ser.close()
capN.release()
capS.release()
cv2.destroyAllWindows()
