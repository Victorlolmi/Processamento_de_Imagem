#import numpy as np
import cv2
import os

def createImages(img):
    copyImg = img.copy()
    contrastValue = 0

    height, width, channels = img.shape
    
    incrementAux = 0
    while contrastValue < 100:
        for y in range(height):
            for x in range(width):
                for c in range(channels):
                    copyImg[y][x][c] = img[y][x][c] * (contrastValue/100)
        copyImg = cv2.convertScaleAbs(img, alpha= contrastValue/100)
        cv2.imwrite("Head/04_1_Animation/img/Img_" + str(incrementAux) + ".png", copyImg)
        incrementAux += 1
        contrastValue += 10

def createVideo(width, height):
    imageFolder = "Head/04_1_Animation/img"

    images = [img for img in os.listdir(imageFolder)]

    video = cv2.VideoWriter("Head/04_1_Animation/Video.avi", 0, 3, (width, height))

    for img in images:
        video.write(cv2.imread(os.path.join(imageFolder, img)))
    
    for img in reversed(images):
        video.write(cv2.imread(os.path.join(imageFolder, img)))

    video.release()




def main():

    img = cv2.imread("Head/04_1_Animation/OG.png")

    height, width, _ = img.shape
    
    createImages(img)
    createVideo(width, height)

main()
