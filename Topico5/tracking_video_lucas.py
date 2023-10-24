import numpy as np 
import cv2


def TrackbarTreatment():

    #Dicionario Hue
    hue = {}
    hue["min"] = cv2.getTrackbarPos("Min Hue", trackbarWindow)
    hue["max"] = cv2.getTrackbarPos("Max Hue", trackbarWindow)

    if hue["min"] > hue["max"]:
        #seta o valor do maximo para o valor do minimo 
        cv2.setTrackbarPos("Max Hue", trackbarWindow, hue["min"])
        #atualiza o valor maximo
        hue["max"] = cv2.getTrackbarPos("Max Hue", trackbarWindow)
    
    #Dicionario sat
    sat = {}
    sat["min"] = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
    sat["max"] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    if sat["min"] > sat["max"]:
        #seta o valor do maximo para o valor do minimo 
        cv2.setTrackbarPos("Max Saturation", trackbarWindow, sat["min"])
        #atualiza o valor maximo
        sat["max"] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    #Dicionario val
    val = {}
    val["min"] = cv2.getTrackbarPos("Min Value", trackbarWindow)
    val["max"] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    if val["min"] > val["max"]:
        #seta o valor do maximo para o valor do minimo 
        cv2.setTrackbarPos("Max Value", trackbarWindow, val["min"])
        #atualiza o valor maximo
        val["max"] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    return hue, sat, val

def computerTracking(frame, hue, sat, val):
    
    #transforma a imagem de bgr para hsv
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #definir os intervalor de cores que vao aparecer na imagem final
    lowerColor = np.array([hue['min'], sat['min'], val['min']])
    upperColor = np.array([hue['max'], sat['max'], val['max']])

    #definir a mascara com os valores min e max dados
    mask = cv2.inRange(hsvImage, lowerColor, upperColor)

    #Compara a mascara com a imagem 
    result = cv2.bitwise_and(frame, frame, mask = mask)

    #aplica a limiarizacao 
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _,gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #encontra os contornos da regiao (findcontours)
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #se existir contornos
    if contours:
        #retorna a area do primeiro grupo de pixels brancos 
        maxArea = cv2.contourArea(contours[0])
        contour_ID = 0
        i=0
        
    #para cada grupo de pixel branco
    for cnt in contours:
        print(cnt)
        #procura o grupo com maior area
        if maxArea < cv2.contourArea(cnt):
            maxArea = cv2.contourArea(cnt)
            #identificador do contorno de maior area
            contour_ID = i
        i += 1
    
    #Contorno de maior area
    cntMaxArea= contours[contour_ID]
    
    #retorna um retangulo que envolve o contorno
    x, y, w, h = cv2.boundingRect(cntMaxArea)

    #desenha o retangulo na img
    frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    return frame, gray

cap = cv2.VideoCapture(0)

trackbarWindow = "Trackbar Window"

cv2.namedWindow(trackbarWindow)

#retorna oq esta marcado na barrinha da trackbar
def onChange(val):
    return

#criacao da trackbar
#Hue (matiz da cor)
cv2.createTrackbar("Min Hue", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Hue", trackbarWindow, 255, 255, onChange)
#Saturation (tanto que a cor esta misturada com o branco)
cv2.createTrackbar("Min Saturation", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Saturation", trackbarWindow, 255, 255, onChange)
#Value (intencidade luminosa)
cv2.createTrackbar("Min Value", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Value", trackbarWindow, 255, 255, onChange)

#pega o valor da trackbar
min_hue = cv2.getTrackbarPos("Min Hue", trackbarWindow)
max_hue = cv2.getTrackbarPos("Max Hue", trackbarWindow)

min_sat = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
max_sat = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

min_val = cv2.getTrackbarPos("Min Value", trackbarWindow)
max_val = cv2.getTrackbarPos("Max Value", trackbarWindow)

#enquanto dor verdade
while True:

    #pega um frame da web cam
    success, frame = cap.read()

    #Tratamento da Trackbar para o min nao ser maior que o max na hue, sat e val
    hue, sat, val =  TrackbarTreatment()

    frame, gray = computerTracking(frame, hue, sat, val)

    cv2.imshow("Webcam", frame)
    cv2.imshow("Limiarizacao", gray)

    #compara a tecla que foi apertada com a letra dada
    #caso seja sai do loop
    if cv2.waitKey(1) & 0xFF == ord('q') or 0xFF == 27:
        break

#libera os recursos
cap.release
#limpa as janelas
cv2.destroyAllWindows()