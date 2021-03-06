#Facial and eye detection using OPENCV API
import numpy as np
import cv2
from Tkinter import *

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#gets main camera for device
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    #converting image from one color space to another
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #to find faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #draw rectangle on detected faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        #detecting an eye within the face
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #putting a square around the eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 1)

    cv2.imshow('img',img)

    #pressing the esc key to exit window
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    


