import cv2 as cv

a = cv.CascadeClassifier("Codes/haarcascade_frontalface_default.xml")
b = cv.VideoCapture(0)

while True:
    c_rect,d_image = b.read()
    e = cv.cvtColor(d_image,cv.COLOR_BGR2GRAY)
    f =a.detectMultiScale(e, 1.3,6)
    
    for(x1,y1,w1,h1) in f:
        cv.rectangle(d_image,(x1,y1),(x1+w1,y1+h1),(255,255,0),5)
        
    cv.imshow("image",d_image)
    h = cv.waitKey(40) & 0xff
    if h == 40:
        break
    
b.release()
cv.destroyAllWindows()
    
    
    