#Harris Algorithm
import cv2
import numpy as np
import matplotlib.pylab as plt
 
cap = cv2.VideoCapture(0)
winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
ret,frame=cap.read()
def carga_imagen(x):
    
    tab_BGR = cv2.imread(x)
    tab_gray = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2GRAY)
    tab_RGB = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2RGB)
    return tab_gray,tab_RGB,tab_BGR


while(1): 
    if ret:
        imgray,imbgr,imgrgb=carga_imagen(frame)
        #print(imrgb.shape)
        dst=cv2.cornerHarris(src=imgray,blockSize=3,ksize=3,k=0.04)
        #Imagen fuente, tamaño considerado para la deteción,Parámetro de apertura de la derivada de Sobel utilizada, parametro del detector de harrys(presición)
        #Imagen fuente,tamaño del eelemnto,definición de la esquina, definición de forma del elemento
        dst=cv2.dilate(dst,None)
        #Operaciones morfológicas sirven para modificar la estructura de la imágen 
        imgrgb[dst>0.01*dst.max()]=[0,255,0]
        #Si el resultado del algoritmo es mayor que 0.01 veces que el valor máximo, debe ser igual a color verde
        cv2.imshow("Chess",imgrgb)
        cv2.waitKey(0)


        cv2.imshow("BGR", frame)
    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()