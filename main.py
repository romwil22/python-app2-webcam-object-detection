# PYTHON APP2 MOTION DETECTOR

import cv2, time

video = cv2.VideoCapture(0)
first_frame = None

while True:
    check, frame = video.read()

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.GaussianBlur(gray_image, (21, 21), 0)
    
    if(first_frame is None):
        first_frame = gray_image
        continue
    
    delta_frame_image = cv2.absdiff(first_frame, gray_image)

    cv2.imshow("gray image", gray_image)
    cv2.imshow("delta image", delta_frame_image)
    key = cv2.waitKey(1)
    
    if(key == ord("q")):
        break
    
video.release()
cv2.destroyAllWindows()