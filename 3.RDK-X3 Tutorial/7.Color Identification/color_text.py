import os
import cv2
import numpy as np

#Classification and definition of color---HSV
plate_type = ["black","gray","white","red","red2","orange","yellow","green","cyan","blue","purple"]
color_dict = dict()

lower_black_hsv = np.array([0, 0, 0])
upper_black_hsv = np.array([180, 255, 46])

lower_gray_hsv = np.array([0, 0, 46])
upper_gray_hsv = np.array([180, 43, 220])

lower_white_hsv = np.array([0, 0, 221])
upper_white_hsv = np.array([180, 30, 255])

lower_red_hsv = np.array([0, 43, 46])
upper_red_hsv = np.array([10, 255, 255])
lower_red2_hsv = np.array([156, 43, 46])
upper_red2_hsv = np.array([180, 255, 255])

lower_orange_hsv = np.array([11, 43, 46])
upper_orange_hsv = np.array([25, 255, 255])

lower_yellow_hsv = np.array([26, 43, 46])
upper_yellow_hsv = np.array([34, 255, 255])

lower_green_hsv = np.array([35, 43, 46])
upper_green_hsv = np.array([77, 255, 255]) 

lower_cyan_hsv = np.array([78, 43, 46])
upper_cyan_hsv = np.array([99, 255, 255]) 

lower_blue_hsv = np.array([100, 43, 46])
upper_blue_hsv = np.array([124, 255, 255])
 
lower_purple_hsv = np.array([125, 43, 46])
upper_purple_hsv = np.array([155, 255, 255])



color_dict['black'] = [lower_black_hsv, upper_black_hsv]
color_dict['gray'] = [lower_gray_hsv, upper_gray_hsv]
color_dict['white'] = [lower_white_hsv, upper_white_hsv]
color_dict['red'] = [lower_red_hsv, upper_red_hsv]
color_dict['red2'] = [lower_red2_hsv, upper_red2_hsv]
color_dict['orange'] = [lower_orange_hsv, upper_orange_hsv]
color_dict['yellow'] = [lower_yellow_hsv, upper_yellow_hsv]
color_dict['green'] = [lower_green_hsv, upper_green_hsv]
color_dict['cyan'] = [lower_cyan_hsv, upper_cyan_hsv]
color_dict['blue'] = [lower_blue_hsv, upper_blue_hsv]
color_dict['purple'] = [lower_purple_hsv, upper_purple_hsv]



#(array, dictionary, string)
def color_shibei(color_hsv,dictpp,color_str):
    if color_hsv[0] >= dictpp[color_str][0][0] and color_hsv[0] <= dictpp[color_str][1][0] :
        if color_hsv[1] >= dictpp[color_str][0][1] and color_hsv[1] <= dictpp[color_str][1][1] :
            if color_hsv[2] >= dictpp[color_str][0][2] and color_hsv[2] <= dictpp[color_str][1][2] :  
                return color_str
    return "Unkown"



change_X = 75   #change detection area
change_Y = -50  #change detection area

#while cap.isOpened():
while 1:
    frame = cv2.imread("./test.png")
    #Flip the image frame (because the opencv image is reversed from our normal
    frame=cv2.flip(src=frame,flipCode=2)
    hsv_frame=cv2.cvtColor(src=frame,code=cv2.COLOR_BGR2HSV)
    #Get the height and width of the read frame
    height,width,channel=frame.shape
    # print(height,width)
    #Get the location of the detection point
    cx = width // 2 + change_X
    cy=height//2 + change_Y
    
    #Draw detection area
    cv2.rectangle(img=frame,pt1=(cx-10,cy-10),pt2=(cx+10,cy+10),color=(0,255,0),thickness=2)
    #cv2.putText(img=frame,text='detect locate',org=(width//2-width//4,height//2-20),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                #fontScale=1.0,color=(0,255,0),thickness=2)
    #Get the hue value hue of hsv
    pixel_center=hsv_frame[cy,cx]

    color='Unknow'
    hue_value=pixel_center[0]

    for i in range(len(plate_type)):
        color = color_shibei(pixel_center,color_dict,plate_type[i])
        if color == plate_type[i]:
            break

    if color == "red2":
        color = "red"
    #Get the object color at the detected position
    b,g,r=int(frame[cy,cx][0]),int(frame[cy,cx][1]),int(frame[cy,cx][2])
    #Draw text
    cv2.putText(img=frame,text=color,org=(cx-30,cy-20),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.0,color=(0,255,0),thickness=2)
    cv2.circle(img=frame,center=(cx,cy),radius=5,color=(0,255,0),thickness=3)

    cv2.imshow('frame',frame)
    key=cv2.waitKey(1)
    if key==27:
        break
    

# #Image reading and scaling
# img=cv2.imread('images/1.png')
# img=cv2.resize(src=img,dsize=(450,450))
# #Display image
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if __name__ == '__main__':
    print('end of program')
