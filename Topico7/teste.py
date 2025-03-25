import cv2
import numpy as np

# Carregue a imagem térmica
imagem = cv2.imread('Topico6\imgs\FLIR0196.jpg')


# Converta a imagem para o espaço de cores HSV
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Defina os limites superior e inferior para a cor vermelha
vermelho_superior = np.array([255, 255, 255])
vermelho_inferior = np.array([0, 0, 200])


# Crie uma máscara para a cor vermelha
mascara_vermelha = cv2.inRange(hsv, vermelho_inferior, vermelho_superior)


# Combine as máscaras para obter a máscara final
mascara = mascara_vermelha

# Aplique a máscara à imagem original
imagem_recortada = cv2.bitwise_and(imagem, imagem, mask=mascara)



imagem_recortada = cv2.cvtColor(imagem_recortada, cv2.COLOR_BGR2GRAY)

_ , thresholded_mask = cv2.threshold(imagem_recortada, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU )

result = cv2.bitwise_not(imagem_recortada, imagem_recortada, mask = thresholded_mask)


# Mostre a imagem recortada
cv2.imshow('Imagem Recortada', imagem_recortada)
cv2.waitKey(0)