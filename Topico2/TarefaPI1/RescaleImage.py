import numpy as np
import cv2
#from matplotlib import pyplot as plt


def rescaleImage(image, scale_percent):
    # Obtem as dimensões da imagem original com base nos vetores [1] e [0] respectivamentes largura e altura 
    #obtendo essas dimensões dividimos por 100 para obter a porcentagem (regra de 3)
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    # Defini as novas dimensões
    new_dimensions = (width, height)

    # Redimensiona a imagem usando o metodo de intepolação cv2.INTER_AREA
    resized_image = cv2.resize(
        image, new_dimensions, interpolation=cv2.INTER_AREA)

    return resized_image


obj_img = cv2.imread("D:\Desktop\Documents\GitHub\Processamento_de_Imagem\Topico2\TarefaPI1\imgs\Mountain 4K.jpg")
# cv2.imshow(obj_img)
scale_percent = int(input("Digite a scala"))

resized_image = rescaleImage(obj_img, scale_percent)

cv2.imshow('Imagem', obj_img)


# shape retira as dimencoes da imagem e guarda e, vetores
dimensions = obj_img.shape
# vetor [0] possui a altura do objeto
height = dimensions[0]
# vetor [1] possui a largura do objeto
width = dimensions[1]
# vetor [3] possui o numero de canais
num_channels = dimensions[2]
# nbytes mostra o numero de bytes
size_bytes = obj_img.nbytes
# dtype mostra o tipo de dado
data_type = obj_img.dtype
print("Original:")
print("Dimensões: {} x {}".format(width, height))
print("Número de Canais: {}".format(num_channels))
print("Tamanho em Bytes: {}".format(size_bytes))
print("Tipo de Dados dos Pixels: {}".format(data_type))

cv2.imshow('Imagem Redimensionada', resized_image)
# shape retira as dimencoes da imagem e guarda e, vetores
dimensions = resized_image.shape
# vetor [0] possui a altura do objeto
height = dimensions[0]
# vetor [1] possui a largura do objeto
width = dimensions[1]
# vetor [3] possui o numero de canais
num_channels = dimensions[2]
# nbytes mostra o numero de bytes
size_bytes = resized_image.nbytes
# dtype mostra o tipo de dado
data_type = resized_image.dtype
print("Redimensionada:")
print("Dimensões: {} x {}".format(width, height))
print("Número de Canais: {}".format(num_channels))
print("Tamanho em Bytes: {}".format(size_bytes))
print("Tipo de Dados dos Pixels: {}".format(data_type))

# espera uma tecla ser precionada
cv2.waitKey(0)
# fecha as janelas abertas
cv2.destroyAllWindows()
