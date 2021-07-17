import numpy as np
import cv2 as cv
import os
people=[i for i in os.listdir('Files/Faces/train')]
haar_cascade=cv.CascadeClassifier('Detect_Face/haar_face.xml')
face_reg=cv.face.createLBPHFaceRecognizer()
face_reg.load('face_trained.yml')

img=cv.imread('/home/tonlee/Desktop/Practice/Open_CV/Files/Faces/val/ben_afflek/1.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#1.Detect face and extract roi
face_rect=haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in face_rect:
    face_roi=gray[y:y+h, x:x+w]
#2.regconize face:
    label, confidence=face_reg.predict(face_roi)
    print('This is: '+str(people[label]))

    cv.putText(img,str(people[label]), (20,20),cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0),2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0,), 2)
cv.imshow('trained', img)
cv.waitKey(0)