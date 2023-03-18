from tracemalloc import start
import cv2
import time


def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
def mainn():
    cap = cv2.VideoCapture(8)
    #tracker = cv2.legacy.TrackerMOSSE_create()
    tracker = cv2.legacy.TrackerCSRT_create()
    success,img = cap.read()
    bbox = cv2.selectROI("Tracking",img,False)
    #print(bbox)
    #Get the length, width and height of the video
    #height,width,channel=img.shape
    #print(height,width,channel)
    #bbox = (138, 424, 239, 236)

    tracker.init(img,bbox)
    while True:
        timer = cv2.getTickFrequency()
        print(timer)
        success,img = cap.read()
        success,bbox = tracker.update(img)
        print(bbox)
        if success:
            drawBox(img,bbox)
        else:
            cv2.putText(img,"Lost", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
        fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
        cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
        cv2.imshow("1",img)
    
        if cv2.waitKey(1)&0xff == 27:
            break


mainn()
