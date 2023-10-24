import cv2
import numpy as np

#from matplotlib import pyplot as plt

def display(image):
    cv2.imshow("Blended image",image)

    #espera uma tecla ser precionada 
    cv2.waitKey(0)
    #fecha as janelas abertas
    cv2.destroyAllWindows()


def resizeImage(image, scale):
    h, w , c = image.shape
    height = int(h * scale/100)
    width = int(w * scale/100)
    return cv2.resize(image, dsize=(width, height))

def resizeEqual(imageSizeFrom, imageSizeTo):

    print(imageSizeFrom.shape)
    h, w , c = imageSizeFrom.shape
    height = int(h)
    width = int(w)
    return cv2.resize(imageSizeTo, (width, height))

def blend(imgA, imgB):
    resImage = cv2.addWeighted(imgA, 0.8, imgB, 0.2, 0)
    return resImage

'''def addOverlay(background, foreground):
    foreH, foreW, _ = foreground.shape

    backgroundWithNoImage = background[0 : foreH, 0 : foreW]

    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    ret, maskFore = cv2.threshold(foregroundGray, 245, 255, cv2.THRESH_BINARY)


    backWithMask = cv2.bitwise_and(backgroundWithNoImage, backgroundWithNoImage, mask = maskFore)
    foreWithMask = cv2.bitwise_not(maskFore)
    foreWithMask = cv2.bitwise_and(foreground, foreground, mask = foreWithMask)

    result = cv2.add(backWithMask, foreWithMask)
    copyImage = background.copy()

    copyImage[0 : foreH + 30, 0 : foreW + 100]

    return copyImage'''

def addImageNoBackground(foreground, background):
    foreH, foreW, _ = foreground.shape
    #backH, backW, _ = background.shape

    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    ret, maskFore = cv2.threshold(foregroundGray, 75, 255, cv2.THRESH_BINARY)

    #display(foregroundGray)

    backgroundWithNoImage = background[0 : foreH, 0 : foreW]

    backWithMask = cv2.bitwise_and(backgroundWithNoImage, backgroundWithNoImage, mask = maskFore)
    foreWithMask = cv2.bitwise_not(maskFore)
    foreWithMask = cv2.bitwise_and(foreground, foreground, mask = foreWithMask)

    result = cv2.add(foreWithMask, backWithMask)

    return result



def addImage(imgA, imgB):
    return cv2.add(imgA, imgB)

def main():
    imgA = cv2.imread('Head/03_Blend/img/0.jpeg')
    imgB = cv2.imread('Head/03_Blend/img/0_2.jpeg')
    imgC = cv2.imread('Head/03_Blend/img/D.png')
    imgB = resizeEqual(imgA, imgB)
    imgC = resizeEqual(imgA, imgC)

    newImg = cv2.cvtColor(blend(imgA, imgB), cv2.COLOR_BGR2RGB)

    display(newImg)

    display(addImageNoBackground(imgC, newImg))

    '''newImg = cv2.cvtColor(addOverlay(imgB, imgA), cv2.COLOR_BGR2RGB)
    display(newImg)'''

main()