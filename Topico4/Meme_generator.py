
import numpy as np
import cv2
from matplotlib import pyplot as plt

def resizeImage(image, scalePercent):
    width = int(image.shape[1] * scalePercent / 100)
    height = int(image.shape[0] * scalePercent / 100)
    image = cv2.resize(image, (width, height))

    return image

def addImageOverlay(background, foreground, translationForegroundW, translationForegroundH):
    backH, backW, _ = background.shape
    foreH, foreW, _ = foreground.shape
    remainingH, remainingW = backH - foreH, backW - foreW

    if translationForegroundH + foreH > backH:
        print("Erro: sobreposição com altura maior do que a permitida.")
        print("Posição final que altura do objeto da frente termina:", translationForegroundH + foreH)
        print("Altura do fundo:", backH)
        return

    if translationForegroundW + foreW > backW:
        print("Erro: sobreposição com largura maior do que a permitida.")
        print("Posição final que largura do objeto da frente termina:", translationForegroundW + foreW)
        print("Largura do fundo:", backW)
        return

    #parte do cenário do fundo em que a imagem será adicionada
    crop = background[translationForegroundH : foreH + translationForegroundH, translationForegroundW : foreW + translationForegroundW]

    #Transformamos o foreground em imagem com tons de cinza e criamos uma máscara binária da mesma com a binarização (cv2.threshold)
    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    ret, maskFore = cv2.threshold(foregroundGray, 240, 255, cv2.THRESH_BINARY)

    #Agora aplicamos uma operação de AND binário na imagem recortada 'crop'. No caso, realizar a operação binária entre a mesma imagem não terá efeito. Só que, com a inclusão da máscara no terceiro parâmetro, os pixels pretos de maskFore serão ignorados e, portanto, ficarão escuros. Com isso temos a marcação em que vamos incluir o foreground posteriormente.
    backWithMask = cv2.bitwise_and(crop, crop, mask = maskFore)
    foreWithMask = cv2.bitwise_not(maskFore)
    foreWithMask = cv2.bitwise_and(foreground, foreground, mask = foreWithMask)

    #Faremos a composição entre 'frente' e 'fundo', compondo o foreground na imagem extraída do background.
    combinedImage = cv2.add(foreWithMask, backWithMask)

    #Adicionamos a imagem gerada no background final.
    copyImage = background.copy()
    copyImage[translationForegroundH:foreH + translationForegroundH, translationForegroundW:foreW + translationForegroundW] = combinedImage

    return copyImage

def addBlendingEffect(firstImage, secondImage, weight):
    firstImageGray = cv2.cvtColor(firstImage, cv2.COLOR_BGR2GRAY)
    secondImageGray = cv2.cvtColor(secondImage, cv2.COLOR_BGR2GRAY)

    mask = firstImageGray - secondImageGray
    ret, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)

    copyImg = firstImage.copy()
    altura, largura, = mask.shape
    for y in range(0, altura):
        for x in range(0, largura):
            if mask.item(y, x) == 255:
                blendingPixelBlue = firstImage.item(y, x, 0) * (1.0 - weight) + secondImage.item(y, x, 0) * weight
                blendingPixelGreen = firstImage.item(y, x, 1) * (1.0 - weight) + secondImage.item(y, x, 1) * weight
                blendingPixelRed = firstImage.item(y, x, 2) * (1.0 - weight) + secondImage.item(y, x, 2) * weight

                copyImg.itemset((y, x, 0), blendingPixelBlue)
                copyImg.itemset((y, x, 1), blendingPixelGreen)
                copyImg.itemset((y, x, 2), blendingPixelRed)

    return copyImg

def memeGeneratorWithBlending(fala1, imagem1, fala2, imagem2, fundo):
    atilaFeliz = cv2.imread(imagem1)
    background = cv2.imread(fundo)
    atilaFeliz = resizeImage(atilaFeliz, 250)
    finalImageUmAtila = addImageOverlay(background, atilaFeliz, 380, 465)

    atilaBravo = cv2.imread(imagem2)
    atilaBravo = resizeImage(atilaBravo, 250)
    finalImageDoisAtilas = addImageOverlay(finalImageUmAtila, atilaBravo, 930, 460)


    finalImage = addBlendingEffect(finalImageUmAtila, finalImageDoisAtilas, 0.4)

    finalImage = cv2.putText(finalImage, fala1, (210, 420), cv2.FONT_HERSHEY_SIMPLEX ,
                   2.5, (0, 0, 0), 5, cv2.LINE_AA)

    finalImage = cv2.putText(finalImage, fala2, (1030, 1150), cv2.FONT_HERSHEY_SIMPLEX ,
                   2.5, (0, 0, 0) , 5, cv2.LINE_AA)

    cv2.imwrite("Topico4\imgs\memeatila.png", finalImage)

memeGeneratorWithBlending('Respeito seu argumento!', "Topico4\imgs\img_atila_feliz.png", 'Burro pra caramba...', "Topico4\imgs\img_atila_bravo.png", "Topico4\imgs\img_fundo2.jpg")
atila_bravo = cv2.imread("Topico4\imgs\memeatila.png")

cv2.imshow("Meme",atila_bravo)

#espera uma tecla ser precionada 
cv2.waitKey(0)
#fecha as janelas abertas
cv2.destroyAllWindows()
