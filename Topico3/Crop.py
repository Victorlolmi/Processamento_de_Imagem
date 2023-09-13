import cv2


def crop(image, x, y, width, height):

    cropped_image = image[y:y+height, x:x+width]

    return cropped_image

x_obj = int(input("Digite a posicao x:"))
y_obj = int(input("Digite a posicao y:"))

width_obj = int(input("Digite a largura:"))
height_obj = int(input("Digite a altura:"))

image = cv2.imread("D:\Desktop\Documents\GitHub\Processamento_de_Imagem\Topico3\imgs\garnet.jpg")

cropped_img = crop(image, x_obj, y_obj, width_obj, height_obj)

cv2.imshow("Cropped Image", cropped_img)

cv2.imwrite("Topico3\imgs\cropped_image.png", cropped_img)

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()