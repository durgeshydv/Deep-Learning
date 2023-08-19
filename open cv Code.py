
#OBJECT DETECTION USING OPENCV 



'''How can we detect which color it is and how can way say to the computer only 1 specific color
that is what we are going to see using opencv'''

import cv2 # package of AI 

import numpy as np

#Lets capture the camera. 0 for webcam. if you want other webcam then we can change to index to 1, 2 
cap = cv2.VideoCapture(0) 

#Lets load the frame 
while True:
    _, frame = cap.read() 
    
    
#we convert this format to hsv , bgr library this is color format red, green, blue, we are frame with hsv which use to select the color

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
# Lets frame on the windows   
    cv2.imshow("Frame", frame) 
    
# weight key event which is 1 and which is 27 then break the loop that means we are going to stop the loop
    key = cv2.waitKey(1)
    if key ==27:
        break

# Lets run this one and we will see the camera, camera is on 
######################################################################################################################

# using this code we can use only red color detection
# Only Red color detection

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([161, 155, 84]) # lowest hue would be - 161,155,84( how do i found this i tested before and found this) 
    high_red = np.array([179, 255, 255])
    #mask = cv2.inRange(hsv_frame, low_red, high_red) 
        
    red_mask = cv2.inRange(hsv_frame, low_red, high_red) #we create maskk on hsv frame and then low red or high red
    red = cv2.bitwise_and(frame, frame, mask=red_mask)


    cv2.imshow("Frame", frame) 
    #cv2.imshow('Red mask', mask) 
    cv2.imshow('Red', red)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break

#########################################################################################################################

#USING THIS CODE WE CAN DETECT ONLY BLUE COLOR
    # Only Blue color Detection


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    #Blue color 
    
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    cv2.imshow("Frame", frame) 
    cv2.imshow('Blue', blue)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break
    
#####################################################################################################################

# USING THIS LINE OF CODE WE CAN DETECT ONLY GREEN COLOR

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow("Frame", frame) 
    cv2.imshow('Green', green)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break


#########################################################################################################


# WE CAN DETETCT EVERY COLOR ACCEPT WHITE COLOR

# LETS TRY THE CODE 

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    #Every color except white
    low = np.array([0, 42, 0]) 
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame) 
    cv2.imshow('Result', result)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break
####################################################################