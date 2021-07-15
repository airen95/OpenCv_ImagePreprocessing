import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('Files/Photos/cats.jpg')
# gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# #masking
blank=np.zeros(img.shape[:2], dtype='uint8')
circle=cv.circle(blank.copy(), (img.shape[1]//2, img.shape[1]//2-100), 100, 255, -1)
img_mask=cv.bitwise_and(img, img, mask=circle)
cv.imshow('Image mask', img_mask)

# #grayscale the histogram
# #gray_hist=cv.calcHist([gray],[0], None,[256], [0,256])
# gray_hist=cv.calcHist([gray],[0],circle,[256], [0,256])



# plt.figure()
# plt.title('GrayScale History')
# plt.xlabel('Bins')
# plt.ylabel('# pixel')
# plt.plot(gray_hist)
# plt.show()

#Colour Histogram
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
color=['b','g','r']
for idx, col in enumerate(color):
    hist=cv.calcHist([img],[idx],circle,[256],[0,256])
    plt.plot(hist, color=col)
plt.show()




cv.waitKey(0)