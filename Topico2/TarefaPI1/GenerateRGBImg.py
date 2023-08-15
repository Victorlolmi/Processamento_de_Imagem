import numpy as np
import cv2

# Cria uma imagem vazia de tamanho 600x300 com 3 canais de cor, np.zeros cria uma matriz introduzida com zeros
obj_image = np.zeros((300, 600, 3), dtype=np.uint8)

# Divide a imagem em três colunas iguais largura/3
third_width = obj_image.shape[1] // 3

# preenche ate o valor third_width 1/3 da imagem com a cor vermelha no canal 3
obj_image[:, :third_width, 0] = 0   # Blue
obj_image[:, :third_width, 1] = 0   # Green
obj_image[:, :third_width, 2] = 255  # Red

# preenche do valor third_width ate 2*third_width 2/3 da imagem com a cor verde no canal 2
obj_image[:, third_width:2*third_width, 0] = 0   # Blue
obj_image[:, third_width:2*third_width, 1] = 255  # Green
obj_image[:, third_width:2*third_width, 2] = 0    # Red

# Preenche a partir do valor third_width ate o fim da matriz  3/3 da imagem com a cor azul no canal 
obj_image[:, 2*third_width:, 0] = 255  # Blue
obj_image[:, 2*third_width:, 1] = 0    # Green
obj_image[:, 2*third_width:, 2] = 0    # Red

# Salva a imagem no disco
cv2.imwrite("Topico2\TarefaPI1\imgs\imagem3.png", obj_image)