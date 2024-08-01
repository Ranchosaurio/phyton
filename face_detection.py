#Fuerza bruta con ORB descriptors
import cv2
import numpy as np
import matplotlib.pylab as plt

def carga_imagen(x):
    tab_BGR = cv2.imread(x)
    tab_gray = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2GRAY)
    tab_RGB = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2RGB)
    return tab_gray,tab_RGB,tab_BGR
def detect_face(img):
    face_cascade=cv2.CascadeClassifier('data/haarcascades_cuda/haarcascade_eye.xml')
    #face_cascade=cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
    #face_cascade=cv2.CascadeClassifier('data/haarcascades_cuda/haarcascade_smile.xml')
    face_img=img.copy()
    face_rectangle=face_cascade.detectMultiScale(face_img)

    for(x,y,w,h) in face_rectangle:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,0,0),5)
    return face_img

imgray,imbgr,imgrgb=carga_imagen("pelon.jpg")
imgray_1,imbgr_1,imgrgb_1=carga_imagen("nina.jpg")
deteccion=detect_face(imgrgb)
deteccion_1=detect_face(imgrgb_1)
#cv2.imshow("giannis",imgray)
#cv2.imshow("lebron",imgray_1)
cv2.imshow("detección ",deteccion)
cv2.imshow("detección uno",deteccion_1)
cv2.waitKey(0)