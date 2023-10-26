import cv2
import numpy as np

#from matplotlib import pyplot as plt

#receb duas imagens e uma se retira as medidas da forma com o .shape e a outra e resized com essas dimenções com .resize
def resizeEqual(imageSizeFrom, imageSizeTo):

    #Retiramos altura e largura, nao utilizamos o canal
    height, width , _ = imageSizeFrom.shape

    return cv2.resize(imageSizeTo, (int(width), int(height)))


def addImageInBackground(foreground, background):

    #Retiramos da imagem de primeiro plano as dimencoes
    foreH, foreW, _ = foreground.shape

    #Converte para cinza
    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)

    #Cria uma macara que destacas as areas nao tranparentes(255) e transparentes (0) , o resultado e salvo em maskFore o resto é ignorado
    rest, maskFore = cv2.threshold(foregroundGray, 75, 255, cv2.THRESH_BINARY)
    
    #.bitwise_and aqui funciona como um recort pega apenas as partes onde a mascara e branca (nao transparente)
    #recorta o fundo no formado da imagem de primeiro plano
    backWithMask = cv2.bitwise_and(background, background, mask = maskFore)
    #.bitwise_not inverte os valores da mascara onde era 0 vira 255 e onde era 255 vira 0
    foreWithMask = cv2.bitwise_not(maskFore)
    #Pega as partes nao transparente do primeiro plano
    foreWithMask = cv2.bitwise_and(foreground, foreground, mask = foreWithMask)

    #mistura as duas imagens
    result = cv2.add(foreWithMask, backWithMask)

    return result

def main():

    Background_img = cv2.imread('Topico4\imgs\Mountain 4K.jpg')
    
    Foreground_img = cv2.imread('Topico4\imgs\A.png')
  
    Foreground_img = resizeEqual(Background_img, Foreground_img)

    
    cv2.imshow("Blended image", addImageInBackground(Foreground_img, Background_img))

    #espera uma tecla ser precionada
    cv2.waitKey(0)
    #fecha as janelas abertas
    cv2.destroyAllWindows()
 

main()