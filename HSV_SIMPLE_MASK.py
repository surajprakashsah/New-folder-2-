import cv2
import numpy as np

cap= cv2.VideoCapture(0)

kernel = np.ones((5,5),np.float32)/25
z=0
while(1):

    _,fr= cap.read()

    frame= fr.copy()

    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower= np.array([80,50,50])
    upper= np.array([100,255,255])

    mask = cv2.inRange(hsv,lower,upper)
    mask= cv2.medianBlur(mask,5)
    
    ret,thresh= cv2.threshold(mask,127,255,cv2.ADAPTIVE_THRESH_MEAN_C)
    contours,hierarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours)!=0:
        
        cnt= contours[4]

        res= cv2.bitwise_and(frame,frame,mask=mask)
        #res= cv2.drawContours(res,contours,cnt,(0,255,0),2)

        (x,y),radius= cv2.minEnclosingCircle(cnt)
        center= (int(x),int(y))
        radius= int(radius)
        img= cv2.circle(frame,center,radius,(0,255,0),2)

        if x-radius<40 or x+radius>600:
            print('out of bounds ',z)
            z=z+1
    

    cv2.imshow('frame',fr)
    cv2.imshow('mask',mask)
    cv2.imshow('result',img)

    k= cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
