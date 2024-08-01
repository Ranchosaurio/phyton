import cv2
import numpy as np

cap = cv2.VideoCapture(0)

winName = 'IP_CAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Reducir el tamaño del video de entrada (opcional)
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    img_dist = cv2.medianBlur(frame, 9)
    bordes_1 = cv2.Canny(img_dist, threshold1=200, threshold2=120)

    countours_b, _ = cv2.findContours(
        bordes_1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, countours_b, -1, (0, 255, 0), 3)

    if countours_b:
        contours_data = np.vstack(countours_b).reshape(-1, 2)
        np.savetxt('contours_data.txt', contours_data, fmt='%d', delimiter=', ')

        centroid_x = int(np.mean(contours_data[:, 0]))
        centro_imagen_x = frame.shape[1] // 2
        rango_tolerancia = 45  

        if centro_imagen_x - rango_tolerancia < centroid_x < centro_imagen_x + rango_tolerancia:
            print("Los contornos están en el centro.")
        elif centroid_x < centro_imagen_x - rango_tolerancia:
            print("Los contornos están a la izquierda.")
        elif centroid_x > centro_imagen_x + rango_tolerancia:
            print("Los contornos están a la derecha.")

    cv2.imshow("Imagen", frame)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows()
