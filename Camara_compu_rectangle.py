import cv2

cap = cv2.VideoCapture(0)

winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
while(1):
    #cap.open(url)
    ret,frame=cap.read()
    video=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    video2=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    print(video.shape)
    
    video=cv2.resize(frame,(100,200))
    H = video[: , : , 0]
    S = video[: , : , 1]
    V = video[: , : , 2]
    H[:,:]=130
    video[:,:,0]=H
    HSV=cv2.merge((H,S,V))
    video_1=cv2.cvtColor(HSV,cv2.COLOR_HSV2RGB)
    
    ancho=2
    alto=2
    video1=cv2.resize(frame,(0,0),frame,ancho,alto)
    R = video1[: , : , 0]
    G = video1[: , : , 1]
    B = video1[: , : , 2]
    G[:,:]=180
    video1[:,:,0]=G
    RGB=cv2.merge((R,G,B))

    
    video2=cv2.flip(frame,0)
    B_1 = video2[: , : , 0]
    G_1 = video2[: , : , 1]
    R_1 = video2[: , : , 2]
    B_1[:,:]=210
    video2[:,:,0]=B_1
    BGR=cv2.merge((B_1,G_1,R_1))
    video_3=cv2.cvtColor(BGR,cv2.COLOR_BGR2RGB)

    #cv2.rectangle(frame,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10)
    print(frame.shape)
    if ret:
        
        #frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        frame_2=cv2.flip(frame,1)
        cv2.rectangle(frame_2,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10)
        cv2.circle(frame_2,center=(320,240),radius=20,color=(255,120,110),thickness=5)
        cv2.circle(frame_2,center=(50,20),radius=20,color=(255,0,255),thickness=-1)
        cv2.line(frame_2,pt1=(0,0),pt2=(640,480),color=(120,120,120),thickness=5)
        fuente=cv2.FONT_ITALIC
        cv2.putText(frame_2,text="Hola mundo",org=(10,240),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow(winName, rct)
        cv2.imshow(winName, frame_2)
        
        frame2=cv2.flip(video_1,1)
        cv2.putText(frame2,text="HSV",org=(10,240),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        cv2.imshow("HSV", frame2)
        
        frame3=cv2.flip(RGB,1)
        cv2.putText(frame3,text="RGB",org=(10,240),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        cv2.imshow("RGB", frame3)
        
        cv2.imshow("BGR", video_3)
    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()