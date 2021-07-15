import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('Files/Photos/park.jpg')
'''cv.imshow('Origin', img)

#gray
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#hsv
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#LAB
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)
cv.waitKey(0)

rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()'''

#spliting color of image:
b,g,r=cv.split(img)
'''cv.imshow('Blue', b)
cv.imshow('Red', r)
cv.imshow('Green', g)'''
blank=np.zeros(img.shape[:2], dtype='uint8')
blue=cv.merge([b,blank,blank])
red=cv.merge([blank,blank,r])
green=cv.merge([blank,g,blank])
cv.imshow('Blue', blue)
cv.imshow('Red', red)
cv.imshow('Green', green)


print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

#merged image
merged=cv.merge([b,g,r])
cv.imshow('merged', merged)
print('merged shape:'+str(merged.shape))



cv.waitKey(0)