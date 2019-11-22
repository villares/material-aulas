# Reduzir
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
    global cor1, cor2, cor3
    if keyPressed:
        cor1 = color(*coresB[0])
        cor2 = color(*coresB[1])
        cor3 = color(*coresB[2])
    else:
        cor1 = color(*coresB[3])
        cor2 = color(*coresB[4])
        cor3 = color(*coresB[5])

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


    def desenha(self,id, pontas=10, raio1=50, raio2=100):
        """ Desenha polígono em torno das coordenadas do objeto """
        noStroke()
        # fill(self.cor)
        stroke(cor2)
        fill(triangulo(cor1, cor2, cor3, map(mouseX, 0, width, 0, 360)))
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
    
def triangulo(a, b, c, v):
    if 0 <= v < 60 or v == 360:
        return a
    if 60 <= v < 120:
        t = map(v, 60, 120, 0, 1)
        return lerpColor(a, b, t)
    if 120 <= v < 180:
        return b
    if 180 <= v < 240:
        t = map(v, 180, 240, 0, 1)
        return lerpColor(b, c, t)
    if 240 <= v < 300:
        return c
    if 300 <= v < 360:
        t = map(v, 300, 360, 0, 1)
        return lerpColor(c, a, t)
