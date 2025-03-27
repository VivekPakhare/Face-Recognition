import cv2 as cv
import numpy as np 

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2],dtype='uint8')


mask = cv.circle(blank,(img.shape[1]//2-130,img.shape[0]//2-100),100,255,-1)


masked_image = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked image',masked_image)

cv.waitKey(0)
