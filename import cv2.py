import cv2

cap = cv2.VideoCapture(0)

winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
while(1):
    #cap.open(url)
    ret,frame=cap.read()
   
    rct = frame[200:250, 150:350]
    cv2.imshow(winName, rct)
    video=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    video2=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    print(video.shape)
        
    video=cv2.resize(rct,(400,500))
    H = video[: , : , 0]
    S = video[: , : , 1]
    V = video[: , : , 2]
    H[:,:]=50
    video[:,:,0]=H
    HSV=cv2.merge((H,S,V))
    video_1=cv2.cvtColor(HSV,cv2.COLOR_HSV2RGB)
    

    video1=cv2.resize(rct,(400,500))
    R = video1[: , : , 0]
    G = video1[: , : , 1]
    B = video1[: , : , 2]
    B[:,:]=70
    video1[:,:,0]=B
    RGB=cv2.merge((R,G,B))

    
    video2=cv2.resize(rct,(400,500))
    B_1 = video2[: , : , 0]
    G_1 = video2[: , : , 1]
    R_1 = video2[: , : , 2]
    B_1[:,:]=200
    video2[:,:,0]=B_1
    BGR=cv2.merge((B_1,G_1,R_1))
    video_3=cv2.cvtColor(BGR,cv2.COLOR_BGR2RGB)

        #cv2.rectangle(frame,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10)
    print(frame.shape)
    if ret:
        fuente=cv2.FONT_ITALIC
        gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow(winName, frame)
        cv2.putText(video_1,text="HSV",org=(10,240),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        cv2.imshow("HSV", video_1)
        
        cv2.putText(RGB,text="RGB",org=(10,240),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        cv2.imshow("RGB", RGB)

        cv2.putText(video_3,text="BGR",org=(10,240),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        cv2.imshow("BGR", video_3)
    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()
