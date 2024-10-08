import cv2 as cv
import numpy as np

def redhousesinBurntGrass(image):
    frame=cv.imread(image)
    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # gray_img=cv.cvtColor(hsv, cv.COLOR_BGR2GRAY)
    lower_brown=np.array([10,100,20])
    upper_brown=np.array([20,255,200])
    lower_blue=np.array([100,150,0])
    upper_blue=np.array([140,255,255])
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    lower_red1=np.array([0,100,100])
    upper_red1=np.array([10,255,255])
    lower_red2=np.array([160,100,100])
    upper_red2=np.array([180,255,255])
    
    img=frame.copy()
    mask1=cv.inRange(hsv, lower_brown, upper_brown)
    mask2=cv.inRange(hsv, lower_blue, upper_blue)
    mask3=cv.inRange(hsv, lower_green, upper_green)
    mask4 = cv.inRange(hsv, lower_red1, upper_red1)
    mask5 = cv.inRange(hsv, lower_red2, upper_red2)
    combined_red = cv.bitwise_or(mask4, mask5)
    brown_color=np.array([50,100,150])
    black_color=np.array([0,0,0])
    # img[mask2 > 0] = brown_color
    # img[mask3 > 0] = black_color
    # cv.imshow('img', img)
  
    _, thresh_img=cv.threshold(mask1, 220, 255, cv.THRESH_BINARY)
    
    # contours, heirarchy = cv.findContours(thresh_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours, heirarchy = cv.findContours(thresh_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    b=0
    for i, contour in enumerate(contours):
        epsilon=0.04*cv.arcLength(contour, True)
        approx=cv.approxPolyDP(contour, epsilon, True)
        # cv.drawContours(thresh_img, contour, 0, (0,0,0), 4)
        x,y,w,h=cv.boundingRect(approx)
        x_mid=int(x+w/3)
        y_mid=int(y+h/1.5)
        coords=(x_mid, y_mid)
        colour=(0,0,255)
        font=cv.FONT_HERSHEY_COMPLEX_SMALL
    
        if len(approx)==3:
            cv.putText(thresh_img, "Triangle", coords, font, 1, colour, 1)
            b+=1
    cv.imshow('final', thresh_img)
    print(b)
    cv.waitKey(0)
    return b

redhousesinBurntGrass('1.png')
