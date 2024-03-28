import cv2
from matplotlib import pyplot as plt

def display(image):
    plt.imshow(image)
    plt.show()

def displayMultiple(image1, image2, image3, image4, image5, image6, figSizeX, figSizeY):
    fig = plt.figure(figsize=(figSizeX,figSizeY))
    fig.add_subplot(2, 3, 1)
    plt.imshow(image1)
    plt.title("Imagem Média")

    fig.add_subplot(2, 3, 2)
    plt.imshow(image2)
    plt.title("Imagem Gaussiana")

    fig.add_subplot(2, 3, 3)
    plt.imshow(image3)
    plt.title("Imagem Mediana")

    fig.add_subplot(2, 3, 4)
    plt.imshow(image4)
    plt.title("Imagem Sobel")

    fig.add_subplot(2, 3, 5)
    plt.imshow(image5)
    plt.title("Imagem Laplaciana")

    fig.add_subplot(2, 3, 6)
    plt.imshow(image6)
    plt.title("Imagem Canny Edge")

    plt.show()

def displayCombination(image1, image2, image3, image4, figSizeX, figSizeY):
    fig = plt.figure(figsize=(figSizeX,figSizeY))
    fig.add_subplot(1, 4, 1)
    plt.imshow(image1)
    plt.title("Imagem Original")

    fig.add_subplot(1, 4, 2)
    plt.imshow(image2)
    plt.title("Imagem Lowpass")

    fig.add_subplot(1, 4, 3)
    plt.imshow(image3)
    plt.title("Imagem Highpass")

    fig.add_subplot(1, 4, 4)
    plt.imshow(image4)
    plt.title("Imagem Combinada")

    plt.show()


def BGRToRGB(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def BGRToGRAY(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image

def RGBToGRAY(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image

def GRAYToRGB(image):

    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    return image

def filterAverage(img, ksize1, ksize2):
    img = cv2.blur(img, (ksize1, ksize2))
    return img

def filterGauss(img, ksize1, ksize2):
    img = cv2.GaussianBlur(img,(ksize1,ksize2),cv2.BORDER_DEFAULT) 
    return img

def filterMedian(img, ksize):
    img = cv2.medianBlur(img, ksize)
    return img

def filterSobel(img, ksize):
    img = BGRToGRAY(img)
    imgx = cv2.Sobel(img, ddepth=-1, dx=1, dy=0, ksize=ksize)
    imgy = cv2.Sobel(img, ddepth=-1, dx=0, dy=1, ksize=ksize)
    imgxy = blendSame(imgx, imgy, 0.5, 0.5)
    return imgxy

def filterLaplacian(img, ksize):
    img = BGRToGRAY(img)
    img = cv2.Laplacian(img, ddepth=-1, ksize=ksize, scale=1)
    return img

def filterCannyEdge(img, t_lower, t_upper):
    img = BGRToGRAY(img)
    img = cv2.Canny(img, t_lower, t_upper)
    return img

def conv2d(source_image, matrix):
    pass

def blendGray(imgA, imgB, pct1, pct2):
    imgB = GRAYToRGB(imgB)
    resImage = cv2.addWeighted(imgA, pct1, imgB, pct2, 0)
    return resImage

def blendSame(imgA, imgB, pct1, pct2):
    resImage = cv2.addWeighted(imgA, pct1, imgB, pct2, 0)
    return resImage

def aprimora_imagem(imgOg, imgLowpass, imgHighpass, pct1, pct2):
    resImage = blendSame(imgOg, imgLowpass, pct1, pct2)
    resImage = blendGray(resImage, imgHighpass, pct1, pct2)

    cv2.imwrite("images/imgOg.png", BGRToRGB(imgOg))
    cv2.imwrite("images/imgLowpass.png", BGRToRGB(imgLowpass))
    cv2.imwrite("images/imgHighpass.png", BGRToRGB(imgHighpass))
    cv2.imwrite("images/resImage.png", BGRToRGB(resImage))

    return resImage

def main():
    img = cv2.imread("07_Filtros/images/03.jpg")
    img = BGRToRGB(img)

    ksizeA = 11
    ksizeB = 11
    ksizeUnico = 3
    CannyT_upper = 255
    CannyT_lower = 200

    imgAverage = filterAverage(img, ksizeA, ksizeB)
    imgGauss = filterGauss(img, ksizeA, ksizeB)
    imgMedian = filterMedian(img, ksizeUnico)
    imgSobel = filterSobel(img, ksizeUnico)
    imgLaplace = filterLaplacian(img, ksizeUnico)
    imgCannyEdge = filterCannyEdge(img, CannyT_lower, CannyT_upper)
    displayMultiple(imgAverage, imgGauss, imgMedian, imgSobel, imgLaplace, imgCannyEdge, 12, 7)
    imgAprimorada = aprimora_imagem(img, imgMedian, imgCannyEdge, 0.8, 0.2)
    displayCombination(img, imgMedian, imgCannyEdge, imgAprimorada, 12, 5)

main()