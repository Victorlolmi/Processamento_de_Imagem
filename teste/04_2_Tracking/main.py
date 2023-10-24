import numpy as np
import cv2
import os

def computeTracking(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #_, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#205    178	100
    lowerColor = np.array([[100], [200], [0]])
    upperColor = np.array([[150], [255], [255]])

    mask = cv2.inRange(hsvImage, lowerColor, upperColor)
    
    result = cv2.bitwise_and(frame, frame, mask = mask)

    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        maxArea = cv2.contourArea(contours[0])
        contourMaxAreaId = 0
        i = 0

        for cnt in contours:
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                contourMaxAreaId = i
            i += 1

        cntMaxArea = contours[contourMaxAreaId]

        x, y, w, h = cv2.boundingRect(cntMaxArea)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return frame, gray

def main():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()

        frame, gray = computeTracking(frame)

        cv2.imshow("Webcam", gray)
        cv2.imshow("Webcam2", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or 0xFF == 27:
            break
        if cv2.waitKey(1) & 0xFF == ord('q') or 0xFF == 27:
            break

    
    cap.release()
    cv2.destroyAllWindows()

main()
