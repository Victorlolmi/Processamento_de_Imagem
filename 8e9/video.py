import cv2 as cv
import numpy as np

def videoErosao(img):
    num_steps = 100  # Incrementos para os loops
    kernel = np.ones((5, 5), np.uint8)
    largura = 640
    altura = 480
    fps = 30
    codec = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')  # Codec MJPEG

    # Crie um objeto de vídeo para gravar
    img = cv.resize(img, (largura, altura))

    saida_video = cv.VideoWriter('video_saida_erosao.avi', codec, fps, (largura, altura))
    saida_video.write(img)
    
    for i in range(num_steps):
        copyimg = cv.erode(img, kernel, iterations=i)
        copyimg_bgr = cv.cvtColor(copyimg, cv.COLOR_GRAY2BGR)  # Converta para BGR antes de escrever no vídeo
        saida_video.write(copyimg_bgr)

    saida_video.release()
    cv.destroyAllWindows()

def videoDilatacao(img):
    num_steps = 100  # Incrementos para os loops
    kernel = np.ones((5, 5), np.uint8)
    largura = 640
    altura = 480
    fps = 30
    codec = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')  # Codec MJPEG

    # Crie um objeto de vídeo para gravar
    img = cv.resize(img, (largura, altura))

    saida_video = cv.VideoWriter('video_saida_dilatacao.avi', codec, fps, (largura, altura))
    saida_video.write(img)
    for i in range(num_steps):
        copyimg = cv.dilate(img, kernel, iterations=i)
        copyimg_bgr = cv.cvtColor(copyimg, cv.COLOR_GRAY2BGR)  # Converta para BGR antes de escrever no vídeo
        saida_video.write(copyimg_bgr)

    saida_video.release()
    cv.destroyAllWindows()

# Carregar a imagem em escala de cinza
img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)

videoDilatacao(img)
videoErosao(img)
