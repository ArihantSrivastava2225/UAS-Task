import cv2
import numpy as np

def housesinBurntGrass(image):
    image = cv2.imread(image)
    gray_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_brown=np.array([10,100,20])
    upper_brown=np.array([20,255,200])
    mask1 = cv2.inRange(hsv, lower_brown, upper_brown)
    result=cv2.bitwise_and(image, image, mask=mask1)
    _, thresh_image=cv2.threshold(mask1, 220, 255, cv2.THRESH_BINARY)
    
    contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    b=0
    for i, contour in enumerate(contours):
        if i==0:
            continue

        epsilon=0.04*cv2.arcLength(contour, True)
        approx=cv2.approxPolyDP(contour, epsilon, True)

    #   cv2.drawContours(mask1, contour, 0, (255,0,0), 4)

        x,y,w,h=cv2.boundingRect(approx)
        x_mid=int(x+w/3)
        y_mid=int(y+h/1.5)

        coords=(x_mid, y_mid)
        colour=(0,0,0)
        font=cv2.FONT_HERSHEY_DUPLEX

        if len(approx)==3:
            cv2.putText(mask1,"Triangle", coords, font, 1, colour, 1)
            b+=1
        
    cv2.waitKey(0)
    return b
