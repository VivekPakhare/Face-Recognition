import cv2 as cv
import numpy as np

img = cv.imread('Photos/group 1.jpg')
cv.imshow('image',img)

blank = np.zeros(shape=img.shape,dtype='uint8')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)


canny = cv.Canny(img,125,175)
cv.imshow('canny',canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)