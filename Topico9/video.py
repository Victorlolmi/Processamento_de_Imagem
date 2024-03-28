import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def BGRToRGB(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def getContour(img):
    result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, (1,1))
    return result

def imgErode(img, kernel, iterations):
    img = cv2.erode(img, kernel, iterations=iterations)
    return img

def imgDilate(img, kernel, iterations):
    img = cv2.dilate(img, kernel, iterations=iterations)
    return img

def createImagesErode(img, kernel, iterations):
    copyImg = img.copy()
    cv2.imwrite("Topico9/videoErode/0.png", copyImg)
    incrementAux = 1
    for i in range(40):
        copyImg = imgErode(copyImg, kernel, iterations)
        cv2.imwrite("Topico9/videoErode/" + str(incrementAux) + ".png", copyImg)
        incrementAux += 1

def createImagesDilate(img, kernel, iterations):
    copyImg = img.copy()
    cv2.imwrite("Topico9/videoDilate/0.png", copyImg)
    incrementAux = 1
    for i in range(20):
        copyImg = imgDilate(copyImg, kernel, iterations)
        cv2.imwrite("Topico9/videoDilate/" + str(incrementAux) + ".png", copyImg)
        incrementAux += 1

def createVideos(width, height):
    imageFolderErode = "Topico9/videoErode/"
    imageFolderDilate = "Topico9/videoDilate/"

    images = [img for img in os.listdir(imageFolderErode)]

    video = cv2.VideoWriter("Topico9/VideoErode.avi", 0, 1, (width, height))

    for img in images:
        video.write(cv2.imread(os.path.join(imageFolderErode, img)))

    video.release()

    images = [img for img in os.listdir(imageFolderDilate)]

    video = cv2.VideoWriter("Topico9/VideoDilate.avi", 0, 1, (width, height))

    for img in images:
        video.write(cv2.imread(os.path.join(imageFolderDilate, img)))

    video.release()


img = cv2.imread("Topico9\imgs\imageJ.PNG")

kernel = np.ones((3, 3), dtype='uint8')
kernel2 = np.ones((5, 5), dtype='uint8')

createImagesErode(img, kernel, 2)
createImagesDilate(img, kernel, 9)
createVideos(558, 743)

