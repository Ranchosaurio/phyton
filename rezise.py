#importamos librerias
import cv2
import matplotlib.pylab as plt
#Importamos la imagen del drone en color
dronecolor=cv2.imread("descarga.jpg") #Tres canales o tres matrices
#Corrección de color de BGR a rgb
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)

#Ploteamos los canales
print(img.shape)
#Resize por dimensión
imagen_r1=cv2.resize(img,(100,200))
#Resize por radio
ancho=2
alto=2
imagen_r2=cv2.resize(img,(0,0),img,ancho,alto)
imagen_r3=cv2.flip(img,0)
print(imagen_r2.shape)
fig=plt.figure()


H = imagen_r1[: , : , 0]
S = imagen_r1[: , : , 1]
V = imagen_r1[: , : , 2]
H[:,:]=130
imagen_r1[:,:,0]=H
HSV=cv2.merge((H,S,V))
################################################################
R = imagen_r2[: , : , 0]
G = imagen_r2[: , : , 1]
B = imagen_r2[: , : , 2]
G[:,:]=180
imagen_r2[:,:,0]=G
RGB=cv2.merge((R,G,B))
################################################################
B_1 = imagen_r3[: , : , 0]
G_1 = imagen_r3[: , : , 1]
R_1 = imagen_r3[: , : , 2]
B_1[:,:]=210
imagen_r3[:,:,0]=B_1
BGR=cv2.merge((B_1,G_1,R_1))

#Canal rojo
ax1=fig.add_subplot(2,2,1)
ax1.imshow(imagen_r1)
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


plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)

