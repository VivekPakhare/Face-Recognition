import cv2 as cv


img = cv.imread('Photos/Flower.jpg')

cv.imshow('image',img)



#grascale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray image',gray)

#blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur image',blur)

#edge cascade 
canny = cv.Canny(img,100,101)
cv.imshow('edge cascade',canny)

#resize image
resize = cv.resize(img,dsize=(500,400),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resize)

#crop image 
crop = resize[50:200,200:400]
cv.imshow('crop',crop)

cv.waitKey(0)