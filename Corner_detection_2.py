#Shi-Tomasi Algorithm
import cv2
import numpy as np
import matplotlib.pylab as plt
def despliega(img_3):
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img_3)
    plt.show()
def carga_imagen(x):
    tab_BGR = cv2.imread(x)
    tab_gray = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2GRAY)
    tab_RGB = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2RGB)
    return tab_gray,tab_RGB,tab_BGR

imgray,imbgr,imgrgb=carga_imagen("tablero_base.jpg")

esquinas=cv2.goodFeaturesToTrack(imgray,100,0.09,10) #primera el numero de esquinas, segundo se necesita que sea menor a 1, tercer parametro
#tercer parametro presicion y ell cuarto convierte parametros de hasta 64 bits  
#Imagen, numero de puntos, detección fina < 1, precisión
#esquinas=cv2.goodFeaturesToTrack(imgray,500,0.09,10)
esquinas=np.int64(esquinas)
for i in esquinas:
    x,y=i.ravel()
    cv2.circle(imgrgb,(x,y),10,(255,0,255),1) #corrimiento de x y y 
despliega(imgrgb)

cv2.waitKey(0)