#!/usr/bin/python3

import cv2

#starting camera
     # 0 for default camera, 1 for external camera
cap=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('face.xml') #using cascade classifier to add face data in xml format

while cap.isOpened():
    status=cap.read()[0]
    frame=cap.read()[1]
    cv2.imshow('live',frame)
    print(status)
      #0xFF takes keyboard input #ord covertes in ascii
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
