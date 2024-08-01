import cv2
import numpy as npq
import matplotlib.pylab as plt

def detect_face(img):
    face_cascade = cv2.CascadeClassifier('carros/cars2.xml')
    face_img = img.copy()
    face_rectangle = face_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in face_rectangle:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (0, 256, 0), 2)
    return face_img


cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()  
    if not ret:
        break

    detection = detect_face(frame)

    cv2.imshow('Detección en Tiempo Real', detection)

    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()