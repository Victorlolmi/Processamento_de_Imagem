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

def PeB_histogram():

    gray_img = cv2.imread("Topico6\imgs\campo_de_flores.jpg",0)

    #nao precisa tranformar a img em cinza, ao dar o canl ja faz automaticamente

    histogram = cv2.calcHist([gray_img], [0], None, [256], [0,256])

    #mostra a imagem cinza
    cv2.imshow("Imagem cinza", gray_img)

    #plotar o histograma
    plt.figure()
    plt.title("Historgrama de escala de cinza")
    plt.xlabel("Bings")
    plt.ylabel("# de pixels")
    plt.plot(histogram)
    plt.xlim([0,256])
    plt.show()

    #espera uma tecla ser precionada 
    cv2.waitKey(0)
    #fecha as janelas abertas
    cv2.destroyAllWindows()

def RGB_histogram():

    RGB_img = cv2.imread("Topico6\imgs\campo_de_flores.jpg")

    #Calcula o histograma para cada cor
    colors = ('b','g', 'r')
    for i, color in enumerate(colors):
        histogram = cv2.calcHist([RGB_img], [i], None, [256], [0,256])
        plt.plot(histogram, color = color)
        plt.xlim([0,256])

    #Mostra a imagem RGB
    cv2.imshow("Imagem colorida",RGB_img)

    #plotar o histograma
    plt.title("Historgrama Colorido")
    plt.xlabel("Bings")
    plt.ylabel("# de pixels")
    plt.show()

    #espera uma tecla ser precionada 
    cv2.waitKey(0)
    #fecha as janelas abertas
    cv2.destroyAllWindows()

def PeB_histogram_equalization():

    gray_img = cv2.imread("Topico6\imgs\campo_de_flores.jpg",0)

    # equaliza o istograma da img
    equalization = cv2.equalizeHist(gray_img)

    showImages([gray_img, equalization], ['Original', 'Equalizada'], size=(7,4), grid=(1,2))

def RGB_histogram_equalization():

    RGB_img = cv2.imread("Topico6\imgs\campo_de_flores.jpg")

    ycrcb = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2YCrCb)

    ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])

    equ = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2RGB)
    
    RGB_img = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2RGB)

    showImages([RGB_img, ycrcb, equ],['Original', 'Ycrcb', 'Equalizada', ], size=(20,10), grid=(1,3))

PeB_histogram()

RGB_histogram()

PeB_histogram_equalization()

RGB_histogram_equalization()