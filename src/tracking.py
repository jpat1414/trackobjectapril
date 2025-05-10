"""
Created on 5-10-2025
@author: Jenish
"""

from src.detection import *

# creating the ROI
roi = cv2.selectROI(frame, False)

# initializing the tracker with the first frame and the ROI
object_tracker.init(frame, roi)
if not object_tracker:
    raise Exception("tracker not initialized")

active = True