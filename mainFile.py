import cv2
import numpy as np

cap = cv2.VideoCapture("resource/project.avi")


def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",10,200,empty)
cv2.createTrackbar("Threshold2","Parameters",10,200,empty)
cv2.createTrackbar("Area","Parameters",0,500,empty)
cv2.createTrackbar("width","Parameters",1,10,empty)


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getCountour(img):
    countour,hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in countour:
        (x,y,w,h) = cv2.boundingRect(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if cv2.contourArea(cnt)<areaMin:
            continue
        widthMin = cv2.getTrackbarPos("width", "Parameters")
        if h > widthMin*w:
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)

while True:
    success, img = cap.read()
    if img is None:
        break
    imgContour = img.copy()

    # Colour extraction
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([0,157,9])
    upper = np.array([179,255,255])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgColour = cv2.bitwise_and(img,img,mask=mask)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    imgCanny = cv2.Canny(imgColour,threshold1,threshold2)
    kernel = np.ones((5, 5))
    getCountour(imgCanny)
    imgStack = stackImages(0.5,([img,mask],
                                [imgCanny,imgContour]))
    cv2.imshow("Result", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
