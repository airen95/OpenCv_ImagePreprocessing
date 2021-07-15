import cv2 as cv
import numpy as np

'''blank=np.zeros((400,400), dtype='uint8')
rec=cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle=cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', rec)
cv.imshow('Circle', circle)

#Bitwise AND
bitwise_and=cv.bitwise_and(rec, circle)
cv.imshow('AND', bitwise_and)

#bitwise OR
bitwise_or=cv.bitwise_or(rec, circle)
cv.imshow('OR', bitwise_or)

#bitwise xor
bitwise_xor=cv.bitwise_xor(rec, circle)
cv.imshow('XOR', bitwise_xor)

#bitwise not
bitwise_not=cv.bitwise_not(rec)
cv.imshow('NOT', bitwise_not)'''

# MASKING
img=cv.imread('Files/Photos/cats.jpg')
img_2=cv.imread('Files/Photos/cats 2.jpg')
blank=np.zeros(img_2.shape[:2], dtype='uint8')
cv.imshow('Cat', img)
cv.imshow('Cat', img_2)

cv.imshow('Blank', blank)

mask=cv.circle(blank.copy(),(img_2.shape[1]//2,img_2.shape[0]//2), 100, 255,-1 )
cv.imshow('Blank mask',mask)
masked=cv.bitwise_and(img_2, img_2, mask=mask)
cv.imshow('IMG_masked', masked)

#weird_shape:
circle=cv.circle(blank.copy(),(img_2.shape[1]//2 +45,img_2.shape[0]//2+45), 100, 255,-1 )
rec=cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)
weird_shape=cv.bitwise_and(circle, rec)
cv.imshow('circle', circle)
cv.imshow('Rectangle', rec)
cv.imshow('weird', weird_shape)
mask_weird=cv.bitwise_and(img_2, img_2, mask=weird_shape)
cv.imshow('Mask_weird', mask_weird)



cv.waitKey(0)