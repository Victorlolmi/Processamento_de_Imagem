
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tempfile
from deepface import DeepFace
import pickle

# pip install deepface pandas opencv-python-headless


def generateFolderWithFaces(output_folder, video_path, target_image_path, match_threshold, threshold_faces=20, step_frame=50):
    detected_faces_list = []  # Lista para armazenar as faces detectadas
    detected_faces_counter = 0
    frame_counter = 0

    # Carregue a imagem alvo
    target_image = cv2.imread(target_image_path)

    # Carregue o vídeo
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        # Contabiliza frames
        frame_counter += 1

        # Pega o próximo frame
        ret, frame = cap.read()

        # Acabou o vídeo ou detectou o limite de faces?
        if not ret or detected_faces_counter >= threshold_faces:
            break

        # "Pula" alguns frames
        if frame_counter % step_frame != 0:
            continue

        # Detecte as faces no frame usando DeepFace
        detected_faces = DeepFace.analyze(frame, actions=['detect_face'], enforce_detection=False)

        if len(detected_faces) > 0:
            for i, face in enumerate(detected_faces):
                # Verifique se a face é igual à imagem alvo
                (x, y, w, h) = (int(face['region']['x']), int(face['region']['y']), int(face['region']['w']), int(face['region']['h']))
                face_crop = frame[y:y + h, x:x + w]

                # Compara as imagens usando o histograma de cores e a métrica de correlação
                correlation = cv2.compareHist(cv2.calcHist([target_image], [0], None, [256], [0, 256]),
                                              cv2.calcHist([face_crop], [0], None, [256], [0, 256]),
                                              cv2.HISTCMP_CORREL)

                if correlation >= match_threshold:
                    # Adicionar a face detectada à lista
                    detected_faces_list.append(face_crop)

                    # Total de faces detectadas até o momento
                    detected_faces_counter += 1
                    # Salvar região das faces em uma pasta
                    img_path = os.path.join(output_folder, f"face_{detected_faces_counter}_{frame_counter}.jpg")
                    cv2.imwrite(img_path, face_crop)

                    # Adicionar retângulo ao redor da face e marcações para exibir bonitinho
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 4)

    # Fechar o vídeo após processamento
    cap.release()

    # Retornar a lista de faces detectadas
    return detected_faces_list



#Leon

# Caminho para o vídeo de entrada
video_path = 'ReconhecimentoFacial/download/leon.mp4'

# Caminho para a foto do rosto da pessoa desejada
foto_path = 'ReconhecimentoFacial/Past_Leon/img1.jpg'

# Pasta para salvar as imagens recortadas
folder_name = 'ReconhecimentoFacial/Past_Leon'

#Defina um limiar de correspondência (ajuste conforme necessário)
match = 0.95  # Valor próximo de 1 para correspondências muito parecidas

#leon = generateFolderWithFaces(folder_name, video_path, foto_path, match)

#Nilce

# Caminho para o vídeo de entrada
video_path = 'ReconhecimentoFacial/download/vid_nilce.mp4'

# Caminho para a foto do rosto da pessoa desejada
foto_path = 'ReconhecimentoFacial/Past_Nilce/img1.jpg'

# Pasta para salvar as imagens recortadas
folder_name = 'ReconhecimentoFacial\Past_Nilce'

#Defina um limiar de correspondência (ajuste conforme necessário)
match = 0.82  # Valor próximo de 1 para correspondências muito parecidas

Nilce_faces = generateFolderWithFaces(folder_name, video_path, foto_path, match)

# Mostrar as imagens das faces detectadas usando o matplotlib
num_faces = len(Nilce_faces)
fig, axes = plt.subplots(nrows=1, ncols=num_faces, figsize=(16, 4))

for i, face in enumerate(Nilce_faces):
    axes[i].imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
    axes[i].set_title(f'{i + 1}')
    axes[i].axis('off')

plt.show()