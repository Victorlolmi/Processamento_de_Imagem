import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def showImages(imgsArray, titlesArray, size, grid=(1,1)):

    y, x = grid
    fig, axes = plt.subplots(y, x, figsize = size)
    axes = axes.ravel() if isinstance(axes, np.ndarray) else np.array([axes])

    if len(imgsArray) != len(titlesArray):
        print("Error: the numbers of images and titles has to be the same!")
        return
    
    for idx, (img,title) in enumerate(zip(imgsArray, titlesArray)):
        if len(img.shape) == 2: # the image is gray tones
            axes[idx].imshow(img, cmap='gray')
        else : # the image is RGB
            axes[idx].imshow(img)
        axes[idx].set_title(title, fontdict={'fontsize':18, 'fontweight': 'medium'}, pad=10)
        if len(title) == 0:
            axes[idx].axis('off')

    plt.tight_layout() 
    plt.show()

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


img = cv.imread("Topico8\imgs\img_icons.png", cv.IMREAD_GRAYSCALE)

matrix= np.array([[1, 0], [0, 1]])
matrix2 = (1/32)*np.array([[16, 26, 16], [26, 41, 26], [16, 26, 16]])
matrix3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

dest_image = conv2d(img, matrix)
dest_image2 = conv2d(img, matrix2)
dest_image3 = conv2d(img, matrix3)
showImages([img, dest_image, dest_image2, dest_image3],['Original','Filtrada 1', 'Filtrada 2','Filtrada 3'], size=(10,10), grid=(2,2))


cv.waitKey(0)

