import cv2
import numpy as np

# Función para detectar autos en la imagen
def detect_cars(img):
    car_cascade = cv2.CascadeClassifier('carros/cars.xml')
    car_img = img.copy()
    car_rectangles = car_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=5)
    car_count = 0

    for (x, y, w, h) in car_rectangles:
        cv2.rectangle(car_img, (x, y), (x + w, y + h), (0, 256, 0), 2)
        car_count += 1
    
    return car_img, car_count

# Captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Asumiendo un número fijo de espacios en el parquímetro
total_spaces = 10

while True:
    ret, frame = cap.read()  
    if not ret:
        break

    # Detección de autos y conteo
    detection, car_count = detect_cars(frame)

    # Cálculo de espacios disponibles
    available_spaces = total_spaces - car_count

    # Mostrar el conteo de autos y espacios disponibles en la imagen
    cv2.putText(detection, f'Autos: {car_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(detection, f'Espacios Disponibles: {available_spaces}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Mostrar la imagen con las detecciones y el conteo
    cv2.imshow('Detección en Tiempo Real', detection)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:  # Presiona 'Esc' para salir
        break

# Liberar la captura y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
