import cv2 as cv
import numpy as np
'''
    
    erosion = cv.erode(img,kernel,iterations = 1)
    dilation = cv.dilate(img,kernel,iterations = 1)
   
    
'''

def correcaoPorAbertura(img):
    '''Abertura =   erosao seguida por dilatacao'''
    kernel = np.ones((5,5),np.uint8)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    limite, imagem_limiarizada = cv.threshold(opening, 10, 255, cv.THRESH_BINARY)
    kernel = np.ones((10,10),np.uint8)
    opening = cv.morphologyEx(imagem_limiarizada, cv.MORPH_OPEN, kernel)
    kernel = np.ones((3,3),np.uint8)
    closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
    return closing
    
def correcaoPorFechamento(img):
    kernel = np.ones((4,4),np.uint8)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

    '''Fechamento = dilatacao seguida por erosao'''
    kernel = np.ones((20,20),np.uint8)
    closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
    return  closing

def main():
    entrada1 = cv.imread("Cervo.png",  cv.IMREAD_GRAYSCALE)
    entrada2 = cv.imread("pontos.png",  cv.IMREAD_GRAYSCALE)
    
    newImage1 = correcaoPorAbertura(entrada1)
    newImage2 = correcaoPorFechamento(entrada2)

    cv.imshow("Cervo Original", entrada1)
    cv.imshow("Cervo corrigido", newImage1)
    cv.imshow("Pontos Original", entrada2)
    cv.imshow("Pontos corrigido", newImage2)

    cv.waitKey(0)
    pass


if __name__ == "__main__":
    main()
