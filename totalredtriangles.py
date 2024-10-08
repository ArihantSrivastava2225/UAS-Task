import cv2 as cv
import numpy as np

def totalRed(image):
    frame=cv.imread(image)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_brown=np.array([10,100,20])
    upper_brown=np.array([20,255,200])
    lower_blue=np.array([90,50,50])
    upper_blue=np.array([130,255,255])
    lower_red1=np.array([0,100,100])
    upper_red1=np.array([10,255,255])
    lower_red2=np.array([160,100,100])
    upper_red2=np.array([180,255,255])
    mask1 = cv.inRange(hsv, lower_brown, upper_brown)
    mask2 = cv.inRange(hsv, lower_blue, upper_blue)
    mask3 = cv.inRange(hsv, lower_red1, upper_red1)
    mask4 = cv.inRange(hsv, lower_red2, upper_red2)
    combined_mask = cv.bitwise_or( mask3, mask4)
    result= cv.bitwise_and(frame, frame, mask=combined_mask)

    gray_img = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
    b=0
    _, thresh_image=cv.threshold(gray_img, 128, 255, cv.THRESH_BINARY)

    contours, heirarchy = cv.findContours(gray_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for i, contour in enumerate(contours):
        epsilon=0.01*cv.arcLength(contour, True)
        approx=cv.approxPolyDP(contour, epsilon, True)
        cv.drawContours(result, contour, 0, (0,0,0), 4)
        x,y,w,h=cv.boundingRect(approx)
        x_mid=int(x+w/3)
        y_mid=int(y+h/1.5)
        coords=(x_mid, y_mid)
        colour=(255,0,0)
        font=cv.FONT_HERSHEY_COMPLEX_SMALL
    
        if len(approx)==3:
            cv.putText(result, "Triangle", coords, font, 1, colour, 1)
            b+=1
    
    cv.waitKey(0)
    return b