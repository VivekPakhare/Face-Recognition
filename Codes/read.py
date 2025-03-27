import cv2 as cv

vivek = cv.imread('vivek.jpg')
cv.imshow('vivek',vivek)


cv.waitKey(delay=0)
#reading videos 

capture = cv.VideoCapture('Videos/vido.mp4')

while True:
   isTrue , frame = capture.read()
    
   cv.imshow('video',frame) 
   if cv.waitKey(20) & 0xFF == ord('F1'):
       break
   
   
capture.release()

