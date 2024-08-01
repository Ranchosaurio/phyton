#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen color
img = 255*np.ones((250,125,3), np.uint8)
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
for i in range(250):
    for m in range(255):
        R[i,:]=255
        G[i,m]=i
        B[i,:]=255
        img[i, m,:]= m
img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B
plt.imshow(img, cmap='gray')
plt.show()

#verde
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
for i in range(250):
    for m in range(250):
        R[i,m]=i
        G[i,:]=255
        B[i,m]=i
        img[i, m,:]= m

#Se muestran los valores numericos
img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B
plt.imshow(img, cmap='gray')
plt.show()

#rojo
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
for i in range(250):
    for m in range(250):
        R[i,:]=255
        G[i,m]=i
        B[i,m]=i
        img[i, m,:]= m

img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B
plt.imshow(img, cmap='gray')
plt.show()