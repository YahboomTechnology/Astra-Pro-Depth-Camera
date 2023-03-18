import cv2
import numpy as np

print("Press the "ESC" key to end the program")
cap=cv2.VideoCapture(8)
while cap.isOpened():
# Get every frame
    ret,frame=cap.read()
    frame_ = cv2.GaussianBlur(frame,(5,5),0)
# Convert to HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# Threshold for color - blue
    lower_red=np.array([100, 43, 46])
    upper_red=np.array([124, 255, 255])
# Build a mask based on the threshold
    mask=cv2.inRange(hsv,lower_red,upper_red) 
    mask = cv2.erode(mask,None,iterations=2)
    mask = cv2.dilate(mask,None,iterations=2)
    mask = cv2.GaussianBlur(mask,(3,3),0) 
# Find contours
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2] 
    if len(cnts) > 0:
        cnt = max (cnts, key = cv2.contourArea)
        (color_x,color_y),color_radius = cv2.minEnclosingCircle(cnt)
        if color_radius > 10:
            cv2.circle(frame,(int(color_x),int(color_y)),int(color_radius),(255,0,255),2)
# Perform bitwise operations on original image and mask
    res=cv2.bitwise_and(frame,frame,mask=mask)
# Display image
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
#cap.release()    #Turn off camera
# Close the window
cv2.destroyAllWindows()

