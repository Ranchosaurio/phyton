import cv2
import numpy as np
import matplotlib.pylab as plt
img_bgr=cv2.imread("drone.jpg")


img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
hist_values=cv2.calcHist([img_bgr], channels=[1], mask=None,histSize=[256],ranges=[0,256]) #Calcula el histograma par la matriz verde
print(hist_values.shape)
tamaño=(512,512)

img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
hist_values1=cv2.calcHist([img_bgr], channels=[0], mask=None,histSize=[256],ranges=[0,256]) #Calcula el histograma par la matriz rojo
print(hist_values1.shape)
tamaño=(512,512)

img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
hist_values2=cv2.calcHist([img_bgr], channels=[2], mask=None,histSize=[256],ranges=[0,256]) #Calcula el histograma par la matriz blue
print(hist_values2.shape)
tamaño=(512,512)

img_resize=cv2.resize(img_bgr,tamaño,interpolation=cv2.INTER_CUBIC)
hist_values_resize=cv2.calcHist([img_resize], channels=[1], mask=None,histSize=[256],ranges=[0,256])
#plt.plot(hist_values)

img_resize1=cv2.resize(img_bgr,tamaño,interpolation=cv2.INTER_CUBIC)
hist_values_resize1=cv2.calcHist([img_resize1], channels=[0], mask=None,histSize=[256],ranges=[0,256])
#plt.plot(hist_values)

img_resize2=cv2.resize(img_bgr,tamaño,interpolation=cv2.INTER_CUBIC)
hist_values_resize2=cv2.calcHist([img_resize2], channels=[2], mask=None,histSize=[256],ranges=[0,256])
#plt.plot(hist_values)

print(img_bgr.shape)
min=0
max=0
for x in hist_values:
    for z in x:
        if z > max:
             max = z
        if z < min:
            min = z
print(max)
print(min)
   
fig_1 = plt.figure()
# imagen original
ax1 = fig_1.add_subplot(2,2,1)
ax1.imshow(img_rgb)
ax1.set_title("IMAGEN")

# recorte
ax2 = fig_1.add_subplot(2,2,2)
ax2.plot(hist_values_resize)
ax2.set_title("Histograma verde")

ax3 = fig_1.add_subplot(2,2,3)
ax3.plot(hist_values_resize1)
ax3.set_title("Histograma rojo")

ax4 = fig_1.add_subplot(2,2,4)
ax4.plot(hist_values_resize2)
ax4.set_title("Histograma azul")

plt.show()