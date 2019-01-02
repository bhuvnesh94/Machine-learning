#!/usr/bin/python3
#importing libraries to be used
#importing opencv library
import cv2 
#importing numpy for matrix operations
import numpy as np

#starting camera
camera=cv2.VideoCapture(0)

while True:

    status,frame=camera.read()
    #Capture only color frames
    red_img=cv2.inRange(frame,(0,0,60),(40,40,255))
    blue_img=cv2.inRange(frame,(60,0,0),(255,0,0))
# numpy.ones(shape, dtype=None, order='C')  Return a new array of given shape and type, filled with ones. Order define whether to store given array in row major order i.e. C or in column major order i.e. F.
# dtype is data_type i.e. uint8
    kernal = np.ones((5,5), "uint8")
# cv2.dilate
    red=cv2.dilate(red_img, kernal)
    blue=cv2.dilate(blue_img, kernal)

# taking bit wise AND of the frames
    res_red=cv2.bitwise_and(frame,frame, mask=red_img)
    res_blue=cv2.bitwise_and(frame,frame,mask=blue_img)
