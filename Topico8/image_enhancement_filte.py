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


def LowPass_BlurFilter(image):

    blur_img = cv2.blur(image,(5,5))

    return blur_img

def HighPass_SobelFilter(gray_image):

    img_sobelx = cv2.Sobel(src= gray_image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3 )
    img_sobely = cv2.Sobel(src= gray_image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3 )
    #img_sobelxy = cv2.Sobel(src= gray_image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3 )
    img_sobelxy = cv2.addWeighted(img_sobelx, 0.5, img_sobely, 0.5,0)

    return img_sobelxy

def blendGray(imgA, imgB, pct1, pct2):
    resImage = cv2.addWeighted(imgA, pct1, imgB, pct2, 0)
    return resImage

def blendSame(imgA, imgB, pct1, pct2):
    resImage = cv2.addWeighted(imgA, pct1, imgB, pct2, 0)
    return resImage

def EnhancementFilter(gray_image,lowpass, highpass, pct1, pct2):

    resImage = blendSame(gray_image, lowpass, pct1, pct2)
    resImage = blendGray(resImage, highpass, pct1, pct2)

    return resImage

gray_image= cv2.imread("Topico8\imgs\img_lorem_ipsum.jpg",0)

lowpass = LowPass_BlurFilter(gray_image)

highpass = HighPass_SobelFilter(gray_image)

highpass = cv2.convertScaleAbs(highpass)

enhanced_img = EnhancementFilter(gray_image, lowpass, highpass, 0.8, 0.2)

showImages([gray_image,lowpass,highpass,enhanced_img], ['Gray Img','LowPass','HighPass','Enhanced'],(10,7),(1,4))

