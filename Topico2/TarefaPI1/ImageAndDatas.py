import numpy as np
import cv2
#from matplotlib import pyplot as plt

#recebe o endereco da imagem
obj_img = cv2.imread("D:\Desktop\Documents\GitHub\Processamento_de_Imagem\Topico2\TarefaPI1\imgs\garnet.jpg")
#imprime a imagem na janela
cv2.imshow('Imagem', obj_img)

#shape retira as dimencoes da imagem e guarda e, vetores
dimensions = obj_img.shape
#vetor [0] possui a altura do objeto
height = dimensions[0]
#vetor [1] possui a largura do objeto
width = dimensions[1]
#vetor [3] possui o numero de canais
num_channels = dimensions[2]
#nbytes mostra o numero de bytes
size_bytes = obj_img.nbytes
#dtype mostra o tipo de dado
data_type = obj_img.dtype

print("Dimensões: {} x {}".format(width, height))
print("Número de Canais: {}".format(num_channels))
print("Tamanho em Bytes: {}".format(size_bytes))
print("Tipo de Dados dos Pixels: {}".format(data_type))

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()
