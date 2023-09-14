import numpy as np 
import cv2

ESCAPE_KEY_ASCII = 27
img = cv2.imread("Topico5\imgs\lonilse.jpg")

windowTitle = "Ajuste de Brilho e Contraste"
cv2.namedWindow(windowTitle)

while True:
    cv2.imshow(windowTitle, img)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ESCAPE_KEY_ASCII:
        break


#fecha as janelas abertas
cv2.destroyAllWindows()