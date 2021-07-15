import cv2 as cv
img=cv.imread('Files/Photos/cats.jpg')
cv.imshow('Origin', img)

#Blurring techniques:
average=cv.blur(img, (3,3))
cv.imshow('Average',average)

gauss=cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Gaussian', gauss)

median=cv.medianBlur(img,3)
cv.imshow('Median', median)

bilateral=cv.bilateralFilter(img, 10, 35, 35)
cv.imshow('Bilateral',bilateral)








cv.waitKey(0)