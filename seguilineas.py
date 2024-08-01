#Harris Algorithm
import cv2
import numpy as np
import matplotlib.pylab as plt
import cv2
import RPi.GPIO as GPIO
import os
import time
#DEFINIR NOMBRES
GPIO.setmode(GPIO.BCM)
ena=13
enb=15
M1 = 12
M2 = 11
#CONFIGURAR PINES SEGUN EL MICRO
GPIO.setmode(GPIO.BCM)
#CONFIGURAR PINES COMO SALIDA
GPIO.setup(M1,GPIO.OUT)
GPIO.setup(M2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
#PWM
pwm_1=GPIO.PWM(ena,500)
pwm_2=GPIO.PWM(enb,500)
#inicializar pwm 
pwm_1.start(0)
pwm_2.start(0)

cap = cv2.VideoCapture(0)

winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
while(1):
    ret,frame=cap.read()
    img_dist=cv2.medianBlur(frame,9)
    bordes=cv2.Canny(frame,threshold1=0,threshold2=120)
    bordes_1=cv2.Canny(img_dist,threshold1=200,threshold2=120)
    med_valor=np.median(frame)
    lower=int(max(0,0.7*med_valor))
    upper=int(max(255,1.3*med_valor))
    bordes_2=cv2.Canny(img_dist,threshold1=lower,threshold2=upper)
    bordes_3=cv2.Canny(frame,threshold1=lower,threshold2=upper)
    countours_b,jerarqui_b=cv2.findContours(bordes_1,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,countours_b,-1,(0,255,0),3)
    if len(countours_b) > 0:
        contours_data = np.vstack(countours_b).reshape(-1, 2)
        np.savetxt('contours_data.txt', contours_data, fmt='%d', delimiter=', ')
    cv2.drawContours(frame, countours_b, -1, (0, 255, 0), 3)
    cv2.imshow("Imagen",frame)

        # Calcular el centroide de los contornos en el eje X
    centroid_x = int(np.mean(contours_data[:, 0]))

        # Calcular el centro de la imagen
    centro_imagen_x = frame.shape[1] // 2

        # Definir un rango de tolerancia alrededor del centro
    rango_tolerancia = 45  # Ajusta este valor según sea necesario

        # Comparar con el centro de la imagen y el rango de tolerancia
    if centro_imagen_x - rango_tolerancia < centroid_x < centro_imagen_x + rango_tolerancia:
            print("Los contornos están en el centro.")
            GPIO.output(M1,True)
            GPIO.output(M2,True)
    elif centroid_x < centro_imagen_x - rango_tolerancia:
            print("Los contornos están a la izquierda.")
            GPIO.output(M1,False)
            GPIO.output(M2,True)
    elif centroid_x > centro_imagen_x + rango_tolerancia:
            print("Los contornos están a la derecha.")
            GPIO.output(M1,True)
            GPIO.output(M2,False)
    cv2.drawContours(frame, countours_b, -1, (0, 255, 0), 3)

    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()