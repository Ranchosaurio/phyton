#importamos librerias
import cv2
import matplotlib.pylab as plt
#Importamos la imagen del drone en escala de grises
dronegray=cv2.imread("descarga.jpg", 0)#Un solo canal o una sola matriz
#Importamos la imagen del drone en color
dronergb=cv2.imread("descarga.jpg", 1) #Tres canales o tres matrices
#Importamos la imagen del drone en color
dronecolor=cv2.imread("descarga.jpg") #Tres canales o tres matrices
#Corrección de color de BGR a rgb
#Corrección de color de BGR a rgb
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
#Corrección de color de RGB a HSV
imgHSV=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

#Extraemos los atributos principales de la imagen en escala de grises
H = imgHSV[: , : , 0]
S = imgHSV[: , : , 1]
V = imgHSV[: , : , 2]
#Los 3 comandos anteriores son identicos a el siguiente comando

H[:,:]=15

imgHSV[:,:,0]=H

HSV=cv2.merge((H,S,V))

#Extraemos los atributos principales de la imagen en escala de grises
R = img[: , : , 0]
G = img[: , : , 1]
B = img[: , : , 2]
#Los 3 comandos anteriores son identicos a el siguiente comando

B[:,:]=80

img[:,:,0]=B

RGB=cv2.merge((R,G,B))
#Extraemos los atributos principales de la imagen en escala de grises
B_1 = dronecolor[: , : , 0]
G_1 = dronecolor[: , : , 1]
R_1 = dronecolor[: , : , 2]
#Los 3 comandos anteriores son identicos a el siguiente comando

B_1[:,:]=150

dronecolor[:,:,0]=B_1

BGR=cv2.merge((B_1,G_1,R_1))

#Ploteamos los canales
fig=plt.figure()
#Canal rojo
ax1=fig.add_subplot(2,2,1)
ax1.imshow(RGB)
ax1.set_title("Canal B MODIFICADO")
#Canal verde
ax2=fig.add_subplot(2,2,2)
ax2.imshow(HSV)
ax2.set_title("Canal H MODIFICADO")
#Canal azul
ax2=fig.add_subplot(2,2,3)
ax2.imshow(BGR)
ax2.set_title("Canal BGR MODIFICADO")
#Reconstrucción de imagen
imgre=cv2.merge((RGB,HSV,BGR))
#Imagen original

imgr=cv2.cvtColor(dronergb,cv2.COLOR_RGB2BGR)
ax4=fig.add_subplot(2,2,4)
ax4.imshow(imgr)
ax4.set_title("Original")


plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)