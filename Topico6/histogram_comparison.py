import cv2
import matplotlib.pyplot as plt
import numpy as np

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

def showIntensityLevels():
    #carrega as imgs

    image_1 = cv2.imread("Topico6\imgs\squid_game_1.jpg",0)
    image_2 = cv2.imread("Topico6\imgs\squid_game_2.jpg",0)

    showImages([image_1, image_2], ['Boneca 1', 'Boneca 2'], size=(7,4), grid=(1,2))

    #calcula hist
    #pq 256
    hist1 = cv2.calcHist([image_1], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([image_2], [0], None, [256], [0,256])

    #normaliza os hist
    hist1 = cv2.normalize(hist1,hist1)
    hist2 = cv2.normalize(hist2,hist2)

    #plot hist
    plt.figure(figsize=(8,4))

    plt.plot(hist1, color = 'blue', label = 'Image 1')
    plt.plot(hist2, color = 'red', label = 'Image 2')

    plt.title('Comparcao de histogramas')
    plt.xlabel('Niveis de intencidade')
    plt.ylabel('Quantidade de pixels')
    plt.legend()
    plt.show()

showIntensityLevels()

#comparando o histograma de imagens em uma pasta 

import glob

def listJpgFiles(diretorio):
    # glob aqui obtem a lista de aquivos jpg de uma pasta
    aquivos_jpg = glob.glob(diretorio + '/*.jpg')

    return aquivos_jpg

def calculateHistogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0,256])
    histogram = cv2.normalize(histogram,histogram)
    return histogram

files_jpg = listJpgFiles("Topico6\imgs")

target_img = cv2.imread("Topico6\imgs\squid_game_1.jpg",0)

target_histogram = calculateHistogram(target_img)

#dicionario para armazenar o nome do arquivo e o valor de correlacao
comparison = {}

#calcular hist para cada imagem e compara-o com a imagem alvo
for file in files_jpg:

    img = cv2.imread(file, 0 )
    histogram_img = calculateHistogram(img)
   
    comparison_value = cv2.compareHist(target_histogram, histogram_img, cv2.HISTCMP_CORREL)
    
    comparison[file] = comparison_value

#ordena o dicionario de comparacoes em ordem decrescente

ordered_comparison = sorted(comparison.items(), key = lambda x: x[1], reverse=True)

#imprime o ranking

for i, (file, comparison) in enumerate(ordered_comparison):
    print(f"Ranking{i+1}: {file}, comparacao: {comparison}")