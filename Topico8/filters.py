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

def blurFilter(image):

    blur_img = cv2.blur(image,(5,5))

    showImages([image, blur_img], ['Original', 'average filter'], size=(10,10), grid=(1,2))

    return blur_img

def gaussianFilter(image):

    blur_img = cv2.GaussianBlur(image,(5,5),0)

    showImages([image, blur_img], ['Original', 'Gaussian filter'], size=(10,10), grid=(1,2))

    return blur_img
    
def medianFilter(image):

    median_img = cv2.medianBlur(image, 11)

    showImages([image, median_img], ['Original', 'Median Filter'], size=(10,10), grid=(1,2))

    return median_img

def sobelFilter(gray_image):

    img_sobelx = cv2.Sobel(src= gray_image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3 )
    img_sobely = cv2.Sobel(src= gray_image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3 )
    #img_sobelxy = cv2.Sobel(src= gray_image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3 )
    img_sobelxy = cv2.addWeighted(img_sobelx, 0.5, img_sobely, 0.5,0)

    return img_sobelx, img_sobely, img_sobelxy

def laplacianFilter(gray_image):

    laplacian_img3 = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=3)

    blur_img = blurFilter(gray_image)

    laplacian_img5 = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=5)
    
    blur_more_laplacian_img3 = cv2.Laplacian(blur_img, cv2.CV_64F, ksize=3)

    blur_more_laplacian_img5 = cv2.Laplacian(blur_img, cv2.CV_64F, ksize=5)
    
    return laplacian_img3, laplacian_img5, blur_more_laplacian_img3, blur_more_laplacian_img5

def cannyFilter(gray_img, min, max):

    cannyimg = cv2.Canny(gray_img, min, max)

    return cannyimg
#filtragem passa-Baixa(suavizacao) Retem a alta frequencia
#passa so a baixa frequencia( onde nao se tem muita variacao de cor)

#filtro da media(blur)

img = cv2.imread("Topico8\imgs\img_icons.png")

blur = blurFilter(img)

#filtroGaussiano

gaussian = gaussianFilter(img)

showImages([img, blur, img, gaussian], ('Original', 'Blur por media', 'Original', 'Gaussian Blur'), size=(10,10), grid=(2,2))

#Filtro de Mediana

noise_img = cv2.imread("Topico8\imgs\img_flowers.jpg")

medianFilter(noise_img)

wall_img = cv2.imread("Topico8\imgs\img_parede.jpg")
original=wall_img
wall_img = cv2.cvtColor(wall_img, cv2.COLOR_BGR2GRAY)
imgx, imgy, imgxy = sobelFilter(wall_img)
wall_img = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

showImages([wall_img, imgx, imgy, imgxy],['Original','Sobelx','Sobely','Sobelxy'], size=(10,10), grid=(2,2))

#transforma os pixels de negativos para a escala de 0 a 255
imgx = cv2.convertScaleAbs(imgx)
imgy = cv2.convertScaleAbs(imgy)
imgxy = cv2.convertScaleAbs(imgxy)


showImages([wall_img, imgx, imgy, imgxy],['Original','Sobelx','Sobely','Sobelxy'], size=(10,10), grid=(2,2))

#laplaciano 

wall_img = cv2.imread("Topico8\imgs\img_icons.png")
original=wall_img
wall_img = cv2.cvtColor(wall_img, cv2.COLOR_BGR2GRAY)

laplacian_img3, laplacian_img5, blur_more_laplacian_img3, blur_more_laplacian_img5 = laplacianFilter(wall_img)

laplacian_img3 = cv2.convertScaleAbs(laplacian_img3)
laplacian_img5 = cv2.convertScaleAbs(laplacian_img5)
blur_more_laplacian_img3 = cv2.convertScaleAbs(blur_more_laplacian_img3)
blur_more_laplacian_img5 = cv2.convertScaleAbs(blur_more_laplacian_img5)
wall_img = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
showImages([wall_img, laplacian_img3, blur_more_laplacian_img3, laplacian_img5, blur_more_laplacian_img5], ['Original', 'Laplacian 3', 'Blur + Laplacian 3', 'Lapacian 5', 'Blur + Laplacian 5'], size=(10,7), grid=(2,3))


#CannyEdga
wall_img = cv2.imread("Topico8\imgs\img_parede.jpg")
original=wall_img
wall_img = cv2.cvtColor(wall_img, cv2.COLOR_BGR2GRAY)


canny_img = cannyFilter(wall_img, min=175,max = 255)
wall_img = cv2.cvtColor(wall_img, cv2.COLOR_GRAY2RGB)
showImages([wall_img, canny_img], ['Original', 'Canny Edga'], size=(10,7), grid=(1,2))
