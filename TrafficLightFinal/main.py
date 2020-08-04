import cv2
from YOLO import detector

yolodetector = detector.Detector()

# Weights for each street
street1 = 0
street2 = 0
street3 = 0

# time delays for each street
time1 = 0
time2 = 0
time3 = 0

street1Go = False
street2Go = False
street3Go = False

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
# cap3 = cv2.VideoCapture(2)

counter = 0
street = 0
while cap1.isOpened() and cap2.isOpened():

    if counter % 2 == 0:
        # get camera feed from each street
        _, frame1 = cap1.read()
        _, frame2 = cap2.read()
        _, frame3 = cap2.read()
        cv2.imshow("original", frame1)
        height, width, channels = frame1.shape

        print(height)
        print(width)

        w = round(width / 3)
        w2 = 2 * w

        cv2.imshow("left", frame1)
        cv2.imshow("middle", frame2)
        cv2.imshow("right", frame3)

        # process the images
        objects1 = yolodetector.detect(frame1)

        objects2 = yolodetector.detect(frame2)

        objects3 = yolodetector.detect(frame3)

        # Add factors to the weights
        time1 += 2
        time2 += 2
        time3 += 2

        street1 = len(objects1) * time1
        street2 = len(objects2) * time2
        street3 = len(objects3) * time3

        # Determine which street has the biggest weight and choose that one
        print(street1)
        print(street2)
        print(street3)

        if street1 >= street2 and street1 >= street3:
            time1 = 0
            street = 1

        elif street2 >= street3 and street2 >= street1:
            time2 = 0
            street = 2

        elif street3 >= street2 and street3 >= street1:
            time3 = 0
            street = 3

    if street == 1:
        street1Go = True
        street2Go = False
        street3Go = False

    elif street == 2:
        street2Go = True
        street1Go = False
        street3Go = False

    elif street == 3:
        street3Go = True
        street1Go = False
        street2Go = False

    print("1: " + str(street1Go))
    print("2: " + str(street2Go))
    print("3: " + str(street3Go))

    key_code = cv2.waitKey(5) & 0xFF
    if key_code == 27:
        break

cv2.destroyAllWindows()
