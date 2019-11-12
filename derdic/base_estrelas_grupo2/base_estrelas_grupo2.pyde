

estrelas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de estrelas """
    # fullScreen()
    size(800, 600)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2., height / 2. # floats
    for _ in range(6):
        e = Estrela(meia_largura, meia_altura)
        estrelas.append(e)

def draw():
    """ Limpa a tela, desenha e atualiza estrelas """
    background(0)  # atualização do desenho, fundo preto
    for estrela in estrelas:
        estrela.desenha()
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
        self.cor = color(247,  # R
                         176,  # G
                         142,  # B
                         200)  # alpha

    def desenha(self,pontas=10, raio1=25, raio2=100):
        """ Desenha polígono em torno das coordenadas do objeto """
        noStroke()
        fill(self.cor)
        pushMatrix()
        translate(self.x, self.y)
        estrela(0, 0, 4, raio1*.8, raio2*.8)
        rotate(QUARTER_PI)
        estrela(0, 0, 4, raio1, raio2)
        # estrela(0, 0, 4, raio1 * .7, raio2 * . 7)
        popMatrix()
    
    def anda(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += self.vx
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
