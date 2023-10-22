import numpy as np
import cv2

def resizeImage(image, scalePercent):
    width = int(image.shape[1] * scalePercent / 100)
    height = int(image.shape[0] * scalePercent / 100)
    image = cv2.resize(image, (width, height))
    return image

def addWatermark(background, watermark, x_offset, y_offset):
    # Redimensiona a marca d'água para se ajustar à imagem de fundo
    watermark = resizeImage(watermark, scalePercent=20)

    # Obtém as dimensões da imagem de fundo
    bg_height, bg_width, _ = background.shape
    wm_height, wm_width, _ = watermark.shape

    # Verifica se o deslocamento não excede os limites da imagem de fundo
    if x_offset + wm_width > bg_width or y_offset + wm_height > bg_height:
        print("Erro: Sobreposição com dimensões maiores do que a imagem de fundo.")
        return None

    # Cria uma cópia da imagem de fundo para adicionar a marca d'água
    image_with_watermark = background.copy()

    # Define a região da imagem de fundo onde a marca d'água será adicionada
    roi = image_with_watermark[y_offset:y_offset + wm_height, x_offset:x_offset + wm_width]

    # Cria uma máscara de canal alfa para a marca d'água
    alpha_channel = watermark[:, :, 3] / 255.0

    # Combinando a marca d'água com a imagem de fundo usando a máscara alfa
    for c in range(0, 3):
        roi[:, :, c] = (1 - alpha_channel) * roi[:, :, c] + alpha_channel * watermark[:, :, c]

    return image_with_watermark


# Carrega a imagem de fundo e a marca d'água
background = cv2.imread("Topico4\imgs\Mountain 4K.jpg")
watermark = cv2.imread("Topico4\imgs\marcadagua.png", cv2.IMREAD_UNCHANGED)  # Certifique-se de que a marca d'água tenha um canal alfa

# Define as coordenadas para a sobreposição da marca d'água (ajuste conforme necessário)
x_offset = 10
y_offset = 10

# Adiciona a marca d'água à imagem de fundo
result_image = addWatermark(background, watermark, x_offset, y_offset)

if result_image is not None:
    # Salva a imagem resultante
    cv2.imwrite("output_image.png", result_image)
    print("Marca d'água adicionada com sucesso!")
