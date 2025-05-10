"""
Created on 5-10-2025
@author: Jenish
"""

import cv2

# initializing the object tracker
object_tracker = cv2.TrackerMedianFlow.create()
webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()

# creating the ROI
roi = cv2.selectROI("Tracking", frame, False)

    