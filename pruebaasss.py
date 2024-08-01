import cv2
import numpy as np

cap = cv2.VideoCapture(1)

winName = 'IP_CAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

while True:
    ret, frame = cap.read()
    img_dist = cv2.medianBlur(frame, 9)
    bordes_1 = cv2.Canny(img_dist, threshold1=100, threshold2=200)  # Ajusta estos valores según sea necesario

    countours_b, jerarqui_b = cv2.findContours(bordes_1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    if len(countours_b) > 0:
        contours_data = np.vstack(countours_b).reshape(-1, 2)
        np.savetxt('contours_data.txt', contours_data, fmt='%d', delimiter=', ')

        # Calcular el centroide de los contornos en el eje X
        centroid_x = int(np.mean(contours_data[:, 0]))

        # Calcular el centro de la imagen
        centro_imagen_x = frame.shape[1] // 2

        # Definir un rango de tolerancia alrededor del centro
        rango_tolerancia = 150  # Ajusta este valor según sea necesario

        # Comparar con el centro de la imagen y el rango de tolerancia
        if centro_imagen_x - rango_tolerancia < centroid_x < centro_imagen_x + rango_tolerancia:
            print("Los contornos están en el centro.")
        elif centroid_x < centro_imagen_x - rango_tolerancia:
            print("Los contornos están a la izquierda.")
        elif centroid_x > centro_imagen_x + rango_tolerancia:
            print("Los contornos están a la derecha.")

        cv2.drawContours(frame, countours_b, -1, (0, 255, 0), 3)

    cv2.imshow("Imagen", frame)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows()
cap.release()
