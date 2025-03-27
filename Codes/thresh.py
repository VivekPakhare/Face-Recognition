import cv2 as cv
import numpy as np


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)


#gray 
gray = cv.cvtColor(img,code=cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)



cv.waitKey(0)