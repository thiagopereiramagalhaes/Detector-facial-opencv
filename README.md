# Detector facial
## Detecção facial com python e openCV

Para o desenvolvimento deste projeto usamos o python3 e openCV.

Você pode obter o python em **python.org** e o openCV com o pip:

`
pip install opencv-python
`

Este projeto consiste em um detector de faces com haarcascade.

1 - Primeiramente vamos começar importando o openCV:

`
import cv2
`

2 - Vamos passar o caminho dos haarcascades: 

O algoritmo Haar Cascade, é um algoritmo de detecção de objetos, que utiliza diversos classificadores.

**Frontal face: Responsável por classificar a parte frontal de uma pessoa.**

`
classificador = cv2.CascadeClassifier('haarcascade/haarcascade-frontalface-default.xml')
`

**Eye: Classificar os olhos em uma face.**

`
classificadorOlho = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
`

3 - Passamos o dispositivo de câmera que pretendemos usar e o tamanho da janela da aplicação:

`
camera = cv2.VideoCapture(0)
`

`
largura, altura = 220, 220
`

4 - A seguir:

`
  while True:
`

  A - O dispositivo começa a gravar em loop:
  
  `
      conectado, imagem = camera.read()
  `
  
  B - As imagens são convertidas em escala de cinza:
  
  `
      imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
  `
  
  C - As imagens são processadas pelo classificador:
  
  `
      facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))
  `
 
  D - É desenhado retângulos ao redor da face e dos olhos:
  
  `
      for x, y, l, a in facesDetectadas:
  `
  
  `
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
  `
  
  `
        regiao = imagem[y:y + a, x:x + l]
  `
  
  `
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
  `
  
  `
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
  `

  `
        for ox,oy,ol,oa in olhosDetectados:
  `
  
  `
            cv2.rectangle(regiao, (ox,oy), (ox + ol, oy + oa), (0, 0, 255), 2)
  `
  
  E - Uma janela com a live e todas as informações é aberta:
 
  `
    cv2.imshow("Detector", imagem)
  `
  
  `  
    cv2.waitKey(1)
  `
  
5 - Libera memória e fecha todas as janelas abertas:
 
`
camera.release()
`

`
cv2.destroyAllWindows()
`
