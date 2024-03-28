import cv2 as cv
import numpy as np

def conv2d(source_image, matrix):
    height, width = source_image.shape
    matrix_height, matrix_width = matrix.shape
    dest_image = np.zeros((height, width), dtype=np.uint8)
    offset_h = matrix_height // 2
    offset_w = matrix_width // 2
    
    
    if(matrix_height == 2 and matrix_width == 2):
        n =0
    if(matrix_height == 3 and matrix_width == 3):
         n=1

    
    for y in range(offset_h, height - offset_h):
        for x in range(offset_w, width - offset_w):
            # Extrai a região da imagem que corresponde à matriz de convolução
            region = source_image[y - offset_h:y + offset_h +n, x - offset_w:x + offset_w+n]

            # Realiza a convolução multiplicando os elementos da região pela matriz de convolução
            result = (region * matrix).sum()

            # Atribui o resultado à posição correspondente na imagem de destino
            dest_image[y, x] = np.clip(result, 0, 255).astype(np.uint8)


    return dest_image

def main():
    img = cv.imread("imagem.png", cv.IMREAD_GRAYSCALE)
    matrix= np.array([[1, 0], [0, 1]])
    #matrix = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    matrix2 = (1/9)*np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    #matrix = (1/16)*np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    #matrix = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    #matrix2 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    #matrix = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    dest_image = conv2d(img, matrix)
    dest_image2 = conv2d(img, matrix2)
    cv.imshow("imagem original", img)
    cv.imshow("imagem filtrada", dest_image)
    cv.imshow("imagem filtrada 2", dest_image2)
    cv.waitKey(0)

if __name__ == "__main__":
    main()
