import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def filtragem(img, name):
    lower_threshold = 50
    upper_threshold = 150
    kernel_size = (5, 5)
    sigma = 0
    filtered_image = None
    
    if name == "media":
        filtered_image=(cv.blur(img, kernel_size))
    if name == "gaussiano":
        filtered_image=(cv.GaussianBlur(img, kernel_size, sigma))
    if name == "mediana":
        kernel_size = 5  
        filtered_image=(cv.medianBlur(img, kernel_size))
    if name == "sobel":
        sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
        sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
        filtered_image=(cv.bitwise_and(sobelx, sobely))
    if name == "laplaciano":
        filtered_image=(cv.Laplacian(img, cv.CV_64F))
    if name == "edge":
        filtered_image=(cv.Canny(img, lower_threshold, upper_threshold))
        
    return filtered_image

def plotImages(img, filtered_images, titles):
    plt.figure(figsize=(24, 16))
    plt.subplot(1, len(filtered_images) + 1, 1)
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title("Imagem Original")
    
    for i, filtered_img in enumerate(filtered_images):
        plt.subplot(1, len(filtered_images) + 1, i + 2)
        plt.imshow(cv.cvtColor(filtered_img, cv.COLOR_BGR2RGB) if len(filtered_img.shape) == 3 else filtered_img, cmap='gray')
        plt.title(titles[i])

    plt.show()

def main():
    img = cv.imread("imagem.png", cv.IMREAD_GRAYSCALE)
    media = filtragem(img, "media")
    gaussian = filtragem(img, "gaussiano")
        
    mediana = filtragem(img, "mediana")
    sobel = filtragem(img, "sobel")
    laplaciano = filtragem(img, "laplaciano")
    edge = filtragem(img, "edge")
    
    titles = ["Filtro de Média", "Filtro Gaussiano", "Filtro de Mediana", "Filtro Sobel", "Filtro Laplaciano", "Detecção de Bordas"]
    
    plotImages(img, [media, gaussian, mediana, sobel, laplaciano, edge], titles)
    
if __name__ == "__main__":
    main()
