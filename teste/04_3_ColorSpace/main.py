import numpy as np
import cv2
import os

def onChange(val):
    pass

def computeTracking(frame, min_hue, min_sat, min_val, max_hue, max_sat, max_val):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #_, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerColor = np.array([[min_hue], [min_sat], [min_val]])
    upperColor = np.array([[max_hue], [max_sat], [max_val]])

    mask = cv2.inRange(hsvImage, lowerColor, upperColor)
    
    result = cv2.bitwise_and(frame, frame, mask = mask)

    '''gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

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

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)'''

    return mask

def main():
    cap = cv2.VideoCapture(0)

    trackbarWindow = "trackbarWindow"
    cv2.namedWindow("trackbarWindow")

    cv2.createTrackbar("Min Hue", trackbarWindow, 0, 255, onChange)
    cv2.createTrackbar("Max Hue", trackbarWindow, 255, 255, onChange)

    cv2.createTrackbar("Min Sat", trackbarWindow, 0, 255, onChange)
    cv2.createTrackbar("Max Sat", trackbarWindow, 255, 255, onChange)

    cv2.createTrackbar("Min Val", trackbarWindow, 0, 255, onChange)
    cv2.createTrackbar("Max Val", trackbarWindow, 255, 255, onChange)

    while True:
        success, frame = cap.read()

        min_hue = cv2.getTrackbarPos("Min Hue", trackbarWindow)
        max_hue = cv2.getTrackbarPos("Max Hue", trackbarWindow)

        min_sat = cv2.getTrackbarPos("Min Sat", trackbarWindow)
        max_sat = cv2.getTrackbarPos("Max Sat", trackbarWindow)

        min_val = cv2.getTrackbarPos("Min Val", trackbarWindow)
        max_val = cv2.getTrackbarPos("Max Val", trackbarWindow)

        result = computeTracking(frame, min_hue, min_sat, min_val, max_hue, max_sat, max_val)

        cv2.imshow("Webcam", result)
        #cv2.imshow("Webcam2", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or 0xFF == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

main()
