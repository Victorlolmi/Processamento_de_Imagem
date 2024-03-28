import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog as fd


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
    enhanced = cv.addWeighted(img1, 0.5, img2, 0.5, 0, dtype=cv.CV_64F)
    return enhanced

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
        plotImages(img, [highPass, lowPass, enhanced], ["HighPass", "LowPass", "Enhanced"])
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