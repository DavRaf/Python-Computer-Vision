# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:37:22 2019

@author: David
"""

import cv2

class EyeTracker:
    def __init__(self, faceCascadePath, eyeCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
        self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)
        
    def track(self, image, scaleFactor = 1.2, minNeighbors = 5, minSize = (30, 30)):
        faceRects = self.faceCascade.detectMultiScale(image, scaleFactor = scaleFactor, minNeighbors = minNeighbors, minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)
        rects = []
        for (fX, fY, fW, fH) in faceRects:
            faceROI = image[fY:fY + fH, fX:fX + fW]
            rects.append((fX, fY, fX + fW, fY + fH))
            
            eyeRects = self.eyeCascade.detectMultiScale(faceROI, scaleFactor = scaleFactor, minNeighbors = 10, minSize = (20, 20), flags = cv2.CASCADE_SCALE_IMAGE)
            for (eX, eY, eW, eH) in eyeRects:
                rects.append((fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))
        return rects