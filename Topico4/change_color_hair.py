import cv2
import numpy as np

#carrega imagens

original_img = cv2.imread("Topico4\imgs\cabelo_ruivo.png")
mask_img = cv2.imread("Topico4\imgs\mask.png")

final_img = cv2.addWeighted(original_img, 0.5, mask_img, 0.5, 0)

cv2.imshow("Imagem original", original_img)
cv2.imshow("Mask", mask_img)

cv2.imshow("Imagem com mascara", final_img)

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()