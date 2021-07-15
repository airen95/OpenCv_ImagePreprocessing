import cv2 as cv
img=cv.imread('Files/Photos/park.jpg')
cv.imshow('Img', img)

#gray
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur=cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edges_Canny
canny=cv.Canny(img, 125,175)
cv.imshow('Canny',canny)

#dilating
dilated=cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

#erode
eroded=cv.erode(dilated, (7,7), iterations=1)
cv.imshow('Erode',eroded)

#resize:
resize=cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resize)

#cropped:
crop=img[13:133,13:133]
cv.imshow('crop',crop)

cv.waitKey(0)