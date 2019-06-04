# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:27:47 2019

@author: David
"""

from facedetector import FaceDetector
import cv2
import os

"""
folder = 'images'
for image_path in os.listdir(folder):
    image = cv2.imread(folder + "\\" + image_path)
    # cv2.imshow("Image", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fd = FaceDetector("cascades\\haarcascade_frontalface_default.xml")
    faceRects = fd.detect(gray, scaleFactor = 1.2)
    print("I found {} face(s)".format(len(faceRects)))
    for (x, y, w, h) in faceRects:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Faces", image)
    cv2.waitKey(0)
"""
    
camera = cv2.VideoCapture(0)
fd = FaceDetector("cascades\\haarcascade_frontalface_default.xml")
while True:
    (grabbed, frame) = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceRects = fd.detect(gray)
    print("I found {} face(s)".format(len(faceRects)))
    for (x, y, w, h) in faceRects:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Faces", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()