import cv2

cap = cv2.VideoCapture(1)

winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
while(1):
    ret,frame=cap.read()
    print(frame.shape)
    if ret:
        ret,frame=cap.read()
    
        cv2.imshow(winName, frame)
        print(frame.shape)
        cv2.imshow("buganvilia",frame)

    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()