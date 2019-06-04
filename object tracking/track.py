# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:30:55 2019

@author: David
"""

import numpy as np
import cv2

color_lower = np.array([100, 67, 0], dtype = "uint8")
color_upper = np.array([255, 128, 50], dtype = "uint8")

camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read()
    
    if not grabbed:
        break
    
    threshold_image = cv2.inRange(frame, color_lower, color_upper)
    threshold_image = cv2.GaussianBlur(threshold_image, (3,3), 0)
    (_, cnts, _) = cv2.findContours(threshold_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(cnts) > 0:
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
        
    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", threshold_image)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()