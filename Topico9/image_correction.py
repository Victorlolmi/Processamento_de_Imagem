import cv2
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

def correcaoPorAbertura(img):
    '''Abertura =   erosao seguida por dilatacao'''
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    limite, imagem_limiarizada = cv2.threshold(opening, 10, 255, cv2.THRESH_BINARY)
    kernel = np.ones((10,10),np.uint8)
    opening = cv2.morphologyEx(imagem_limiarizada, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((3,3),np.uint8)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return closing
    
def correcaoPorFechamento(img):
    kernel = np.ones((4,4),np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    '''Fechamento = dilatacao seguida por erosao'''
    kernel = np.ones((20,20),np.uint8)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return  closing



cervo = cv2.imread("Topico9\imgs\cervo.PNG",  cv2.IMREAD_GRAYSCALE)
moeda = cv2.imread("Topico9\imgs\moeda.PNG",  cv2.IMREAD_GRAYSCALE)

img_cervo = correcaoPorAbertura(cervo)
img_moeda = correcaoPorFechamento(moeda)

showImages([cervo, img_cervo, moeda, img_moeda],['Cervo Orignal','Corrigido','Moeda Original','Corrigida'],(7,7), (2,2))

    
