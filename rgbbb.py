import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen color
img = 255*np.ones((250,250,3), np.uint8)
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
for i in range(125):
    for m in range(250):
        R[i,:]=255
        G[i,m]=i
        B[i,:]=255
        img[i, m,:]= m

img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B


#verde
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
for i in range(125):
    for m in range(250):
        R[i,m]=i
        G[i,:]=255
        B[i,m]=i
        img[i, m,:]= m

#Se muestran los valores numericos
img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B


#azul
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
for i in range(125):
    for m in range(250):
        R[i,m]=i
        G[i,m]=i
        B[i,:]=255
        img[i, m,:]= m

img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B


#amarillo
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
for i in range(125):
    for m in range(250):
        R[i,:]=255
        G[i,:]=255
        B[i,m]=i
        img[i, m,:]= m

img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B

fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.set_title("Canal morado")


ax1=fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.set_title("Canal h")
#Canal verde
ax2=fig.add_subplot(2,2,2)
ax1.imshow(img)
ax2.set_title("Canal s")
#Canal azul
ax2=fig.add_subplot(2,2,3)
ax2.imshow(img)
ax2.set_title("Canal v")

ax4=fig.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("Original")