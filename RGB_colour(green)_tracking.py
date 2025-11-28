import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    
    if ret:
        frame = cv2.flip(frame, 1)

        lower_green = np.array([0, 100, 0])
        upper_green = np.array([100, 255, 100])

        mask = cv2.inRange(frame, lower_green, upper_green)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500: 
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Green", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        cv2.imshow('maske' , mask)
    KInp = cv2.waitKey(1)
    
    if KInp == ord('q'): 
        break

vid.release()
cv2.destroyAllWindows()