#Caoimhe Harvey
#File deals with uploading and recognizing face in a picture
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#get image path from command line
imagePath = sys.argv[1] 

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#code to detect the faces
faces = faceCascade.detectMultiScale (
	gray,
	scaleFactor = 1.1,
	minNeighbors = 5,
	minSize = (30,30),
	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

print "Found {0} faces!".format(len(faces))

for (x,y,w,h) in faces:
	cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Faces Found: ", image)
cv2.waitKey(0)