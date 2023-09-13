import cv2

def paste(src, dst, x, y):

#shape obtem as dimensoes da imagem 0 = altura, 1 = largura, 2 = numero de canais(rgb)
    dst_shapes = dst.shape

    dst_height = dst_shapes[0] 
    dst_width  = dst_shapes[1]

    #Verificar se a imagem colada possui dimenoes para ser colada na imagem 
    

    #faz uma copia para a original nao ser modificada

    result = src.copy()
    
    result[y:y + dst_height, x:x + dst_width] = dst

    return result


x_obj = int(input("Digite a posicao x:"))
y_obj = int(input("Digite a posicao y:"))

src = cv2.imread("D:\Desktop\Documents\GitHub\Processamento_de_Imagem\Topico3\imgs\Mountain 4k.jpg")
dst = cv2.imread("D:\Desktop\Documents\GitHub\Processamento_de_Imagem\Topico3\imgs\cropped_image.png")

pasted_image = paste(src, dst, x_obj, y_obj)

cv2.imshow("Imagem Colada", pasted_image)

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()





