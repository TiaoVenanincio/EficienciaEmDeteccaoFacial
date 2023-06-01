#Esse algoritmo usa a biblioteca MediaPipe para a detecção

import cv2
import mediapipe as mp

video = cv2.VideoCapture("Caso3.avi") #carrega o video para o teste

reconhecimento_rosto = mp.solutions.face_detection # ativando a solução de reconhecimento de rosto
desenho = mp.solutions.drawing_utils # ativando a solução de desenho
reconhecedor_rosto = reconhecimento_rosto.FaceDetection() # criando o item que consegue ler uma imagem e reconhecer os rostos ali dentro

contador = 0
while video.isOpened() and contador < 300:
    validacao, frame = video.read() # lê a imagem da webcam
    
    if not validacao:
        break
    
    lista_rostos = reconhecedor_rosto.process(frame) # usa o reconhecedor para criar uma lista com os rostos reconhecidos
    
    if lista_rostos.detections: # caso algum rosto tenha sido reconhecido
        for rosto in lista_rostos.detections: # para cada rosto que foi reconhecido
            desenho.draw_detection(frame, rosto) # desenha o rosto na imagem

    cv2.imshow("Video com reconhecimento aplicado", cv2.flip(frame,1)) # mostra a imagem do video

    contador += 1
    if cv2.waitKey(5) == 27: # ESC # garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura do video
        break

video.release() # encerra a conexão com o video
cv2.destroyAllWindows() # fecha todas as janelas