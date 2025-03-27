import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank_img',blank)

blank[200:400 ,300:500]= 50,40, 100


#draw rectangle

cv.rectangle(blank,(0,0),(500,250),color=(0,255,0),thickness=-1)
cv.imshow('rectangle',blank)

#draw circle
cv.circle(blank,center=(blank.shape[1]//2,blank.shape[0]//2),radius=40,color=(100,150,200),thickness=-1)
cv.imshow('circle',blank)

#draw a line
cv.line(blank,(100,250),(300,400),color=(255,255,0),thickness=2)
cv.imshow('line',blank)

#text on image
cv.putText(blank,"hello my name is Vivek",(0,250),fontFace=cv.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2.1,color=(0,255,255),thickness=2)
cv.imshow('text',blank)


cv.waitKey(delay=0)
