import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def showImages(imgsArray, titlesArray, size, grid=(1,1)):

    y, x = grid
    _ , axes = plt.subplots(y, x, figsize = size)
    axes = axes.ravel() if isinstance(axes, np.ndarray) else np.array([axes])

    if len(imgsArray) != len(titlesArray):
        print("Error: the numbers of images and titles has to be the same!")
        return
    
    for idx, (img,title) in enumerate(zip(imgsArray, titlesArray)):
        if len(img.shape) == 2: # gray
            axes[idx].imshow(img, cmap='gray')
        else : # RGB
            axes[idx].imshow(img)
        axes[idx].set_title(title, fontdict={'fontsize':18, 'fontweight': 'medium'}, pad=10)
        if len(title) == 0:
            axes[idx].axis('off')

    plt.tight_layout() 
    plt.show()

def detctorDeBordas(img):
    # matriz 5x5 
    kernel = np.ones((5,5),np.uint8)
    # gradiente morfologico 
    gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    
    return gradient


img = cv.imread("Topico9\imgs\image.PNG",  cv.IMREAD_GRAYSCALE)

output_img = detctorDeBordas(img)

showImages([img, output_img],['Original','Bordas'],(10,6),(1,2))




