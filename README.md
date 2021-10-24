<h1>Detector facial</h1>
<h2>Detecção facial com python e openCV</h2>

<p>Para o desenvolvimento deste projeto usamos o python3 e openCV.</p>
<p>Você pode obter o python em 'python.org' e o openCV com o pip:</p>

<code>pip install opencv-python</code>

<p>Este projeto consiste em um detector de faces com haarcascade.</p>

<ol>
<div name='1'>
<li><h3>Primeiramente vamos começar importando o openCV:</h3></li>
<code>import cv2</code>
</div>
        
<div name='2'>
<li><h3>Vamos passar o caminho dos haarcascades:</h3></li>
<p>O algoritmo Haar Cascade, é um algoritmo de detecção de objetos, que utiliza diversos classificadores.</p>
<ul>
<li>Frontal face: Responsável por classificar a parte frontal de uma face;</li>
<li>Eye: Classificar os olhos em uma face.</li>
</ul>
<code>classificador = cv2.CascadeClassifier('haarcascade/haarcascade-frontalface-default.xml')</code><br>
<code>classificadorOlho = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')</code>
</div>

<div name='3'>
<li><h3>Passamos o dispositivo de câmera que pretendemos usar e o tamanho da janela da aplicação:</h3></li>
<code>camera = cv2.VideoCapture(0)</code><br>
<code>largura, altura = 220, 220</code>
</div>

<div name='4'>
<li><h3>A seguir:</h3></li>
<ol type='A'>
<div name='A'>
<li><h4>O dispositivo começa gravar em loop:</h4></li>
<code>while True:</code><br>
<code>conectado, imagem = camera.read()</code>
</div>

<div name='B'>
<li><h4>As imagens são convertidas em escala de cinza:</h4></li>
<code>imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)</code>
</div>

<div name='C'>
<li><h4>As imagens são processadas pelo classificador:</h4></li>
<code> facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))</code>
</div>

<div name='D'>
<li><h4>É desenhado retângulos ao redor da face e dos olhos:</h4></li>
<code>for x, y, l, a in facesDetectadas:</code><br>
<code>cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)</code><br>
<code>regiao = imagem[y:y + a, x:x + l]</code><br>
<code>regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)</code><br>
<code>olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)</code><br>
<code>for ox,oy,ol,oa in olhosDetectados:</code><br>
<code>cv2.rectangle(regiao, (ox,oy), (ox + ol, oy + oa), (0, 0, 255), 2)</code>
</div>
            
<div name='E'>
<li><h4>Uma janela com a live e todas as informações é aberta:</h4></li>
<code>cv2.imshow("Detector", imagem)</code><br>
<code>cv2.waitKey(1)</code>
</div>
</ol>
</div>
    
<div name='5'>
<li><h3>Libera memória e fecha todas as janelas abertas:</h3></li>
<code>camera.release()</code><br>
<code>cv2.destroyAllWindows()</code>
</div>
</ol>

<h3>Exemplo:</h3>

![Exemplo Detector](https://user-images.githubusercontent.com/51063415/138610489-995329be-d3e8-4b85-8624-758cabc04867.png)


