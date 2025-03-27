import cv2 as cv
import numpy as np 


img = cv.imread('Photos/park.jpg')
#median blur 
median = cv.medianBlur(img,3)
cv.imshow('median',median)

#blur
blur = cv.blur(img,(3,3))
cv.imshow('blur',blur)

#average blur
avg_blur = cv.average
