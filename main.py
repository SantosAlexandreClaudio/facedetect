import cv2
print(cv2.__version__)

# URL do DroidCam (substitua pelo seu IP)
url = "http://192.168.0.16:4747/video"

video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Não foi possível acessar a câmera do celular")
    exit()

while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Erro ao capturar vídeo")
        break

    cv2.imshow('Camera do Celular', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture = cv2.VideoCapture(url)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Erro ao capturar vídeo")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    eyes = eyeCascade.detectMultiScale(gray, 1.2, 18)
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    smiles = smileCascade.detectMultiScale(gray, 1.7, 20)
    for (x, y, w, h) in smiles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # MOSTRAR O VÍDEO (fora dos loops)
    cv2.imshow('video', frame)

    # SAIR COM Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()