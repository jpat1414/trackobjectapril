"""
Created on 5-10-2025
@author: Jenish
"""

from detection import *

# creating the ROI
roi = cv2.selectROI("Select ROI", frame, False)
print(f"Selected ROI: {roi}")

# initializing the tracker with the first frame and the ROI
object = object_tracker.init(frame, roi)
if not object:
    raise Exception("tracker not initialized")

box_color = (0, 0, 255)

# loop to read the video
active = True
while active:
    ret, frame = webcam.read()
    if not ret:
        break
    obj, bbox = object_tracker.update(frame)

    if obj:
        x, y, w, h = map(int, bbox)
        cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)
        cv2.putText(frame, "Tracking object", (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, box_color)
        output.write(frame)
    else:
        cv2.putText(frame, "Cannot track object", (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, box_color)

    # display the frame
    cv2.imshow("Object Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
webcam.release()    
