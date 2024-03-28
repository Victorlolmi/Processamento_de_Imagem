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



def filtering(gray_image, filter_name):

    if filter_name == 'average':
        blur_img = cv2.blur(gray_image,(9,9))
        
        showImages([gray_image, blur_img], ['Gray','Blur image'], size=(7,5), grid=(1,2))
    
    elif filter_name == 'gaussian':
        blur_img = cv2.GaussianBlur(gray_image,(9,9),0)
        showImages([gray_image, blur_img], ['Gray','GaussianBlur image'], size=(7,5), grid=(1,2))
        
    elif filter_name == 'median':
        median_img = cv2.medianBlur(gray_image, 11)
        showImages([gray_image, median_img], ['Gray','Median image'], size=(7,5), grid=(1,2))

    elif filter_name== 'sobel':
        img_sobelx = cv2.Sobel(src= gray_image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3 )
        img_sobely = cv2.Sobel(src= gray_image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3 )
        img_sobelxy = cv2.addWeighted(img_sobelx, 0.5, img_sobely, 0.5, 0)

        imgx = cv2.convertScaleAbs(img_sobelx)
        imgy = cv2.convertScaleAbs(img_sobely)
        imgxy = cv2.convertScaleAbs(img_sobelxy)


        showImages([gray_image, imgx, imgy, imgxy],['Gray','Sobel x','Sobel y','Sobel xy'], size=(10,10), grid=(2,2))

    elif filter_name == 'laplacian':

        laplacian_img = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=3)

        blur_img = cv2.blur(gray_image,(5,5))

        blur_more_laplacian_img = cv2.Laplacian(blur_img, cv2.CV_64F, ksize=3)

        laplacian_img = cv2.convertScaleAbs(laplacian_img)
        blur_more_laplacian_img = cv2.convertScaleAbs(blur_more_laplacian_img)

        showImages([gray_image, laplacian_img, blur_more_laplacian_img], ['Original', 'Laplacian', 'Blur + Laplacian'], size=(10,7), grid=(1,3))

    elif filter_name == 'canny_edge':
        cannyimg = cv2.Canny(gray_image, 30, 255)
        
        showImages([gray_image, cannyimg], ['Original', 'Canny Edge'], size=(10,7), grid=(1,2))
    else:
        print("Digite um filtro existente:")
        print("average, gaussian, median, sobel, laplacian, canny_edge")


image = cv2.imread("Topico8\imgs\cervo.PNG",0)

filter_name = "median"

filtering(image, filter_name)