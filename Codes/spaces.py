import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Photos/group 2.jpg')
cv.imshow('image',img)

#gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)


#bgr to lab
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#bgr to rgb
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

#visualization
plt.imshow(rgb)
plt.show()

cv.waitKey(0)