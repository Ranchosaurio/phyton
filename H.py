#Harris Algorithm
import cv2
import numpy as np
import matplotlib.pylab as plt

cap = cv2.VideoCapture(1)
winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)


while(1):
    ret,frame=cap.read()
    tab_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(tab_gray.shape)
    if ret:
        #print(imrgb.shape)
        dst=cv2.cornerHarris(src=tab_gray,blockSize=3,ksize=3,k=0.02) #ksize define la esquina y block incementra el tamaño de la esquina
        #Imagen fuente, tamaño considerado para la deteción,Parámetro de apertura de la derivada de Sobel utilizada, parametro del detector de harrys(presición)
        #Imagen fuente,tamaño del eelemnto,definición de la esquina, definición de forma del elemento
        dst=cv2.dilate(dst,None)
        #Operaciones morfológicas sirven para modificar la estructura de la imágen 
        frame[dst>0.05*dst.max()]=[0,255,0]
        #Si el resultado del algoritmo es mayor que 0.01 veces que el valor máximo, debe ser igual a color verde
    cv2.imshow("Chess",frame)
    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()