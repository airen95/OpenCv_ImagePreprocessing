import cv2 as cv
import numpy as np

# img=cv.imread('Files/Photos/cats.jpg')
# cv.imshow('Cats',img)
# gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #simple threshold
# threshold, thresh= cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# cv.imshow('Simple Thres', thresh)

# threshold_inv, thresh_inv=cv.threshold(gray, 150, 255, cv.THRESH_TOZERO_INV)
# cv.imshow('Simple Thres Invert', thresh_inv)

# #adaptive threshold
# adaptive_thresh=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# cv.imshow('Adaptive thresh Mean', adaptive_thresh)
# adaptive_thresh_gauss=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 5)
# cv.imshow('Adaptive thresh Gauss', adaptive_thresh_gauss)

# Gradient and Edges

img=cv.imread('Files/Photos/lady.jpg')
#blur=cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Laplacian
laplacian=cv.Laplacian(gray, cv.CV_64F)
lap=np.uint8(np.absolute(laplacian))
cv.imshow('laplacian', lap)
print(laplacian)

#Sobel
sobel_x=cv.Sobel(gray, cv.CV_64F,1,0)
sobel_y=cv.Sobel(gray, cv.CV_64F,0,1)
sobel_combine=cv.bitwise_or(sobel_x, sobel_y)

cv.imshow('Sobel x', sobel_x)
cv.imshow('Sobel y', sobel_y)
cv.imshow('Sobel combine', sobel_combine)

#Canny
canny=cv.Canny(gray,150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)