import cv2
import numpy as np

#carrgando as imagens

neon = cv2.imread("Topico4\imgs\_neon.png")
lilce = cv2.imread("Topico4\imgs\lilce.png")

#garantir que as fotos possuam as mesmas dimensoes

height_neon, widht_neon, _ = neon.shape
lilce = cv2.resize(lilce,(widht_neon, height_neon))

#mescla imagens (soma ponderada de duas matrizes, pega os pixels e soma)

nelce = cv2.addWeighted(neon, 0.5, lilce, 0.5, 0)

#reduzir o tamanho da imagem do nelce

neon = cv2.resize(neon, (int(widht_neon * 0.25),int(height_neon * 0.25) ))

# recortar a face

#crop_nelce = nelce[10:100, 20:120]

cv2.imshow("Nelce", nelce)

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()