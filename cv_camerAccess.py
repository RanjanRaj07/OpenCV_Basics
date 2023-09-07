import cv2
import sys

s = 0

#for multiple camera devices giving the camera ID by command line argument 
if len(sys.argv) > 1:
    s = sys.argv[1]

# Capture the video frames
source = cv2.VideoCapture(s)

# Open a window to display the captured frames
win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# Show the window data till the user presses the ESC key
while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

# Release the source and destroy the window
source.release()
cv2.destroyWindow(win_name)
