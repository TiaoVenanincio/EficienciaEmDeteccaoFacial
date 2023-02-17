import cv2

face_cascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

contador = 0
while webcam.isOpened() and contador <300:
    validacao, frame = webcam.read()

    if not validacao:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Video da Webcam Invertido", cv2.flip(frame,1))
        
    key = cv2.waitKey(5)
    if key == 27: # ESC
        break
    contador += 1
    
webcam.release()
cv2.destroyAllWindows()