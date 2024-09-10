import cv2
import time

time_between_frames = 1
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
frame_counter = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo leer el frame.")
        break

    filename = f'frames/frame_{frame_counter}.jpg'
    cv2.imwrite(filename, frame)

    print("Frame capturado:", filename)
    frame_counter += 1
    time.sleep(time_between_frames)

cap.release()
cv2.destroyAllWindows()
