import cv2
import numpy as np

img = cv2.imread("Topico3\imgs\green_image.png")

#Extrai canais de cores
red_channel = img[:, :, 2]
green_channel = img[:, :, 1]
blue_channel = img[:, :, 0]


cv2.imshow("Canal vermelho", red_channel)
cv2.imshow("Canal Azul", blue_channel)
cv2.imshow("Canal Verde", green_channel)

#calcula a media das cores
red_mean = np.mean(red_channel)
blue_mean = np.mean(blue_channel)
green_mean = np.mean(green_channel)


#cor predominante

predominant_color = ""

if red_mean > green_mean and red_mean > blue_mean:
    predominant_color = "Vermelho"
elif blue_mean > red_mean and blue_mean > green_mean:
    predominant_color = "Azul"
elif green_mean > red_mean and green_mean > blue_mean:
    predominant_color = "Verde"
else:
    predominant_color = "inexistente"

print(f"A cor predominante da imagem é {predominant_color}")


#espera uma tecla ser precionada
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()
