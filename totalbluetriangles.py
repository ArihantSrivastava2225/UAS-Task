import cv2 as cv
import numpy as np

def totalBlue(image):
        
    frame=cv.imread(image)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue=np.array([90,50,50])
    upper_blue=np.array([130,255,255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    result= cv.bitwise_not(mask)

    _, thresh_img = cv.threshold(result, 220, 255, cv.THRESH_BINARY)

    b=0
    contours, heirarchy = cv.findContours(result, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
    # if i==0:
    #     continue #commenting this out because this was skipping our one array element with 0 index, i.e. it was also skipping one triangle
        epsilon=0.02*cv.arcLength(contour, True)
        approx=cv.approxPolyDP(contour, epsilon, True)
        # cv.drawContours(result, contour, 0, (0,0,0), 4)
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

# totalBlue('2.png') --testing success