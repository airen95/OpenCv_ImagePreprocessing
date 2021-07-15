import cv2 as cv
import numpy as np
img=cv.imread('Files/Photos/cats.jpg')

#1.gray
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#2.canny the blur to reduce the found contours
blur=cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny=cv.Canny(blur,125, 175 )
cv.imshow('canny',canny)

#2. Using threshold
ret, thresh=cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Thres', thresh)
blank=np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

#3.contour
#3.1 find contourskathbươxy lam truong
_,contours, hierarchies=cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#_,contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

print('%d contours found' %len(contours))

#3.2 draw contours

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('Contours',blank)




cv.imshow('Origin',img)
cv.waitKey(0)