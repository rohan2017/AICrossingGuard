import cv2
from YOLO import detector

yololol = detector.Detector()

street1 = 0

cap1 = cv2.VideoCapture(0)

counter = 0
while cap1.isOpened():

    # get camera feed from each street
    _, frame1 = cap1.read()

    # process the image
    objects1 = yololol.detect(frame1, True)

    cv2.imshow("frame1", frame1)
    print(objects1)

    key_code = cv2.waitKey(5) & 0xFF
    if key_code == 27:
        break

cv2.destroyAllWindows()
