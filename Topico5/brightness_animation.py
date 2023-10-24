
import cv2
import os

def GenerateImages(img):
    #utiliza uma copia da imagem 
    copyImg = img.copy()
    #valor do contraste 
    contrastValue = 0
    #retira as dimecoes e os canais da img
    height, width, channels = img.shape
    
    imgNumb = 0
    #looping para gerar imgs com os niveis de contraste 
    while contrastValue < 100:
        
        #altera o contraste da img
        copyImg = cv2.convertScaleAbs(img, alpha= contrastValue/100)
        #baixa a img na pasta
        cv2.imwrite("Topico5/imgs/img_" + str(imgNumb) + ".png", copyImg)
        #aumenta o contador
        imgNumb += 1
        #aumenta o nivel de contraste 
        contrastValue += 10

def GenerateAviVideo(width, height):
    #caminho da pasta
    imageFolder = "Topico5/imgs"
    #img recebe as imgs da pasta 
    images = [img for img in os.listdir(imageFolder)]
    #escreve o arquivo do video avi
    video = cv2.VideoWriter("Topico5/output_video.avi", 0, 5, (width, height))

    #para cada img em img adiciona a mesma no video
    for img in images:
        video.write(cv2.imread(os.path.join(imageFolder, img)))
    #faz a adicao de forma reversa
    for img in reversed(images):
        video.write(cv2.imread(os.path.join(imageFolder, img)))
    
    video.release()



#carrega a imagem 
img = cv2.imread("Topico5/old_cartoon.png")

#retira altura e largura 
height, width, _ = img.shape

#funcao de gerar as imagens com brilho alterado
GenerateImages(img)
#funcao de juntar as imgs no formato avi
GenerateAviVideo(width, height)


