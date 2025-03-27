import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')



#translation

def traslate(img,x,y):
    transMat =np.float32([[1,0,x],[0,1,y]])
    dimentions =(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimentions)


translated = traslate(img,-200,-200)
cv.imshow('traslated',translated)

    
# -x = left
# -y = up
# x = right
# y = down 

#roatated
def rotation(img,angel,rotpoint = None):
    (height,weidth) = img.shape[:2]
    
    if rotpoint is None:
        rotpoint = (weidth//2 ,height//2)
        
    rotMat = cv.getRotationMatrix2D(rotpoint,angel,1.0)
    dimentions = (weidth,height)
    
    return cv.warpAffine(img,rotMat,dimentions)

rotate = rotation(img,45)
cv.imshow('rotare',rotate)


#flipping image

flip = cv.flip(img,-1)
cv.imshow('fliped',flip)
    
    
    
    

cv.waitKey(0)
