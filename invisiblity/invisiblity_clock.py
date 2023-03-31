import cv2
import numpy as np

video = cv2.VideoCapture("Projects/invisiblity clock/free green screen effects - people - woman running 5 - free use.mp4")
image = cv2.imread("Projects/invisiblity clock/3D-Beach-Backgrounds-HD-Download-desktop-wallpapers-amazing-background-photos-download-free-best-apple-picture-2560x1440-1024x576.jpg")

def nothing():
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",300,300)

cv2.createTrackbar("L-H","Trackbars",32,255,nothing)
cv2.createTrackbar("L-S","Trackbars",94,255,nothing)
cv2.createTrackbar("L-V","Trackbars",132,255,nothing)
cv2.createTrackbar("U-H","Trackbars",179,255,nothing)
cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
cv2.createTrackbar("U-V","Trackbars",255,255,nothing)

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H","Trackbars")
    l_s = cv2.getTrackbarPos("L-S","Trackbars")
    l_v = cv2.getTrackbarPos("L-V","Trackbars")
    u_h = cv2.getTrackbarPos("U-H","Trackbars")
    u_s = cv2.getTrackbarPos("U-S","Trackbars")
    u_v = cv2.getTrackbarPos("U-V","Trackbars")

    l_g = np.array([l_h,l_s,l_v])
    u_g = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_g, u_g)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    f = frame-res
    green_screen = np.where(f==0,image,f)
    #cv2.imshow("Frame",frame)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("RES",res)
    #cv2.imshow("prefinal",f)
    cv2.imshow("Final",green_screen)
    k=cv2.waitKey(5)
    if k == ord('q'):
        break

video.release()
cv2.distroyAllWindows()