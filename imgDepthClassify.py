import cv2
import numpy as np
import matplotlib.pylab as plt

def empty(a):
    pass

# Image extraction
path = 'resource/frame0549.jpg'
img = cv2.imread(path)

cv2.namedWindow("Track")
cv2.resizeWindow("Track",640,240)
cv2.createTrackbar("Hue min","Track",0,179,empty)
cv2.createTrackbar("Hue max","Track",179,179,empty)
cv2.createTrackbar("SAt min","Track",55,255,empty)
cv2.createTrackbar("SAt max","Track",255,255,empty)
cv2.createTrackbar("Val min","Track",111,255,empty)
cv2.createTrackbar("Val max","Track",255,255,empty)

while True:
    imgContour = img.copy()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min =cv2.getTrackbarPos("Hue min","Track")
    h_max =cv2.getTrackbarPos("Hue max","Track")
    s_min =cv2.getTrackbarPos("SAt min","Track")
    s_max =cv2.getTrackbarPos("SAt max","Track")
    v_min =cv2.getTrackbarPos("Val min","Track")
    v_max =cv2.getTrackbarPos("Val max","Track")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)


    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgContour, 1, 1)

    # cv2.imshow("video",imgContour)
    # if cv2.waitKey(1) & 0xFF==ord('q'):
    #     break

    # cv2.imshow("Original",imgCanny)
    # cv2.imshow("Canny",imgContour)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)