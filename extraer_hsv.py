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
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
#Corrección de color de BGR a HSV
imgHSV=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

#Extraemos los atributos principales de la imagen en escala de grises
H = img[: , : , 0]
S = img[: , : , 1]
V = img[: , : , 2]
#Los 3 comandos anteriores son identicos a el siguiente comando
H,S,V = cv2.split(dronecolor)
print(imgHSV)

#Ploteamos los canales
fig=plt.figure()
#Canal rojo
ax1=fig.add_subplot(2,2,1)
ax1.imshow(H, cmap="gray")
ax1.set_title("Canal h")
#Canal verde
ax2=fig.add_subplot(2,2,2)
ax2.imshow(S, cmap="gray")
ax2.set_title("Canal s")
#Canal azul
ax2=fig.add_subplot(2,2,3)
ax2.imshow(V, cmap="gray")
ax2.set_title("Canal v")
#Reconstrucción de imagen
imgre=cv2.merge((H,S,V))
#Imagen original

ax4=fig.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("Original")

plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)