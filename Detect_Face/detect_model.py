import cv2 as cv

img=cv.imread('Files/Photos/group 1.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Lady Gray', gray)

#reading Haar
haar_cascade=cv.CascadeClassifier('Detect_Face/haar_face.xml')
#return a box surrounding face
face_rect=haar_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=1)
print('Number of faces found %d' %(len(face_rect)))

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0),1)
cv.imshow('Detect',img)

cv.waitKey(0)