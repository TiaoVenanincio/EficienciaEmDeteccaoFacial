import cv2

face_cascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#carrega o algoritmo de haar cascade

video = cv2.VideoCapture("Caso3.avi") #carrega o video

contador = 0
while video.isOpened() and contador < 300:
    validacao, frame = video.read()

    if not validacao:
            break

    if contador % 20 == 0:    #define a quantos frames o reconhecimento será feito 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #transforma o frame colorido em um frame em cinza 

        faces = face_cascade.detectMultiScale(gray, 1.1, 4) #detecta as faces no frame em escalas de cinza

    for (x, y, w, h) in faces: #desenha o retangulo em volta da face reconhecida
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Video com reconhecimento aplicado", cv2.flip(frame,1))
        
    contador += 1
    if cv2.waitKey(5) == 27: #garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura da video
        break
        

video.release()
cv2.destroyAllWindows() #fecha todas as janelas