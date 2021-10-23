import cv2

classificador = cv2.CascadeClassifier('haarcascade/haarcascade-frontalface-default.xml')
classificadorOlho = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

camera = cv2.VideoCapture(0)
largura, altura = 220, 220

while True:
    conectado, imagem = camera.read()

    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

    for x, y, l, a in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        regiao = imagem[y:y + a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        for ox,oy,ol,oa in olhosDetectados:
            cv2.rectangle(regiao, (ox,oy), (ox + ol, oy + oa), (0, 0, 255), 2)

    cv2.imshow('Detector', imagem)
    cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()
