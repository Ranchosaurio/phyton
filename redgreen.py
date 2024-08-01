import cv2
import numpy as np
import matplotlib.pylab as plt

# Crear una imagen color
img = 255 * np.ones((250, 250, 3), np.uint8)

# Extraer los canales
R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

# Modificar los canales para crear el degradado
for y in range(250):
    R[y, :] = 128 + int((y / 250) * (255 - 128))
    G[y, :] = 0
    B[y, :] = 128 + int((y / 250) * (255 - 128))

# Mostrar los valores numéricos
img[:, :, 0] = R
img[:, :, 1] = G
img[:, :, 2] = B
print(img)

# Mostrar la imagen
plt.imshow(img)
plt.show()

# Esperar a que se presione una tecla
cv2.waitKey(0)
