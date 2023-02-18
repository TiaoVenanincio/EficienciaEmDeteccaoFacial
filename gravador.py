import cv2

webcam = cv2.VideoCapture(0) #conecta a webcam ao python

video_cod = cv2.VideoWriter_fourcc(*'XVID') #Cria um codec para o video
video_output = cv2.VideoWriter('Caso3.avi', video_cod, 20,(640,480))
#Nome do arquivo, codec, FPS e tamanho do quadro(640x480)

contador = 0 #para limitar a quantidade de frames a 300
while webcam.isOpened() and contador < 300:
    validacao, frame = webcam.read() #le o frame da webcam

    if not validacao:
            break
    
    video_output.write(frame) #Grava o frame no arquivo

    cv2.imshow("Video da Webcam", cv2.flip(frame,1))
        
    contador += 1
    if cv2.waitKey(5) == 27: #garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura da webcam
        break 

webcam.release() 
video_output.release()
cv2.destroyAllWindows()