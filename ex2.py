import cv2 as cv
import numpy as np

img=cv.imread('Files/Photos/park.jpg')
c,r=img.shape[:2]

#translate
def translate(img, x, y):
    dimensions=(img.shape[:2])
    mat1=np.array([[1,0,x],[0,1,y]], dtype=np.float32)
    return cv.warpAffine(img,mat1,dimensions)

img_trans=translate(img, 130,-100)
cv.imshow('Translate',img_trans)

def rotation (img, angle, root=None):
    y,x=img.shape[:2]
    if root is None:
        root=(x//2, y//2)
    rotMat=cv.getRotationMatrix2D(center=root, angle=angle, scale=1)
    return cv.warpAffine(img, rotMat,(x,y))

img_rot=rotation(img, -45)
cv.imshow('Rotate',img_rot)

#resize:
img_resize=cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resize',img_resize)

#flip

img_flip=cv.flip(img, 1)
cv.imshow('Flip', img_flip)

cv.imshow('Original',img)
cv.waitKey(0)
