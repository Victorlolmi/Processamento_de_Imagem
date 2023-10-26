import cv2
import numpy as np

#carrea a img
original_img = cv2.imread("Topico5\campo_de_flores.jpg")

lowerColor = np.array([0, 0, 0])
upperColor = np.array([120, 255, 255])

#definir a mascara com os valores min e max dados
mask = cv2.inRange(original_img, lowerColor, upperColor)

#Compara a mascara com a imagem 
result = cv2.bitwise_and(original_img, original_img, mask = mask)

#aplica a limiarizacao 
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
_,gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY )



#mostra a img limiarizada
cv2.imshow("Imagem limiarizada",gray )
#mostra a img saida
cv2.imshow("Imagem saida", result)

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()