import cv2

cap = cv2.VideoCapture(0)

winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
while(1):
    ret,frame=cap.read()
    print(frame.shape)
    if ret:
        ret,frame=cap.read()
        rct = frame[200:250, 150:350]
        cv2.imshow(winName, rct)
        print(frame.shape)
        video=cv2.cvtColor(rct,cv2.COLOR_RGB2HSV)
        H = video[: , : , 0]
        S = video[: , : , 1]
        V = video[: , : , 2]
        H[:,:]=130
        video[:,:,0]=H
        HSV=cv2.merge((H,S,V))
        video_1=cv2.cvtColor(HSV,cv2.COLOR_HSV2RGB)
        cv2.imshow("buganvilia",video_1)

    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()