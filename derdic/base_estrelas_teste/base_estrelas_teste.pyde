add_library('sound') # aviso de que vai usar o microfone

estrelas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de estrelas """
    # fullScreen()
    size(600, 600)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2., height / 2. # floats
    for _ in range(6):
        e = Estrela(meia_largura, meia_altura)
        estrelas.append(e)
    global input, loudness, waveform, samples
    source = AudioIn(this, 0)
    source.start()
    loudness = Amplitude(this)
    loudness.input(source)
    samples = 60
    waveform = Waveform(this, samples)
    waveform.input(source)



def draw():
    """ Limpa a tela, desenha e atualiza estrelas """
    background(0)  # atualização do desenho, fundo preto
    volume = loudness.analyze()
    waveform.analyze()
    for i, estrela in enumerate(estrelas):
        t = int(map(volume, 0, 0.5, 10, 100))
        estrela.desenha(30, t)
        estrela.anda()

class Estrela():
    """ Classe Estrela, cor sorteada, tamanho sorteado por default """

    def __init__(self, px, py, ptamanho=None):
        self.x = px
        self.y = py
        if ptamanho:
            self.tamanho = ptamanho
        else:
            self.tamanho = random(50, 200)
        self.vx = random(-2,2)
        self.vy = random(-3,-4)
        sorteio = random(128)
        self.cor = color(128 + sorteio,  # R
                         0,  # G
                         128 + sorteio,  # B
                         200)  # alpha

    def desenha(self,pontas=10, raio1=50, raio2=100):
        """ Desenha polígono em torno das coordenadas do objeto """
        noStroke()
        fill(self.cor)
        pushMatrix()
        translate(self.x, self.y)
        rotate(radians(frameCount))
        estrela(0, 0, pontas, raio1, raio2)
        popMatrix()
    
    
    def anda(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += self.vx
        self.y += self.vy
        metade = self.tamanho / 2
        if self.x > width + metade:
            self.vx = -self.vx
        if self.y > height + metade:
            self.vy = -self.vy
        if self.x < -metade:
            self.vx = -self.vx
        if self.y < -metade:
            self.vy = -self.vy
            
            
def estrela(cx, cy, pontas, raio1, raio2):    
    pontos = pontas * 2
    parte = 360. / pontos
    beginShape() # comece a forma!
    for p in range(pontos): # para cada p
        angulo = radians(p * parte) # calcula angulo
        w =  1 #int(map(waveform.data[p], -1, 1, 0.2, 2))
        if p % 2 == 0: # se for par
            raio = raio1 * w
        else: # senão, se for impar
            raio = raio2 * w
        x = cx + raio * sin(angulo)
        y = cy + raio * cos(angulo)
        vertex(x, y) # vertex é um ponto
    endShape(CLOSE) # termina forma
