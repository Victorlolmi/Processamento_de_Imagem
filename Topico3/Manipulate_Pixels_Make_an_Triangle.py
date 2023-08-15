import numpy as np
import cv2

#recebe o endereco da imagem
obj_img = cv2.imread("D:\Desktop\Documents\GitHub\Processamento_de_Imagem\Topico2\TarefaPI1\imgs\garnet.jpg")
#imprime a imagem na janela
cv2.imshow('Imagem', obj_img)



#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()