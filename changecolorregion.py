import cv2 as cv
import numpy as np

def changeColorRegion(frame):
    image = cv.imread(frame)

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    lower_brown=np.array([10,100,20])
    upper_brown=np.array([20,255,200])
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    mask1 = cv.inRange(hsv, lower_brown, upper_brown)
    mask2 = cv.inRange(hsv, lower_green, upper_green)

    output = image.copy()
    yellow_color = np.array([0, 255, 255])
    aqua_color = np.array([255,255,0])
    output[mask1 > 0] = yellow_color
    output[mask2 > 0] = aqua_color
    
    cv.imshow('Original Image', image)
    cv.imshow('Changed Color Image', output)
    cv.waitKey(0)
    cv.destroyAllWindows()
