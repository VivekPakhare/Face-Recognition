import cv2 as cv

#reading images
img = cv.imread('Photos/lady.jpg')
cv.imshow('picture',img)


#function for rescaling video and images
def rescaleframe(frame , scale = 0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



resized_img = rescaleframe(img)
cv.imshow('vivek_resized', resized_img)
cv.waitKey(0)


#resclaing live videos
def ChangeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


#reading videos
capture = cv.VideoCapture('Videos/vido.mp4')

while True:
   isTrue , frame = capture.read()
   frame_resized = rescaleframe(frame,scale = .12)
  
   cv.imshow('Video',frame)
   cv.imshow('resized_frame',frame_resized) 
   if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows