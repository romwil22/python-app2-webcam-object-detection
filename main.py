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
    thresh_frame_image = cv2.threshold(delta_frame_image, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame_image = cv2.dilate(thresh_frame_image, None, iterations=2)
    
    (cnts, _) = cv2.findContours(thresh_frame_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        if (cv2.contourArea(c) < 1000):
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    print(x)
    print(y)
    print(w)
    print(h)
    
    cv2.imshow("gray image", gray_image)
    cv2.imshow("delta image", delta_frame_image)
    cv2.imshow("threshold image", thresh_frame_image)
    cv2.imshow("color image", frame)
    key = cv2.waitKey(1)
    
    if(key == ord("q")):
        break
    
video.release()
cv2.destroyAllWindows()