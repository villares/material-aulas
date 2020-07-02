
# Paleta A - grupo 2
coresA = [(255, 82, 0), (255, 247, 0), (0, 238, 255),
          (79, 0, 255), (0, 255, 249), (255, 255, 255)]

estrelas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de estrelas """
    # fullScreen()
    size(600, 800)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2., height / 2.  # floats
    for _ in range(6):
        e = Estrela(random(width), random(height))
        estrelas.append(e)

def draw():
    """ Limpa a tela, desenha e atualiza estrelas """
    colorMode(RGB)
    global cor1, cor2, cor3
    if keyPressed:
        cor1 = color(*coresA[0])
        cor2 = color(*coresA[1])
        cor3 = color(*coresA[2])
    else:
        cor1 = color(*coresA[3])
        cor2 = color(*coresA[4])
        cor3 = color(*coresA[5])

    background(0)  # atualização do desenho, fundo preto
    for i, estrela in enumerate(estrelas):
        cor = (triangulo(cor1, cor2, cor3, map(mouseX, 0, width, 0, 360)))
        estrela.desenha(cor)
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
        self.vx = random(-2, 2)
        self.vy = random(-5, -1)
        sorteio = random(255)


    def desenha(self, cor, pontas=10, raio1=25, raio2=100):
        """ Desenha polígono em torno das coordenadas do objeto """
        noStroke()
        fill(cor)
        pushMatrix()
        translate(self.x, self.y)
        estrela(0, 0, 4, raio1 * .8, raio2 * .8)
        rotate(QUARTER_PI)
        estrela(0, 0, 4, raio1, raio2)
        # estrela(0, 0, 4, raio1 * .7, raio2 * . 7)
        popMatrix()

    def anda(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += 5 * sin(radians(frameCount * 2))
        self.y += self.vy
        if keyPressed and keyCode == LEFT:
            self.vx = self.vx + 0.1
        if keyPressed and keyCode == RIGHT:
            self.vx = self.vx - 0.1

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
    beginShape()  # comece a forma!
    for p in range(pontos):  # para cada p
        angulo = radians(p * parte)  # calcula angulo
        if p % 2 == 0:  # se for par
            raio = raio1
        else:  # senão, se for impar
            raio = raio2
        x = cx + raio * sin(angulo)
        y = cy + raio * cos(angulo)
        vertex(x, y)  # vertex é um ponto
    endShape(CLOSE)  # termina forma


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
