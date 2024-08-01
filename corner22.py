#Harris Algorithm
import cv2
import numpy as np
import matplotlib.pylab as plt

cap = cv2.VideoCapture(0)
winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)


while(1):
    ret,frame=cap.read()
    tab_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(tab_gray.shape)
    if ret:
        esquinas=cv2.goodFeaturesToTrack(tab_gray,15,0.08,10) #primera el numero de esquinas, segundo se necesita que sea menor a 1, tercer parametro
        #tercer parametro presicion y ell cuarto convierte parametros de hasta 64 bits  
        #Imagen, numero de puntos, detección fina < 1, precisión
        #esquinas=cv2.goodFeaturesToTrack(imgray,500,0.09,10)
        esquinas=np.int64(esquinas)
        for i in esquinas:
            x,y=i.ravel()
            cv2.circle(frame,(x,y),10,(255,0,255),1) #corrimiento de x y y 


    cv2.imshow("Chess",frame)
    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()