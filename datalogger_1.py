#importamos librerias
import cv2
import matplotlib.pylab as plt
import numpy as np
#Importamos la imagen del drone en color
dronecolor=cv2.imread("ojos.jpg") 
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
B,G,R=cv2.split(img)
b_1 = np.savetxt('B.txt', B, delimiter =', ')    
G_1 = np.savetxt('G.txt', G, delimiter =', ')
R_1 = np.savetxt('R.txt', R, delimiter =', ')        
R = img[: , : , 0]
G = img[: , : , 1]
B = img[: , : , 2]
G[:,:]=180
img[:,:,0]=G

B[:,:]=35
img[:,:,0]=B

B[:,:]=180
img[:,:,0]=B
RGB=cv2.merge((R,G,B))
cv2.waitKey(0)

