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


def cutOutBlack(image):

    imagecopy = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _ , thresholded_mask = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU  )

    imagecopy = cv2.cvtColor(imagecopy, cv2.COLOR_BGR2RGB)

    result = cv2.bitwise_and(imagecopy, imagecopy, mask = thresholded_mask)

    


    return thresholded_mask, result 

def cutOutWhite(image):
    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _ , thresholded_mask = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU )

    result = cv2.bitwise_not(image, image, mask = thresholded_mask)

    result = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)


    return thresholded_mask, result 


mail = cv2.imread("Topico7\imgs\carta_getulio.jpg")

thresholded_img , result= cutOutBlack(mail)

image = cv2.cvtColor(mail, cv2.COLOR_BGR2RGB)

showImages([image, thresholded_img, result], ['Original image', 'Imagem limiarizada', 'Resultado'], size=(10,7) , grid=(1,3))

map_img1 = cv2.imread("Topico7\imgs\img_map1.jpg")
map_img2 = cv2.imread("Topico7\imgs\img_map2.jpg")
map_img3 = cv2.imread("Topico7\imgs\img_map3.jpg")

#map1
thresholded_img1, result1 = cutOutWhite(map_img1)
map_img1 = cv2.cvtColor(map_img1, cv2.COLOR_BGR2RGB)
showImages([map_img1, thresholded_img1, result1], ['Mapa 1', 'Limiarizada', 'Resultado'], size=(10,7) , grid=(1,3))

#map2
thresholded_img2, result2 = cutOutWhite(map_img2)
map_img2 = cv2.cvtColor(map_img2, cv2.COLOR_BGR2RGB)
showImages([map_img2, thresholded_img2, result2], ['Mapa 2', 'Limiarizada', 'Resultado'], size=(10,7) , grid=(1,3))

#map3
thresholded_img3, result3 = cutOutWhite(map_img3)
map_img3 = cv2.cvtColor(map_img3, cv2.COLOR_BGR2RGB)
showImages([map_img3, thresholded_img3, result3], ['Mapa 3', 'Limiarizada', 'Resultado'], size=(10,7) , grid=(1,3))


#allmaps
showImages([map_img1, thresholded_img1, result1, map_img2, thresholded_img2, result2, map_img3, thresholded_img3, result3 ], ['Mapa 1', 'Limiarizada', 'Resultado', 'Mapa 2', 'Limiarizada', 'Resultado','Mapa 3', 'Limiarizada', 'Resultado'], size=(10,7) , grid=(3,3))

