
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog as fd


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

def applyHiPass(img):
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
    filtered_image = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    filtered_image = cv.convertScaleAbs(filtered_image)
    return filtered_image 

def applyLoPass(img):
    kernel_size = (5,5)
    filtered_image=(cv.blur(img, kernel_size))
    return filtered_image

def enhance(img1, img2):
    enhanced = cv.addWeighted(img1, 0.2, img2, 0.8, 0, dtype=cv.CV_64F)
    return enhanced

def LoadImage():
    global filename
    filename = fd.askopenfilename(title="Selecione uma imagem", filetypes=[("Imagens", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if filename:
        label.config(text=f"Imagem selecionada: {filename}")

def Aprimorar():
    global filename
    if(filename != ""):
        img =cv.imread(filename, cv.IMREAD_GRAYSCALE)
        highPass = applyHiPass(img)
        lowPass = applyLoPass(img)
        enhanced = enhance(highPass, lowPass)
        showImages([img, highPass, lowPass, enhanced], ["original","HighPass", "LowPass", "Enhanced"],(10,7),(1,4))
    else:
        label.config(text=f"Nenhum arquivo selecionado")

    pass

filename = ""
janela = tk.Tk()
janela.title("Aprimoramento de Imagem")
botaoLoad = tk.Button(janela, text="Carregar Imagem", command=LoadImage)
botaoAplicar= tk.Button(janela, text="Aprimorar", command=Aprimorar)
botaoLoad.pack(pady=10)
botaoAplicar.pack(pady=10)
label = tk.Label(janela, text="")
label.pack()
janela.mainloop()