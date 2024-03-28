import cv2 as cv
import numpy as np
'''
    erosion = cv.erode(img,kernel,iterations = 1)
    dilation = cv.dilate(img,kernel,iterations = 1)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
'''

def detctorDeBordas(img):
    #elemento estruturante, formado por uma matriz 5x5 de 1's (inteiros, sem sinal, 8bits)
    kernel = np.ones((5,5),np.uint8)
    ''' gradiente morfologico = diferença entre dilatação e erosão da imagem'''
    gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    
    return gradient

def main():
    entrada = cv.imread("image.png",  cv.IMREAD_GRAYSCALE)

    newImg = detctorDeBordas(entrada)
    cv.imshow("Imagem original", entrada)
    cv.imshow("Bordas", newImg)
    cv.waitKey(0)
    pass


if __name__ == "__main__":
    main()
