import numpy as np
import cv2

#recebe o endereco da imagem
obj_img = cv2.imread("D:\Desktop\Documents\GitHub\Processamento_de_Imagem\Topico2\TarefaPI1\imgs\garnet.jpg")


def insert_black_triangle(image,p1, p2, p3):
    
    # Coordenadas dos três pontos do triângulo
    #np.array neste caso armazena as coordenadas dos 3 pontos em um array 
    #np.int32 serve apenas para especificar o tipo de dado do elemento dentro do array
    pts = np.array([p1, p2, p3], np.int32)
    
   #PINTA O TRIANGULO
    result = cv2.fillPoly(image, [pts], 0)
    
    
    return result

# Coordenadas dos três pontos do triângulo
p1x = int(input("Digite a coordenada x do P1:"))
p1y = int(input("Digite a coordenada y do P1:"))
p2x = int(input("Digite a coordenada x do P2:"))
p2y = int(input("Digite a coordenada y do P2:"))
p3x = int(input("Digite a coordenada x do P3:"))
p3y = int(input("Digite a coordenada y do P3:"))
p1 = (p1x, p1y)
p2 = (p2x, p2y)
p3 = (p3x, p3y)

#recebe o endereco da imagem
image = cv2.imread("D:\Desktop\Documents\GitHub\Processamento_de_Imagem\Topico3\imgs\garnet.jpg")

# Insere o triângulo preto na imagem
image_with_triangle = insert_black_triangle(image.copy(), p1, p2, p3)

# Mostra a imagem
cv2.imshow("Image with Triangle", image_with_triangle)

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()