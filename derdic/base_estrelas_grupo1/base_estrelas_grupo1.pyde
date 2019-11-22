
# Paleta B
coresB = [(0, 255, 77), (109, 0, 255), (255, 0, 255),
          (0, 255, 255), (255, 0, 71), (253, 255, 0)]

estrelas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de estrelas """
    # fullScreen()
    size(800, 600)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2., height / 2. # floats
    for _ in range(6):
        e = Estrela(random(width),random(height))
        estrelas.append(e)

def draw():
    colorMode(RGB)
    if keyPressed:
        cor1 = color(*coresB[0])
        cor2 = color(*coresB[1])
        cor3 = color(*coresB[2])
    else:
        cor1 = color(*coresB[3])
        cor2 = color(*coresB[4])
        cor3 = color(*coresB[5])
    colorMode(HSB)
    global paleta
    paleta = (color(hue(cor1),255,255),
              color(hue(cor2),255,255),
              color(hue(cor3),255,255),
              color(hue(cor1),255,255),
              color(hue(cor2),255,255),
              color(hue(cor3),255,255),
              )   
    """ Limpa a tela, desenha e atualiza estrelas """
    background(0)  # atualização do desenho, fundo preto
    for i, estrela in enumerate(estrelas):
        estrela.desenha(i, pontas=7, raio1=50, raio2=10)
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
        self.vy = random(-2,-4)
        sorteio = random(255)
        self.cor = color(random(255),  # R
                         random(255),  # G
                         random(255),  # B
                         200)  # alpha

    def desenha(self,id, pontas=10, raio1=50, raio2=100):
        """ Desenha polígono em torno das coordenadas do objeto """
        noStroke()
        # fill(self.cor)
        stroke(paleta[id])
        fill(paleta[(id + 1) % 6])
        strokeWeight(5)
        strokeJoin(ROUND)
        # if keyPressed: raio2 = 300
        estrela(self.x, self.y, pontas, raio1 + 50 * sin(frameCount/3.),
                raio2 + 50 * sin(frameCount/3.))
        self.tamanho -=  (self.tamanho + raio2 / 5)
    
    
    def anda(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += self.vx
        self.y += self.vy
        metade = self.tamanho / 2
        if self.x > width + metade:
            self.x = -metade
        if self.y > height + metade:
            self.y = -metade
        if self.x < -metade:
            self.x = width + metade
        if self.y < -metade:
            self.y = height + metade
            
            
def estrela(cx, cy, pontas, raio1, raio2):    
    pontos = pontas * 2
    parte = 360. / pontos
    beginShape() # comece a forma!
    for p in range(pontos): # para cada p
        angulo = radians(p * parte) # calcula angulo
        if p % 2 == 0: # se for par
            raio = raio1
        else: # senão, se for impar
            raio = raio2
        x = cx + raio * sin(angulo)
        y = cy + raio * cos(angulo)
        vertex(x, y) # vertex é um ponto
    endShape(CLOSE) # termina forma
