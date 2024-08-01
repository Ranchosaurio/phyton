import cv2
import numpy as np
import matplotlib.pylab as plt

##Funcion_cargar_i8magenes##
def carga_imagen():
    img = cv2.imread('tacos1.jpeg').astype(np.float32) / 255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img
###########################


##Funcion_ploteo###########
def despliega(img_3):
    ax1=fig.add_subplot(2,2,1)
    ax1.imshow(img)
    ax1.set_title("Canal h")


    #Canal verde
    ax2=fig.add_subplot(2,2,2)
    ax2.imshow(imagen_r2)
    ax2.set_title("Canal s")


    #Canal azul
    ax3=fig.add_subplot(2,2,3)
    ax3.imshow(imagen_r3)
    ax3.set_title("Canal v")


    #Reconstrucción de imagen
    ax4=fig.add_subplot(2,2,4)
    ax4.imshow(img )
    ax4.set_title("Original")

    #Reconstrucción de imagen
    ax4=fig.add_subplot(2,2,5)
    ax4.imshow(img )
    ax4.set_title("Original")

    #Reconstrucción de imagen
    ax4=fig.add_subplot(2,2,6)
    ax4.imshow(img )
    ax4.set_title("Original")

    #Reconstrucción de imagen
    ax4=fig.add_subplot(2,2,7)
    ax4.imshow(img )
    ax4.set_title("Original")
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img_3)
    plt.show()
###########################
# Distorsion
imagen=carga_imagen()
gamma=1/50
eleva_un_cuarto=np.power(imagen,gamma)
###despliega(eleva_un_cuarto)
# Distorsión Filtro por kernel
kernel = np.ones(shape = (10,10),dtype = np.float32 )/25
distorsion = cv2.filter2D(imagen, -1,kernel)
###despliega(distorsion)
# Distorsión por blur 
blur_distorsion=cv2.blur(imagen, ksize=(10,10))
###despliega(blur_distorsion) 
blur_gausiano=cv2.GaussianBlur(imagen,(5,5),50)
#despliega(blur_gausiano)
blur_median=cv2.medianBlur(imagen,5)#Se usa sobre todo en imagenes con pixeles extra o puntos 
#despliega(blur_median)
blur_bilateral=cv2.bilateralFilter(imagen,9,75,75)
despliega(blur_bilateral)
#cuadrados


cv2.waitKey(0)
