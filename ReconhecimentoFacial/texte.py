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

#plt.show()



def calculate_face_features(image_path, face_cascade):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecte as faces na imagem usando o modelo Haar Cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 1:
        x, y, w, h = faces[0]
        face_roi = gray[y:y + h, x:x + w]

        # Redimensione a imagem da face para o tamanho desejado
        face_roi = cv2.resize(face_roi, (100, 100))

        # Calcule uma característica simples (por exemplo, histograma de intensidades)
        hist = cv2.calcHist([face_roi], [0], None, [256], [0, 256])

        # Normaliza o histograma
        hist /= hist.sum()

        # Transforme o histograma em uma lista unidimensional
        features = hist.flatten()
        return features
    else:
        return None


# Função para calcular os encodings faciais de uma pasta de imagens usando DeepFace
def calculate_face_encodings(folder_name):
    known_encodings = []
    known_names = []

    for filename in os.listdir(folder_name):
        image_path = os.path.join(folder_name, filename)

        # Use o DeepFace para calcular os encodings faciais
        detected_faces = DeepFace.analyze(image_path, actions=['deep_face'], enforce_detection=False)

        if 'deep_face' in detected_faces:
            # Adicione os encodings e nomes conhecidos
            known_encodings.append(detected_faces['deep_face'])
            known_names.append(filename.split('.')[0])  # Use o nome do arquivo como o nome conhecido

    return known_encodings, known_names

# Diretórios das pastas com as imagens de referência
folder_name_leon = 'ReconhecimentoFacial/Past_Leon'
folder_name_nilce = 'ReconhecimentoFacial/Past_Nilce'

# Calcule os encodings faciais para as imagens de referência
encodings_leon, names_leon = calculate_face_encodings(folder_name_leon)
encodings_nilce, names_nilce = calculate_face_encodings(folder_name_nilce)

# Salve os encodings e nomes em um arquivo
data_encoding = {"encodings_leon": encodings_leon, "names_leon": names_leon, "encodings_nilce": encodings_nilce, "names_nilce": names_nilce}

with open("face_encodings.pkl", "wb") as f:
    pickle.dump(data_encoding, f)

# Carregue o arquivo de encodings
data_encoding = pickle.load(open("face_encodings.pkl", "rb"))

# Carregue o vídeo do disco
video_filename = "ReconhecimentoFacial/download/leon&nilce.mp4"
video_capture_input = cv2.VideoCapture(video_filename)

# Inicialize o classificador Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Defina o nome a ser usado se nenhuma correspondência for encontrada
unknown_name = "Desconhecido"

# Defina o arquivo de vídeo de saída
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(video_capture_input.get(cv2.CAP_PROP_FPS))
frame_width = int(video_capture_input.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture_input.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_capture_output = cv2.VideoWriter("output.mp4", fourcc, fps, (frame_width, frame_height))

# Gere o reconhecimento em vídeo para todos os frames
while True:
    # Para cada frame
    success, frame = video_capture_input.read()

    # Se o vídeo acabou, saia do loop
    if not success:
        break

    # Converta o frame para escala de cinza para detecção de faces
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecte as faces no frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Para cada face detectada
    for (x, y, w, h) in faces:
        face_roi = gray_frame[y:y+h, x:x+w]

        # Use o DeepFace para calcular o encoding da face detectada
        detected_face = DeepFace.analyze(frame, actions=['deep_face'])
        if len(detected_face) > 0:
            detected_encoding = detected_face[0]['deep_face']

            # Compare o encoding da face detectada com os encodings conhecidos
            distance_leon = DeepFace.distance([detected_encoding], data_encoding["encodings_leon"])
            distance_nilce = DeepFace.distance([detected_encoding], data_encoding["encodings_nilce"])

            # Determine a pessoa correspondente com base na menor distância
            if min(distance_leon, distance_nilce) <= 0.6:  # Ajuste o limiar conforme necessário
                if distance_leon < distance_nilce:
                    recognized_name = "Leon"
                else:
                    recognized_name = "Nilce"
            else:
                recognized_name = unknown_name

            # Desenhe um retângulo e adicione o nome ao frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            cv2.putText(frame, recognized_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Escreva o frame no arquivo de vídeo de saída
    video_capture_output.write(frame)

# Libere os objetos de captura e gravação de vídeo
video_capture_input.release()
video_capture_output.release()
